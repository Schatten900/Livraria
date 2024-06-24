import requests
import os
from dotenv import load_dotenv

dotenv_path='.env'
load_dotenv(dotenv_path=dotenv_path)

class Book():
    def __init__(self):
        self.titulo = ''
        self.autor = ''
        self.descricao = ''
        self.price = 0
        self.isbn = ""

    def getISBN(self,titulo,autor):
        url = os.getenv('API_URL')
        params = {'q': titulo, 'key': os.getenv('API_KEY')}
        response = requests.get(url, params = params)

        if (not response.status_code == 200):  
            raise ValueError("Error to connect")

        data = response.json()
        if 'items' in data:
            for item in data['items']:
                volumeInfo = item.get('volumeInfo')
                title = volumeInfo.get('title')
                author = volumeInfo.get('authors',[])
                if titulo.lower() == title.lower() and autor.lower() in [a.lower() for a in author]:
                    industryIdentifiers = item.get('industyIdentifiers')
                    for elem in industryIdentifiers:
                        ISBN = elem.get('identifier')
                        return ISBN
        else:      
            raise ValueError("Error to connect")
    
    def setAuthor(self,autor):
        self.autor = autor

    def setPrice(self,price):
        self.price = price

    def setTitle(self,title):
        self.titulo = title 

    def setDescription(self,description):
        self.descricao = description

    def setISBN(self,ISBN):
        self.isbn = ISBN

    def getTitle(self):
        return self.titulo
    
    def getAuthor(self):
        return self.autor
    
    def getQuantidade(self):
        return self.autor
    
    def getPrice(self):
        return self.price


livro = Book() 
livro.getISBN('harry potter','J.K. Rowling')