import json
import requests
from parsel import Selector

data  = []

for i in range(1,51):
    r=requests.get(f'https://books.toscrape.com/catalogue/page-{i}.html')

    response=Selector(r.text)
    
    for list in response.xpath('//li/article'):
        title=list.xpath('.//h3/a/text()').get()
        price = list.xpath('.//p[@class="price_color"]/text()').get()
        stock = list.xpath('.//p[@class="instock availability"]/text()').getall()[1].strip()
        rating = list.xpath('.//p/@class').get().split()[1]
        image_url = list.xpath('.//img/@src').get()
        image_url = image_url.replace('../', '')

        baseurl = 'https://books.toscrape.com/'
        url = baseurl + image_url

        dic ={
            'Title': title,
            'Price': price,
            'Stock': stock,
            'Rating': rating,
            'Image_url': url
        }
        data.append(dic)

        with open('books_to_scrape.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    print(r.status_code)