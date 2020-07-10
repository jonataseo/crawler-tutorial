import requests
from bs4 import BeautifulSoup

URL = 'https://www.indeed.com.br/jobs?q=Desenvolvedor+Junior+Remoto&l=&ts=1594334334754&pts=1594307043780&rq=1&rsIdx=0'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='resultsBodyContent')
# print(results.prettify())
job_elems = results.find_all('div', class_='jobsearch-SerpJobCard')

for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    sjcl_elem = job_elem.find('span', class_='company')
    summary_elem = job_elem.find('div', class_='summary')
    if None in (summary_elem, sjcl_elem, title_elem):
        continue
    print(title_elem.text.strip())
    print(sjcl_elem.text.strip())
    print(summary_elem.text.strip())
    print("\n---------------------------------------------\n")
    #print(message_elem)
    #print(resultsTop_elem)

