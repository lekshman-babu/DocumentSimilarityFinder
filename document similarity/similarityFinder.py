import json
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import re
js=open("extracted.json","r")
extracted=json.load(js)

def punct(para):
    punct='''±()=<>:.,/-\$+-_;'[]%^&*@"'''
    for i in punct:
        para=para.replace(i,' ')
    para=re.sub(r" +"," ",para)
    return para

def similarityFinder(first,second):
    abstractList=[first,second]
    tfid=TfidfVectorizer()
    matrix=tfid.fit_transform(abstractList)
    documentSimilarity=cosine_similarity(matrix,matrix)
    print(documentSimilarity)
    return round(documentSimilarity[1,0]*100,1)

def abstract(title):
    return punct(extracted[title]['abstract'])

def getTitles():
    titles=[]
    for i in extracted:
        titles.append(i)
    return titles

def getTitleFromNum(titleNum):
    for i in extracted:
        if extracted[i]['id']==titleNum:
            return i    

if __name__=="__main__":
    title1=input("enter first title: ")
    title2=input("enter second title: ")
    first=abstract(title1)
    second=abstract(title2)
    documentSimilarity=similarityFinder(first,second)
    print(f'document similarity = {documentSimilarity}%')
    js.close()
