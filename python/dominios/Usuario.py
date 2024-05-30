import re 
from abc import ABC, abstractmethod


class dominio(ABC):
    def __init__(self):
        self.valor = None

    @abstractmethod
    def validar(self,valor):
        pass

    def set(self,valor):
        self.validar(valor)
        self.valor = valor

    def get(self):
        return self.valor
    
class Nome(dominio):
    def validar(self,nome):
        HasSecondName = False
        SecondName = ""
        FirstName = ""

        for char in nome:
            if char == ' ':
                HasSecondName = True
                continue

            if (HasSecondName):
                SecondName += char
            else:
                FirstName += char
        
        for char in FirstName:
            if char.isdigit() or (not char.isalpha()) or 3 > len(FirstName) or len(FirstName) > 10 or FirstName[0].islower():
                raise ValueError("Invalid Name")
            
        for char in SecondName:
            if char.isdigit() or (not char.isalpha()) or 3 > len(SecondName) or len(SecondName)> 10 or SecondName[0].islower():
                raise ValueError("Invalid Name")
            
class Senha(dominio):
    def validar(self,senha):
        if (len(senha) != 6):
            raise ValueError("Invalid Password")
        self.checkUnique(senha)
        self.checkIncreasing(senha)
        self.checkDecreasing(senha)


    def checkUnique(self,senha):
        dic = {}
        for digit in senha:
            if digit not in dic:
                dic[digit] = 1
            else:
                dic[digit] += 1

        for digit in senha:
            if dic[digit] > 1:
                raise ValueError("Invalid Password")
            
    def checkIncreasing(self,senha):
        cont = 0
        for i in range(len(senha)-1):

            if (not senha[i].isdigit()):
                raise ValueError("Invalid Password")
            
            if int(senha[i+1]) == int(senha[i]) + 1:
                cont +=1
            else:
                cont = 0

            if cont > 3:
                raise ValueError("Invalid Password")
            
    def checkDecreasing(self,senha):
        cont = 0
        atual = int(senha[0])
        for i in range(len(senha)-1):

            if (not senha[i].isdigit()):
                raise ValueError("Invalid Password")
            
            if atual-1 == int(senha[i+1]):
                cont +=1
                atual = int(senha[i+1])
            else:
                cont = 0

            if cont > 3:
                raise ValueError("Invalid password")
            
            i-=1

class Email(dominio):
    def validar(self,email):
        patern = r'^[a-zA-Z0-9._#]+@[a-zA-Z0-9._]+\.[a-zA-Z\.a-zA-Z]{2,}$'
        validEmail = re.match(patern,email)
        if (not validEmail):
            raise ValueError("Invalid E-mail")
      
class User(dominio):
    def __init__(self):
        self.name = Nome()
        self.email = Email()
        self.password = Senha()

    def setUser(self,usuario,email,senha):
        self.name.set(usuario)
        self.email.set(email)
        self.password.set(senha)

    def getName(self):
        return self.name.get()
    
    def getEmail(self):
        return self.email.get()
    
    def getPassword(self):
        return self.password.get()