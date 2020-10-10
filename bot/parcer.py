import requests
from bs4 import BeautifulSoup


def rzhunemogu_api(slug): 
    const_url = 'http://rzhunemogu.ru/Rand.aspx?CType='
    try:
        r = requests.get(const_url + str(slug))
        soup = BeautifulSoup(r.text, features="lxml")
        data = soup.find('content').text
        if r.status_code != 200:
            data = 'API недоступно'
            raise Exception(data)
    except Exception:
        return 'API недоступно'
    return data


def ibash_api():
    url = 'http://ibash.org.ru/random.php'
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, features="lxml")
        data = soup.find('div', {'class': 'quotbody'})
        data = str(data).replace('<br/>', '\n')[22:].split('</div>')[0]
        if r.status_code != 200:
            data = 'API недоступно'
            raise Exception(data)
    except Exception:
        return 'API недоступно'
    return data


def bash_api():
    url = 'https://bash.im/random'
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, features="lxml")
        data = soup.find('div', {'class': 'quote__body'})
        data = str(data).replace('<br/>', '\n')[32:].split('</div>')[0]
        if r.status_code != 200:
            data = 'API недоступно'
            raise Exception(data)
    except Exception:
        return 'API недоступно'
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