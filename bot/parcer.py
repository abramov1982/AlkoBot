import requests
from bs4 import BeautifulSoup


def rzhunemogu_api(type):
    
    const_url = 'http://rzhunemogu.ru/Rand.aspx?CType='

    r = requests.get(const_url + str(type))

    soup = BeautifulSoup(r.text, features="lxml")
    data = soup.find('content').text
    return data



'''    
url = 'http://tostov.net/?m=theme&r=16&p='

pages = [i for i in range(1,17)]

tost_list = []

def tost_parcing():
    for i in pages:
        temp_url = url + str(i)
        r = requests.get(temp_url)
        soup = BeautifulSoup(r.text)
        tosts = soup.find_all('div', {'id': 'tostt'})
        for tost in tosts:
            print(tost)
            tost_list.append(tost.text)  
'''