from bs4 import BeautifulSoup
import requests

keywords = input('Enter job title: ').replace(' ', '%20').lower()
url = f'https://www.linkedin.com/jobs/search?keywords={keywords}&location=&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'

response = requests.get(url).text
doc = BeautifulSoup(response, 'html.parser')

job_list = doc.find(class_='jobs-search__results-list')

print(len(job_list))
