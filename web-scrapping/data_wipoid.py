from requests_html import HTMLSession
import re
import utils


def main():
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
    cols = "url,Modelo,Precio,VRAM,Tipo VRAM,HDMI,DisplayPort,Energia"
    for url in urls:
        model = ''
        price = ''
        vram_size = ''
        vram_type = ''
        hdmi = ''
        dp = ''
        consume = ''
        
        r = session.get(url)
        r.status_code
        
        model = r.html.find("h1.product-detail-name", first=True).text
        if(utils.exclude(model)):
            print('Not a graphic card... skiping')
            continue  

        price = r.html.find("span.current-price-value", first=True).text.replace(',','').replace('.','').replace('€','')
        
        attributes = r.html.find("p")

        for attribute in attributes:
            if 'DDR' in attribute.text and len(attribute.text) and vram_type == '':
                vram = attribute.text
                vram_array = vram.split(' ')
                vram_type = next((word for word in vram_array if 'DDR' in word), '')
                vram_type = utils.vram_type_clean(vram_type)
            if 'GB' in attribute.text and len(attribute.text) and vram_size == '':
                match = re.search(r'(?<!\S)(\d+)\s?GB(?!\S)', attribute.text, re.IGNORECASE)
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
        data_str = f"{url},{model},{price},{vram_size},{vram_type},{hdmi},{dp},{consume}"
        print(data_str)
        data_lines.append(data_str)
        

    utils.add_to_file(data_lines, cols)
