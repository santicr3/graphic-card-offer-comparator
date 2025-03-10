from requests_html import HTMLSession
import re
import utils

def main():
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

    urls = []
    for i in range(5):
        urls.extend(getAllLiks(url+f'?pagina={i}', 'product-link'))

    # Get data of each product

    session = HTMLSession()
    data_lines = []
    cols = "url,Modelo,Precio,VRAM,Tipo VRAM,HDMI,DisplayPort,Energia"
    for url in urls:
        print(base_url+url)
        model = ''
        price = ''
        vram_size = ''
        vram_type = ''
        hdmi = ''
        dp = ''
        consume = ''

        r = session.get(base_url + url)
        r.status_code
        
        model = r.html.find("h1.text-2xl", first=True).text
        if(utils.exclude(model)):
            print('Not a graphic card... skiping')
            continue  

        price = r.html.find("span.product_price", first=True).text.replace('.','')
        price_dec = r.html.find("span.dec_price", first=True).text
        
        price = price+price_dec
        attributes = r.html.find("li")

        for attribute in attributes:
            if 'DDR' in attribute.text and len(attribute.text) < 30:
                vram = attribute.text
                vram_array = vram.split(' ')
                vram_type = next((word for word in vram_array if 'DDR' in word), '')
                vram_type = utils.vram_type_clean(vram_type)
            if 'GB' in attribute.text and len(attribute.text) < 30:
                match = re.search(r'(?<!\S)(\d+)\s?GB(?!\S)', attribute.text)
                vram_size = match.group(1) if match else '' 

            if any(port in attribute.text for port in ['DisplayPort', 'DP', 'HDMI']):
                hdmi, dp = utils.ports_clean(attribute.text)
            
            if re.search(r'\d+\s?W', attribute.text, re.IGNORECASE) and len(attribute.text) and consume == '':
                match = re.search(r'\d+\s?W', attribute.text, re.IGNORECASE)
                consume = match.group()
                consume = re.search(r'\d+', consume, re.IGNORECASE).group() if consume else ''

        if not vram_size:
            match = re.search(r'(?<!\S)(\d+)\s?GB(?!\S)', model)
            vram_size = match.group(1) if match else '' 
        data_str = f"{base_url+url},{model},{price},{vram_size},{vram_type},{hdmi},{dp},{consume}"
        data_lines.append(data_str)

    utils.add_to_file(data_lines, cols)
