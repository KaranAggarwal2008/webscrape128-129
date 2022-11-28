from bs4 import BeautifulSoup
import requests
import pandas as pd
brown_dwarfs_url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page = requests.get(brown_dwarfs_url)
print(page)
soup = BeautifulSoup(page.text,'html.parser')
star_table = soup.find('table')
temp_list= []
table_rows = star_table[7].find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
brown_dwarfs=[]
for i in range(1,len(temp_list)):
    brown_dwarfs.append(temp_list[i])
df2 = pd.DataFrame(list(zip(brown_dwarfs)),columns=['brown_dwarfs'])
print(df2)
df2.to_csv('project128.csv')