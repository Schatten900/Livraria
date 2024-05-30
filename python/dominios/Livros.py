import requests
import os
from dotenv import load_dotenv

load_dotenv()

class Book():
    def __init__(self):
        self.titulo = ''
        self.autor = ''
        self.descricao = ''
        self.quantidade = 0
        self.price = 0
        self.tag = []

    def searchbook(self,titulo,autor):
        url = os.getenv('API_URL')
        params = {'q': titulo, 'key': os.getenv('API_KEY')}
        response = requests.get(url, params = params)

        if (not response.status_code == 200):  
            raise ValueError("Error to connect")
        #cada livro tem uma chave VolumeInfo que contem titulo nome e tal
        data = response.json()
        #print(data)
        if 'items' in data:
            for item in data['items']:
                volumeInfo = item.get('volumeInfo')
                title = volumeInfo.get('title')
                author = volumeInfo.get('authors',[])
                if titulo.lower() == title.lower() and autor.lower() in [a.lower() for a in author]:
                    return
                
        raise ValueError("Error to connect")
    
    def setAuthor(self,autor):
        self.autor = autor

    def setPrice(self,price):
        self.price = price

    def setTitle(self,title):
        self.titulo = title 

    def setDescription(self,description):
        self.descricao = description

    def setTag(self,tag):
        self.tag.append(tag)

    def getTitle(self):
        return self.titulo
    
    def getAuthor(self):
        return self.autor
    
    def getQuantidade(self):
        return self.autor
    
    def getPrice(self):
        return self.price
    
    def getTag(self):
        return self.tag
