import requests
from bs4 import BeautifulSoup

def thehinduinternational():
    url1="https://www.thehindu.com/news/international/"
    response= requests.get(url1)

    if response.status_code==200:
        soup = BeautifulSoup(response.content, 'html.parser')

        elements= soup.find_all(class_="title")
        elements=set(elements)
        return elements

    else:
        return ["sorry! unable to fetch"]
    
def thehindunational():
    url2="https://www.thehindu.com/news/national/"
    response= requests.get(url2)

    if response.status_code==200:
        soup = BeautifulSoup(response.content, 'html.parser')

        elements= soup.find_all(class_="title")
        elements=set(elements)
        return elements

    else:
        return ["sorry! unable to fetch"]  
    
def thehindubreaking():
    url3="https://www.thehindu.com/news/"
    response= requests.get(url3)

    if response.status_code==200:
        soup = BeautifulSoup(response.content, 'html.parser')

        elements= soup.find_all(class_="title")
        elements=set(elements)
        return elements

    else:
        return ["sorry! unable to fetch"]
    
def thehindueconomy():
    url4="https://frontline.thehindu.com/economy/"
    response= requests.get(url4)
    Y=[]
    if response.status_code==200:
        soup = BeautifulSoup(response.content, 'html.parser')

        A= soup.find_all(class_="content")
        for a in A:
            b=a.find('a')
            b=b.get_text(strip=True)
            if len(b.split())>5:
                Y.append(b)
        elements=set(Y)
        return elements

    else:
        return ["sorry! unable to fetch"]  

def toidelhi():
    url5="https://timesofindia.indiatimes.com/city/delhi"
    response= requests.get(url5)

    if response.status_code==200:
        soup= BeautifulSoup(response.content, 'html.parser')

        elements=soup.find_all('figcaption')
        elements=set(elements)
        return elements

    else:
        return ["sorry! unable to fetch"] 

def toiup():
    url6="https://timesofindia.indiatimes.com/india/uttar-pradesh"
    response= requests.get(url6)

    if response.status_code==200:
        soup= BeautifulSoup(response.content, 'html.parser')
        Y=[]
        elements=soup.find_all('a')

        for el in elements:
            a=el.get('title')
            if a and len(a.split())>5:
                Y.append(a)
        elements=set(Y)
        return elements

    else:
        return ["sorry! unable to fetch"]
    
def toibusiness():
    url7="https://timesofindia.indiatimes.com/business"

    response= requests.get(url7)

    if response.status_code==200:
        soup= BeautifulSoup(response.content, 'html.parser')

        elements=soup.find_all('figcaption')
        elements=set(elements)
        return elements

    else:
        return ["sorry! unable to fetch"] 

def toisports():
    url8="https://timesofindia.indiatimes.com/sports"

    response= requests.get(url8)

    if response.status_code==200:
        soup= BeautifulSoup(response.content, 'html.parser')

        elements= soup.find_all(class_="WavNE")

        elements=set(elements)
        return elements
    else:
        return ["sorry! unable to fetch"] 
    
def tet():
    url9="https://economictimes.indiatimes.com/"
    response= requests.get(url9)
    Y={}
    if response.status_code==200:
        soup= BeautifulSoup(response.content, 'html.parser')

        elements= soup.find_all('a')
        for el in elements:
            link=el.get('href')
            el=el.get_text(strip=True)
            if len(el.split())>5:
                Y[el]=link

        return Y
    else:
        return ["sorry! unable to fetch"]

def newsapi():
    apikey = 'acd91fb26b84cda47ad78c205c6ece84';
    url10 = 'https://gnews.io/api/v4/search?q=example&lang=en&country=us&max=10&apikey=' + apikey;

    response = requests.get(url10)
    print("STATUS CODE:", response.status_code)
    print("RESPONSE TEXT:", response.text)

    response.raise_for_status() 

    data = response.json()
    return data