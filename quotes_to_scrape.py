import json
import requests
from parsel import Selector
data = []

for i in range(1000):
    r = requests.get(f'http://quotes.toscrape.com/page/{i}/')
    response = Selector(r.text)

     
    for list in response.xpath('//div[@class="quote"]'):
        quote = list.xpath('.//span[@class="text"]/text()').get()
        author = list.xpath('.//span/small[@class="author"]/text()').get()
        tags = list.xpath('.//div/a[@class="tag"]/text()').getall()
        author_details_link = list.xpath('.//span/a/@href').get()

        baseurl = 'https://quotes.toscrape.com'
        url = baseurl + author_details_link
        
        dic ={
            'Quote': quote,
            'Author': author,
            'Author Details Link': url,
            'Tags': tags
        }

        data.append(dic)

        with open('quotes_to_scrape.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    next_page = response.xpath('//nav/ul/li[@class="next"]/a/text()').get()
    if (next_page == "Next "):
        print(f'page {i+1}')
        print(r.status_code)
        continue
    else:
        break
