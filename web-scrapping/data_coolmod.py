from requests_html import HTMLSession

# Graphic cards URL
base_url = "https://www.coolmod.com"
url = base_url + "/tarjetas-graficas/"
session = HTMLSession()
r = session.get(url)
r.status_code

# Get all the URL's
urls_elements = r.html.find("a.product-link")
urls = []
for url_element in urls_elements:
    urls.append(url_element.attrs["href"])

# Get data of each product
test_url = urls[0]
r = session.get(base_url + test_url)
r.status_code

title = r.html.find("h1.text-2xl", first=True).text
print(title)

price = r.html.find("span.product_price", first=True).text
price_dec = r.html.find("span.dec_price", first=True).text

print(price + "," + price_dec)

attributes = r.html.find("p")
for attribute in attributes:
    print(attribute)
# product_link_class = "product-link"
