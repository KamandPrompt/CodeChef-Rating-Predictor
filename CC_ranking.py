# Importing necessary modules
from urllib.request import Request, urlopen 
import urllib,json                            
import pandas as pd                           

ContestID = "JUNE19A"

# get the max page_number 
path1 = 'https://www.codechef.com/api/rankings/'+ContestID+'&itemsPerPage=100'
req1 = Request(path1 , headers = {'User-Agent':'Mozilla/5.0'})
webpage1 = urlopen(req1)
obj1 = json.load(webpage1)
last_pagen = obj1['availablePages']

# Declaring necessary variables
pages = [str(i) for i in range(1,last_pagen+1)]


# declaring the lists to store data in
rank = []
userHandle = []
name = []


for page in pages:
    # make a request
    path = 'https://www.codechef.com/api/rankings/'+ContestID+'?sortBy=score&order=desc&page='+page+'&itemsPerPage=100'
    req = Request(path , headers = {'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(req)
    
    # Parse json data
    obj = json.load(webpage)
    i = obj['list']

    # Extracting data
    for j in range(len(i)):
        rank.append(i[j]['rank'])
        userHandle.append(i[j]['user_handle'])
        name.append(i[j]['name'])

# creating a Dataframe
df = pd.DataFrame({'user_handle':userHandle,'name':name},index = rank).sort_index()

# Saving into a csv format
df.to_csv('ContestRanking.csv')  
