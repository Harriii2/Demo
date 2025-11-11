import requests
from parsel import Selector

def title(response):
    for list in response.xpath('//li/article'):
         title=list.xpath('.//h3/a/text()').get()
         return title
        

def price(response):
    for list in response.xpath('//li/article'):
         price = list.xpath('.//p[@class="price_color"]/text()').get()
         return price
      
        

def check_avaiablity(response):
    for list in response.xpath('//li/article'):
        raw = list.xpath('.//p[@class="instock availability"]/text()').getall()
        clean =''.join(x.strip() for x in raw if x.strip())
        return clean


def image_url(response):
    for list in response.xpath('//li/article'):
        url = list.xpath('.//a/@href').get()
        return url


def rating(response):
    for list in response.xpath('//li/article'):
        rate = list.xpath('.//p/@class').get().split(' ')[1]
        return rate
        



for i in range(1,2):
    r=requests.get(f'https://books.toscrape.com/catalogue/page-{i}.html')

    response=Selector(r.text)

    for item in response.xpath('//li/article'):
     print(f""" 
           Title:{title(response)}
           Price:{price(response)}
           Availabilty:{check_avaiablity(response)}
           Rating:{rating(response)}
           URL:{image_url(response)}
           """)


    # title(response)
    # price(response)
    # check_avaiablity(response)

    print(f'page {i} complete')
    print(r.status_code)
