import json
import math
j=open("extracted.json","r")
extracted=json.load(j)


def punct(para):
    punct='''±()=<>:.,/-\$+-_;'[]%^&*@"'''
    for i in punct:
        para=para.replace(i,' ')
    para=para.replace('  ',' ')
    return para.lower()

def unique_count(text):
    text_dict={}
    for i in text.split(" "):
        if i in text_dict:
            text_dict[i]+=1
        else:
            text_dict[i]=1
    return text_dict

def dot_prod(td1,td2):
    sum=0
    for i in td1:
        if i in td2:
            sum+=(td1[i]*td2[i])
    return sum

def similarity_finder(text_dict1,text_dict2):
    numarator=dot_prod(text_dict1,text_dict2)
    denominator=math.sqrt(dot_prod(text_dict1,text_dict1)*dot_prod(text_dict2,text_dict2))
    return (numarator/denominator)*100

    
title1=input("enter first title:")
title2=input("enter second title:")
first=punct(extracted[title1]['abstract'])
second=punct(extracted[title2]['abstract'])
document_similarity=similarity_finder(unique_count(first),unique_count(second))
print(f'document similarity = {round(document_similarity,1)}%')