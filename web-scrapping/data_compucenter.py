from requests_html import HTMLSession
import re
import utils

base_url = "https://compucenter.es"
url = base_url + "/categoria.php?id=10850"

def getAllLiks(url, product_class):
    # Graphic cards URL

    session = HTMLSession()
    r = session.get(url)
    r.status_code
    
    # Get all the URL's
    container_elements = r.html.find("div."+product_class)
    urls_elements = container_elements.find('a')

    urls = []
    for url_element in urls_elements:
        urls.append(url_element.attrs["href"])
    
    return urls

urls = []
for i in range(5):
    urls.extend(getAllLiks(url+f'?pagina={i}', 'list-item'))

# Get data of each product

session = HTMLSession()
data_lines = []
cols = "url,modelo,precio,vram,tipo-vram,hdmi,dp,dimensiones,consumo"
for url in urls:
    print(url)
    r = session.get(base_url + url)
    r.status_code
    
    model = r.html.find("h1.text-2xl", first=True).text
    
    price = r.html.find("span.product_price", first=True).text.replace('.','')
    price_dec = r.html.find("span.dec_price", first=True).text
    
    price = price+price_dec
    attributes = r.html.find("li")

    for attribute in attributes:
        if 'DDR' in attribute.text and len(attribute.text) < 30:
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
    data_lines.append(data_str)

with open('results/data.csv', 'w+') as f:
    lines = f.readlines()
    if not len(lines):
        f.write(cols+'\n')
    for data_str in data_lines:
 
