
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests
import pandas as pd

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
    df.to_csv(username+'.csv') 
get_rating_graphs('karansdoshi')
get_rating_graphs('physah86')
