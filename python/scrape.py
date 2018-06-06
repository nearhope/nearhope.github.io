

from bs4 import BeautifulSoup
from urllib import request

url = "https://github.com/humanitiesprogramming/scraping-corpus"

print(url + "/subdomain")

html = request.urlopen(url).read()
print(html[0:2000])



soup = BeautifulSoup(html, 'lxml')



print(soup.find_all('a')[0:10])
#
#
#
print(soup.text[0:2000])
#
#
#
print(soup.text.replace('\n', ' ')[0:1000])
#
#print(soup.find_all('a').text)

print(soup.find_all('a')[0:10])

print(type(soup.find_all('a')).__name__)
