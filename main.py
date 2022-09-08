import requests

URL = 'https://www.linkedin.com/jobs/search/'
page = requests.get(URL)

print(page.text)
