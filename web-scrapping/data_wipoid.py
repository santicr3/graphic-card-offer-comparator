from requests_html import HTMLSession
import re
import utils

base_url = "https://wipoid.com"
url = base_url + "/componentes/tarjetas-graficas/"

def getAllLiks(url, product_class):
    # Graphic cards URL

    session = HTMLSession()
    r = session.get(url)
    r.status_code
    
    
    # Get all the URL's
    container_elements = r.html.find("h3."+product_class)
    urls = []
    for container in container_elements:
        urls_elements = container.find('a')
        for url_element in urls_elements:
            urls.append(url_element.attrs["href"])

    return urls

urls = []
for i in range(5):
    urls.extend(getAllLiks(url+f'?page={i}', 'product-title'))

# Get data of each product

session = HTMLSession()
data_lines = []
cols = "url,modelo,precio,vram,tipo-vram,hdmi,dp,dimensiones,consumo"
for url in urls:
    print(url)
    r = session.get(url)
    r.status_code
    
    model = r.html.find("h1.product-detail-name", first=True).text
    
    price = r.html.find("span.current-price-value", first=True).text.replace(',','').replace('.','').replace('€','')
    
    attributes = r.html.find("p")

    for attribute in attributes:
        if 'DDR' in attribute.text and len(attribute.text):
            print(attribute.text)
            vram = attribute.text
            vram_array = vram.split(' ')
            vram_type = next((word for word in vram_array if 'DDR' in word), None)
        if 'GB' in attribute.text and len(attribute.text) < 30:
            vram = attribute.text
            vram_array = vram.split(' ')
            vram_size = next((word for word in vram_array if 'GB' in word), None)
            vram_size = utils.vram_size_clean(attribute.text)

        if any(port in attribute.text for port in ['DisplayPort', 'DP', 'HDMI']):
            hdmi, dp = utils.ports_clean(attribute.text)
        
        if re.search(r'\d+w', attribute.text, re.IGNORECASE):   
            consume = utils.consume_clean(attribute.text)

        if 'ventiladores' in attribute.text:
            words = attribute.text.split(' ')
            index_ventiladores = next((word for word in vram_array if 'ventiladores' in word), None)

            n_ventiladores = words[-1]
        
    data_str = f"{base_url+url},{model},{price},{vram_size},{vram_type},{hdmi},{dp},{consume}"
    print(data_str)
    data_lines.append(data_str)

with open('results/data.csv', 'w+') as f:
    lines = f.readlines()
    if not len(lines):
        f.write(cols+'\n')
    for data_str in data_lines:
        f.write(data_str+'\n')
