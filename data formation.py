from urllib.request import Request, urlopen 
import urllib,json                            
import pandas as pd 
from bs4 import BeautifulSoup
import requests

ContestID="JUNE19A"
#def scrapeContestRanks(ContestID):
##    ContestID = "JUNE19A"
#    
#    # get the max page_number 
#    path1 = 'https://www.codechef.com/api/rankings/'+ContestID+'&itemsPerPage=100'
#    req1 = Request(path1 , headers = {'User-Agent':'Mozilla/5.0'})
#    webpage1 = urlopen(req1)
#    obj1 = json.load(webpage1)
#    last_pagen = obj1['availablePages']
#    
#    # Declaring necessary variables
#    pages = [str(i) for i in range(1,last_pagen+1)]
#    
#    
#    # declaring the lists to store data in
#    rank = []
#    userHandle = []
#    name = []
#    
#    
#    for page in pages:
#        # make a request
#        path = 'https://www.codechef.com/api/rankings/'+ContestID+'?sortBy=score&order=desc&page='+page+'&itemsPerPage=100'
#        req = Request(path , headers = {'User-Agent':'Mozilla/5.0'})
#        webpage = urlopen(req)
#    
#        # Parse json data
#        obj = json.load(webpage)
#        i = obj['list']
#    
#        # Extracting data
#        for j in range(len(i)):
#            rank.append(i[j]['rank'])
#            userHandle.append(i[j]['user_handle'])
#            name.append(i[j]['name'])
#    
#    # creating a Dataframe
#    df = pd.DataFrame({'user_handle':userHandle,'name':name},index = rank).sort_index()
#    
#    return df



    

#function parameter being contest ID
#df = scrapeContestRanks("JUNE19A")
#df.to_csv('ContestRanking.csv')

ContestData = pd.read_csv("file:///E:/CC rank predictor/ContestRanking.csv") #data of particular contest

dataOverall = pd.read_csv("file:///E:/CC rank predictor/datainCSV.csv") #data of whole ranklist on codechef
participants = ContestData["user_handle"]
#participants=participants.head()

#empty dataframe
work = pd.DataFrame(columns = ["Current_Rating","Rank_in_contest","Mean_below_ranked","Rating_change"])

#function to get rating graph
def get_rating_graphs(username):
    page=requests.get("https://www.codechef.com/users/"+username,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(page.content, 'html.parser')
    x=str(soup.select('script[type="text/javascript"]')[29]).split(';')[9][19:].strip()
    Code=[]
    Year=[]
    Month=[]
    Day=[]
    Reason=[]
    Penalised_In=[]
    Rating=[]
    Rank=[]
    Name=[]
    End_Date=[]
    y=x[1:-2].split('},')
    null='None'
    for i in range(len(y)):
        y[i]=y[i]+'}'
    for i in range(len(y)):
        Code.append(eval(y[i])['code'])
        Year.append(eval(y[i])['getyear'])
        Month.append(eval(y[i])['getmonth'])
        Day.append(eval(y[i])['getday'])
        Reason.append(eval(y[i])['reason'])
        Penalised_In.append(eval(y[i])['penalised_in'])
        Rating.append(eval(y[i])['rating'])
        Rank.append(eval(y[i])['rank'])
        Name.append(eval(y[i])['name'])
        End_Date.append(eval(y[i])['end_date'])
    
    dict = {'Code':Code , 'Year': Year, 'Month': Month,'Day':Day,'Reason':Reason,'Penalised_In':Penalised_In,'Rating':Rating,'Rank':Rank,'Name':Name,'End_Date':End_Date}  
    
    df = pd.DataFrame(dict) 
    return df

#Function to get present rating(parameter being userhandle)
def Present_rating(username):
    row = dataOverall[dataOverall["username"]==username]
    rat = row["rating"]
    rat = list(rat)[0]
    return rat

l1=[]
l2=[]
l3=[]
l4=[]


for i in range(len(participants)):
    username = participants[i]
#    dataOfthat = dataOverall[dataOverall["username"]==username]
#    Total_rat_data = dataOverall["Rating"]
    rating = Present_rating(username)
    tempSum = 0
    try:
        for j in range(i+1,len(participants)):
            tempSum = tempSum + Present_rating(username)
    except:
        pass
    l1.append(rating)
    l2.append(i+1)
    try:
        nos = len(participants)-i-1
        l3.append(tempSum/nos)
    except:
        l3.append(0)
    rating_history = get_rating_graphs(username)
    rating_after = rating_history[rating_history["Code"]==ContestID]["Rating"]
    index1 = (rating_history.loc[rating_history["Code"]==ContestID].index)[0]
    rating_after = list(rating_after)
    rating_after = int(rating_after[0])
    try:
        rating_before = rating_history["Rating"] 
        rating_before = int(rating_before[index1-1])
    except:
        rating_before=rating_after
    change = rating_after - rating_before
    l4.append(change)
    
#  Feeding the empty dataframe    
work.Current_Rating = l1
work.Rank_in_contest = l2
work.Mean_below_ranked = l3
work.Rating_change = l4
print(work)
    
    
    
    
