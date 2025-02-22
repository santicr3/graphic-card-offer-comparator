from requests_html import HTMLSession

base_url = "https://www.coolmod.com"
url = base_url + "/tarjetas-graficas/"

def getAllLiks(url, product_class):
    # Graphic cards URL

    session = HTMLSession()
    r = session.get(url)
    r.status_code
    
    # Get all the URL's
    urls_elements = r.html.find("a."+product_class)
    urls = []
    for url_element in urls_elements:
        urls.append(url_element.attrs["href"])
    
    return urls

urls = getAllLiks(url, 'product-link')


# Get data of each product
#


session = HTMLSession()
data_lines = []
cols = "modelo,precio,vram,tipo-vram,puertos,dimensiones,consumo"
for url in urls:
    print(base_url+url)
    r = session.get(base_url + url)
    r.status_code
    
    model = r.html.find("h1.text-2xl", first=True).text
    
    price = r.html.find("span.product_price", first=True).text
    price_dec = r.html.find("span.dec_price", first=True).text
    
    price = price + "," + price_dec
    
    attributes = r.html.find("li")
    for attribute in attributes:
        if 'DDR' in attribute.text and len(attribute.text) < 30:
            vram = attribute.text
            vram_array = vram.split(' ')
            vram_type = next((word for word in vram_array if 'DDR' in word), None)
            vram_size = next((word for word in vram_array if 'GB' in word), None)
    
        if any(port in attribute.text for port in ['HDMI', 'DisplayPort', 'DP', 'VGA', 'DVI'])  :
            ports = attribute.text
    
        if 'PSU' in attribute.text or any(port in attribute.text for port in ['watts', 'Watts']):
            consume = attribute.text
    
        if any(port in attribute.text for port in ['mm', 'milimetros', 'cm', 'centimetros']):
            size = attribute.text
    
        if 'ventiladores' in attribute.text:
            print(attribute.text)
            words = attribute.text.split(' ')
            index_ventiladores = words.index('ventiladores')
            print(index_ventiladores)
            n_ventiladores = words[-1]
            print(n_ventiladores)
    data_str = f"{model},{price},{vram_size},{vram_type},{ports},{consume},{size}"
    data_lines.append(data_str)

with open('data.csv', 'w+') as f:
    lines = f.readlines()
    if not len(lines):
        f.write(cols+'\n')
    for data_str in data_lines:
        f.write(data_str+'\n')
# product_link_class = "product-link"
