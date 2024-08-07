import requests
import os
from dotenv import load_dotenv

dotenv_path='.env'
load_dotenv(dotenv_path=dotenv_path)

class Book():
    def __init__(self):
        self.isbn = ""
        self.titulo = ""
        self.autor = ""
        self.descricao = ""

    def setLivro(self,titulo,autor):
        url = os.getenv('API_URL')
        params = {'q': f'intitle:{titulo}+inauthor:{autor}', 'key': os.getenv('API_KEY')}
        response = requests.get(url,params = params)

        if (not response.status_code == 200):
            raise ValueError("Error to connect: status code{}".format(response.status_code))
        
        data = response.json()
        if 'items' in data:
            for item in data['items']:
                volumeInfo = item.get('volumeInfo',{})
                self.titulo = volumeInfo.get('title')
                self.descricao = volumeInfo.get('description',"")
                autores = volumeInfo.get('authors',[])
                industryIdentifiers = volumeInfo.get('industryIdentifiers',[])
                for elem in industryIdentifiers:
                    if elem.get('type') in ['ISBN_13']:
                        self.isbn =  elem.get('identifier')
                        break
                    if elem.get('type') in ['ISBN_10']:
                        self.isbn = elem.get('identifier')
                        break
                for elem in autores:
                    self.autor = elem
                    break

                if (self.getAuthor() and self.getISBN() and self.getTitle and self.getDescription()):
                    return
    
    def setAuthor(self,autor):
        self.autor = autor

    def setTitle(self,title):
        self.titulo = title 

    def getISBN(self):
        return self.isbn

    def getTitle(self):
        return self.titulo
    
    def getAuthor(self):
        return self.autor
    
    def getDescription(self):
        return self.descricao
    