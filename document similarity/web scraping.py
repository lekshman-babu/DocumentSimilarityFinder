import requests
import bs4
import json

#json file
js=open("extracted.json",'w')

#get the link
mainLink='https://arxiv.org/'
res=requests.get(mainLink)
soup=bs4.BeautifulSoup(res.text,'lxml')

#getting the links requiered
main=soup.select('main')
base=main[0].select('li')
extracted={}

#extractin all the main subjects
for i in range(2,22):
    link=mainLink+base[i].select('a')[1]['href']
    res=requests.get(link)
    soup=bs4.BeautifulSoup(res.text,'lxml')
    entries=soup.select('b')

    #extracting all the documents in the page
    for j in range(int(entries[0].text[2:])):
        targetLink=mainLink+soup.select('.list-identifier')[j]('a')[0]['href']
        fres=requests.get(targetLink)
        fsoup=bs4.BeautifulSoup(fres.text,'lxml')

        #extracting the title,abstract and subjects of the document
        heading=fsoup.select('.title.mathjax')[0]
        abs=fsoup.select('.abstract.mathjax')
        subject=fsoup.select('.tablecell.subjects')
        title=heading.text[6:]
        abstract=abs[0].text[10:]
        abstract=abstract.replace('\n'," ")

        #storing as a dictionary 
        extracted[title]={'abstract':abstract[2:],'subject':subject[0].text[1:].split(";")}
        print(title)
        if(j==1):
            break
    break

#
json.dump(extracted,js)