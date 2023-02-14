import json
j=open("extracted.json","r")
extracted=json.load(j)
title1=input("enter first title:")
title2=input("enter second title:")
if extracted[title1]["subject"][0]==extracted[title2]["subject"][0]:
    print("the two documents are similar")
else:
    flag=0
    for i in range(1,len(extracted[title1]["subject"])):
        if extracted[title1]["subject"][i] in extracted[title2]["subject"]:
            flag=1
    if flag==1:
        print("the documents are partially similar")
    else:
        print("the documents are unrelated")