import requests
from bs4 import BeautifulSoup

url = 'https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-'

response = requests.get(url)
doc = BeautifulSoup(response.text, 'html.parser')

prices = doc.find_all(text='$')
parent = prices[0].parent
strong = parent.find('strong')

print(strong.string)
