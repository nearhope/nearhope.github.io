from bs4 import BeautifulSoup
from urllib import request

# url = "https://stackoverflow.com/questions/tagged/python"
#
# print(url)
#
# html = request.urlopen(url).read()
# print()
#
# soup = BeautifulSoup(html, 'lxml')
# # parses the link
# htmlLinks=(soup.select('h3 a.question-hyperlink'))[0:10]
# urls=[]
# #makes it a url and stores in a list
# for link in htmlLinks:
#     url="https://stackoverflow.com" + link['href']
#     urls.append(url)
# #   prints list of urls
# for link in urls:
#     print(link)
#
# corpusTexts = []
# for url in urls:
#     print(url)
#     html = request.urlopen(url).read()
#     soup = BeautifulSoup(html, "lxml")
#     text = soup.text#.replace('\n', '')
#     corpusTexts.append(text)
#
#     print(corpusTexts)


#.....................
#try scraping NYTimes arts page
#

url = "https://www.nytimes.com/section/arts/design?action=click&contentCollection=arts&region=navbar&module=collectionsnav&pagetype=sectionfront&pgtype=sectionfront"
print(url)

html = request.urlopen(url).read()
print()

soup = BeautifulSoup(html, 'lxml')
# parses the link
htmlLinks=(soup.select('div a.story-link'))[0:10]
urls=[]
#makes it a url and stores in a list
for link in htmlLinks:
    url=link['href']
    urls.append(url)
#   prints list of urls
#for link in urls:
    #print(link)
headlines=[]
for item in soup.find_all('h2')[6:17]:
    headlines.append(item.text.replace('\n', ''))
    # print('=======')
    # print(item.text.replace('\n', ''))

for line in headlines:
    print(line)
    print("=======")

#
# corpusTexts = []
# for url in urls:
#     # print(url)
#     html = request.urlopen(url).read()
#     soup = BeautifulSoup(html, "lxml")
#     textBodies = soup.find_all('div', class_='css-18sbwfn')
#     # headlines = soup.find_all(div', class_="     ")
#     for textBody in textBodies:
#         corpusTexts.append(textBody.text)

    # print(htmlLinks)
    # print(corpusTexts)


# articles={headlines:corpusTexts}
#
# for header, body in articles.items():
#     print(header)
