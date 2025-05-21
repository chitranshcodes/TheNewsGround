import requests
from bs4 import BeautifulSoup

def thehinduinternational():
    url="https://www.thehindu.com/news/international/"
    response= requests.get(url)

    if response.status_code==200:
        soup = BeautifulSoup(response.content, 'html.parser')

        elements= soup.find_all(class_="title")
        elements=set(elements)
        return elements

    else:
        return ["sorry! unable to fetch"]
    
def thehindunational():
    url="https://www.thehindu.com/news/national/"
    response= requests.get(url)

    if response.status_code==200:
        soup = BeautifulSoup(response.content, 'html.parser')

        elements= soup.find_all(class_="title")
        elements=set(elements)
        return elements

    else:
        return ["sorry! unable to fetch"]  
    
def thehindubreaking():
    url="https://www.thehindu.com/news/"
    response= requests.get(url)

    if response.status_code==200:
        soup = BeautifulSoup(response.content, 'html.parser')

        elements= soup.find_all(class_="title")
        elements=set(elements)
        return elements

    else:
        return ["sorry! unable to fetch"]
    
def thehindueconomy():
    url="https://frontline.thehindu.com/economy/"
    response= requests.get(url)
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
    url="https://timesofindia.indiatimes.com/city/delhi"
    response= requests.get(url)

    if response.status_code==200:
        soup= BeautifulSoup(response.content, 'html.parser')

        elements=soup.find_all('figcaption')
        elements=set(elements)
        return elements

    else:
        return ["sorry! unable to fetch"] 

def toiup():
    url="https://timesofindia.indiatimes.com/india/uttar-pradesh"
    response= requests.get(url)

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
    url="https://timesofindia.indiatimes.com/business"

    response= requests.get(url)

    if response.status_code==200:
        soup= BeautifulSoup(response.content, 'html.parser')

        elements=soup.find_all('figcaption')
        elements=set(elements)
        return elements

    else:
        return ["sorry! unable to fetch"] 

def toisports():
    url="https://timesofindia.indiatimes.com/sports"

    response= requests.get(url)

    if response.status_code==200:
        soup= BeautifulSoup(response.content, 'html.parser')

        elements= soup.find_all(class_="WavNE")

        elements=set(elements)
        return elements
    else:
        return ["sorry! unable to fetch"] 
    
def tet():
    url="https://economictimes.indiatimes.com/"
    response= requests.get(url)
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
