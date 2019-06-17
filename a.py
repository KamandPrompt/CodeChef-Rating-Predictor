from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
html_file=Request("https://www.codechef.com/ratings/all", headers={"User-Agent" :"Mozilla /5.0"})
page=urlopen(html_file)
page_soup=soup(page,"html.parser")

a=page_soup.findAll('tr')
print(page_soup)
for rows in a:
    for col in rows.findAll('td'):
        print(col.text)
    
