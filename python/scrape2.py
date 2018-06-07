from bs4 import BeautifulSoup
from urllib import request

url = "http://www.sothebys.com/en/auctions/results.html"
# subdomain=""
# newUrl = url + subdomain
# print(newUrl)

html = request.urlopen(url).read()
print()
soup = BeautifulSoup(html, 'lxml')

for item in soup.find_all('a')[0:10]:
    print('=======')
    print(item.text.replace('\n', ''))
