import bcrypt
import random
from servicos.connection import executeQuery,Error
from dominios.Usuario import User,Nome,Senha,Email


class Usuario():
    def __init__(self):
        self.user = User()

    def registrar(self,username,email,password):
        nomeUser = Nome()
        emailUser = Email()
        passwordUser = Senha()
        nomeUser.set(username)
        emailUser.set(email)
        passwordUser.set(password)

        #Criar Salt e Hash
        salt = bcrypt.gensalt()
        convertPassword = passwordUser.get().encode('utf-8')
        hashed = bcrypt.hashpw(convertPassword,salt)
        try:
            #Criar um id Unico para o usuario
            while True:
                idAux = self.gerarID()
                unique = self.uniqueID(idAux)
                if unique:
                    break
            CHECK_QUERY = "SELECT * FROM Usuario WHERE Email = %s"
            check_params = (emailUser.get(),)
            result = executeQuery(CHECK_QUERY,check_params)
            if len(result) > 0:
                print("Email ja registrado")
                return False

            QUERY = """
            INSERT INTO Usuario (Email,Nome,Salt,SenhaHash,Saldo,IdEstoque) 
            VALUES (%s,%s,%s,%s,%s,%s)
            """
            insert_params = (
                emailUser.get(),
                nomeUser.get(),
                salt,
                hashed,
                0,
                idAux,
            )
            executeQuery(QUERY,insert_params)
            self.user.setUser(nomeUser.get(),emailUser.get(),passwordUser.get(),0,idAux)
            return self.user
        
        except Error as e:
            print(f"Erro: {e}")
            return None
    
    def login(self,email,password):
        emailUser = Email()
        passwordUser = Senha()
        emailUser.set(email)
        passwordUser.set(password)
        try:
            #Checar se o Usuario existe no DB
            QUERY = "SELECT * FROM Usuario WHERE Email = %s"
            params = (emailUser.get(),)
            aux = executeQuery(QUERY,params)
            if len(aux) == 0:
                return None
            
            #Checar se as senhas são iguais
            userInfo = aux[0]
            saltDB = userInfo[2].encode('utf-8')
            passwordUserConvert = passwordUser.get().encode('utf-8')
            hashPasswordDB = userInfo[3].encode('utf-8')
            checkHashed = bcrypt.hashpw(passwordUserConvert,saltDB)

            #if bcrypt.checkpw(checkHashed, hashPasswordDB):
            if checkHashed == hashPasswordDB:
                self.user.setUser(userInfo[1],emailUser.get(),passwordUser.get(),userInfo[5],userInfo[4])
                return self.user
            else:
                return None     
            
        except Error as e:
            print(e)
            return None

    def gerarID(self):
        return random.randint(0,2**16-1)
    
    def uniqueID(self,idAux):
        QUERY_UNIQUE = "SELECT IdEstoque FROM Usuario WHERE IdEstoque = %s"
        params = (idAux,)
        result = executeQuery(QUERY_UNIQUE,params)
        if len(result) == 0:
            return True
        return False
    
    def getUser(self):
        return self.user