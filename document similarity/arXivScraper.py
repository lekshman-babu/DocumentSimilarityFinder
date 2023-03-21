import requests
import bs4
import json
import re

js=open("extracted.json",'w')
linkRead=open("links.json","r")
mainLink='https://arxiv.org/'
linkDictionary=json.load(linkRead)
extracted={}
id=0

def request(link):
    res=requests.get(link)
    return bs4.BeautifulSoup(res.text,'lxml')

def contentExtractor(targetLink):
    soup=request(targetLink)
    heading=soup.select('.title.mathjax')[0]
    abs=soup.select('.abstract.mathjax')
    # subject=soup.select('.tablecell.subjects')
    title=heading.text[6:]
    abstract=abs[0].text[10:]
    abstract=abstract.replace('\n'," ")
    global id
    extracted[title]={"id":id,'abstract':abstract[2:]}
    id+=1
    print(f"{id}  {title}")

def mainPage(link,all=0):
    soup=request(link)
    totalRecords=soup.select('small')[0].text
    totalRecords=re.findall(r'\d+',totalRecords)[0]
    soup=request(link+totalRecords)
    if not all:
        noOfDoc=int(input("enter the number of documents required(total documents={0}) ".format(totalRecords)))
    else:
        noOfDoc=int(totalRecords)
    
    for j in range(noOfDoc):
        targetLink=mainLink+soup.select('.list-identifier')[j]('a')[0]['href']
        contentExtractor(targetLink)

def newPage(domain):
    soup=request(mainLink)
    main=soup.select('main')
    base=main[0].select('li')
    for i in range(2,len(base)-5):
        if domain==base[i].select('a')[0].text:
            linkDictionary[domain]=mainLink+base[i].select('a')[2]['href'].split("recent")[0]+"pastweek?show="
            linkWrite=open("links.json","w")
            json.dump(linkDictionary,linkWrite)
            linkWrite.close()
            return 0
    print("the entered domain is not present")
    return 0

for i in linkDictionary:
    print(i)
domain=input("enter a specific domain from above or enter 'all' for all the records: ")
if domain!="all":
    if domain in linkDictionary:
        mainPage(linkDictionary[domain])
    else:
        if newPage(domain)>0:
            linkDictionary=json.load(linkRead)
            mainPage(linkDictionary[domain])
else:
    for domain in linkDictionary:
        mainPage(linkDictionary[domain],1)

json.dump(extracted,js)
js.close()
linkRead.close()