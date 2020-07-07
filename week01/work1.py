import requests
from bs4 import BeautifulSoup as bs
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

header = {'user-agent':user_agent}
myUrl = "https://maoyan.com/films?showType=3"
response = requests.get(myUrl,headers=header)

bs_info = bs(response.text, 'html.parser')
 

mylist=[]
for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'})[:10]:
    atag=tags.find_all('div')
    mylist.append(atag[0].find('span').text)
    mylist.append(atag[1].text.split()[1])
    mylist.append(atag[3].text.split()[1])     
import pandas as pd
movie1 = pd.DataFrame(data = mylist)

# windows需要使用gbk字符集
movie1.to_csv('./movie1.csv', encoding='utf8', index=False, header=False)