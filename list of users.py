import urllib.request
import json
import pandas as pd


f=open(r"E:\CC rank predictor\New Text Document.txt", "w",encoding="utf-8")
a1="https://www.codechef.com/api/ratings/all?page="
b1="&sortBy=rating&order=desc&itemsPerPage=100"
flag=1
t=1

#making of headers
html_file1=urllib.request.Request("https://www.codechef.com/api/ratings/all?page=1&sortBy=rating&order=desc&itemsPerPage=100", headers={"User-Agent" :"Mozilla /5.0"})
with urllib.request.urlopen(html_file1) as url1:
    data2 = json.loads(url1.read().decode())
#    print(data1)
data1=data2["list"]
attributes=list(data1[0].keys())
attributes.pop()
headers=""
for i in range(len(attributes)):
    
    headers=headers+attributes[i]+","
f.write(headers+"\n")




err=0


while(t<data2["availablePages"]):
    try:
        html_file=urllib.request.Request(a1+str(t)+b1, headers={"User-Agent" :"Mozilla /5.0"})
        with urllib.request.urlopen(html_file) as url:
            data = json.loads(url.read().decode())
    #        print(data)
        data=data["list"]
        attributes=list(data[0].keys())
        attributes.pop()
        headers=""
        
        for i in range(len(data)):
            a=data[i]
            tempstr=""
            for att in attributes:
                tempstr=tempstr+(str(a[att])).replace(","," ")+","
#            print(tempstr+"\n")
            f.write(tempstr+"\n")
        t=t+1
    except:
        err=err+1
        
    
