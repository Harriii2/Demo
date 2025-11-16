import json
import requests
from parsel import Selector
data =[]

for i in range(1000):
    r=requests.get(f'https://sandbox.oxylabs.io/products?page={i}')

    response=Selector(r.text)

    html_products = response.xpath('.//div[@class="product-card css-e8at8d eag3qlw10"]')

    json_str= response.xpath('.//script[@id="__NEXT_DATA__"]/text()').get()
    json_data = json.loads(json_str)
    json_products = json_data.get('props').get('pageProps').get('products')

    # print(json.dumps(json_data, indent=2))


    for html_item, json_item in zip(html_products, json_products):
        title=json_item.get('game_name')
        price = html_item.xpath('.//div[@class="price-wrapper css-li4v8k eag3qlw4"]/text()').get()
        developer = json_item.get('developer')
        category = json_item.get('genre')

        if json_item.get('inStock'):
            stock = "In stock"
        else:
            stock = "Out of stock"
        
        game_type = json_item.get('type')
        game_type = game_type.capitalize()
        description = json_item.get('description')
        rating = json_item.get('rating')
        game_url = json_item.get('url')

        dictionary ={
            'Title': title,
            'Price': price,
            'Stock': stock,
            'Type': game_type,
            'Rating': rating,
            'Developer': developer,
            'Category': category,
            'Game_URL': game_url,
            'Description': description
        }
        data.append(dictionary)

        with open('sandbox_oxylabs_io.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    next_page = response.xpath('//ul/li[@class ="next"]/a/text()').get()
    if (next_page == "Forward"):
        print(f'page {i+1}')
        print(r.status_code)
        continue
    else:
        break