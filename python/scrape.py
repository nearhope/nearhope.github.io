from bs4 import BeautifulSoup
from urllib import request
import nltk             #imports python package called nltk
url = "https://github.com/humanitiesprogramming/scraping-corpus"
#print(url)
subdomain="/blob/master/0.txt"
newUrl = url + subdomain
print(newUrl)

html = request.urlopen(url).read()
print()
#print(html[0:2000])
soup = BeautifulSoup(html, 'lxml')
#print(soup.find_all('a')[0:10])
#print(soup.text[0:2000])
#print(soup.text.replace('\n', ' ')[0:1000])
#print(soup.find_all('a').text) #dont' do this
#print(soup.find_all('a')[0:10])
#print(type(soup.find_all('a')).__name__)
##print(soup.find_all('a')[0].text)
print(len(soup.find_all('a')))

# for item in soup.find_all('a')[0:10]:
#     print('=======')
#     print(item.text.replace('\n', ''))

#for link in soup.select("td.content a"):
#    print(link.text)

# links_html = soup.select('td.content a')
# urls = []
# for link in links_html:
#     url = link['href']
#     urls.append(url)
# print(urls)

links_html = soup.select('td.content a')
urls = []
for link in links_html:
    url = link['href'].replace('blob/', '')
    urls.append("https://raw.githubusercontent.com" + url)
# print(urls)

corpusTexts = []
for url in urls:
    print(url)
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    text = soup.text.replace('\n', '')
    corpusTexts.append(text)

#for text in corpusTexts:
str=''.join(corpusTexts)

with open("doyle.txt", "w") as file:
    file.write(str)





#print(corpus_texts)
