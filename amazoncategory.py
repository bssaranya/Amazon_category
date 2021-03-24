from bs4 import BeautifulSoup
import requests
import re
import json

r = requests.get('https://www.amazon.in/gp/site-directory?ref=nav_em_ajax_fail')

src=r.text
soup = BeautifulSoup(src,'lxml')

main_categories = {}
products = []
mystr = 'https://www.amazon.in'
maindiv = soup.select('.popover-grouping')
headlist=[]
diclist = []

for div in maindiv:
    for x in div.select('.popover-category-name'):
        head = x.text,'\n'
        headlist.append(head)
       

        for x in div.select('.nav_a'):
            productlink = x.attrs['href']
            products.append(productlink)
     
    main_categories={
        'head':head,
        'productlink':products
    }
    diclist.append(main_categories)
    print(main_categories)


json_text = json.dumps(diclist,indent=4)
with open('amazoncategory.json', 'w') as json_file:
    json_file.write(json_text)