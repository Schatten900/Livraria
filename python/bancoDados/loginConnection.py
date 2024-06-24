import bcrypt
import random
from bancoDados.connection import executeQuery,Error
from dominios.Usuario import User,Nome,Senha,Email

def gerarID():
    return random.randint(0,2**16-1)

def uniqueID(user_id):
    QUERY_UNIQUE = "SELECT ID_Estoque FROM Usuario WHERE ID_Estoque = %s"
    params = user_id
    result = executeQuery(QUERY_UNIQUE,params)
    if len(result) == 0:
        return True
    return False

def gerarHashPassword(password,salt):
    hashed = bcrypt.hashpw(password.encode('utf-8'),salt)
    return hashed

def registerUser(username,email,password,confirm):
    nomeUser = Nome()
    emailUser = Email()
    passwordUser = Senha()
    nomeUser.set(username)
    emailUser.set(email)
    passwordUser.set(password)

    salt = bcrypt.gensalt()
    hashed = gerarHashPassword(passwordUser.get(),salt)
    try:
        while True:
            ID = gerarID()
            if uniqueID(ID):
                break
        CHECK_QUERY = "SELECT * FROM Usuario WHERE Email = %s"
        check_params = (emailUser.get(),)
        result = executeQuery(CHECK_QUERY,check_params)
        if len(result) > 0:
            print("Email ja registrado")
            return False
        if confirm != password:
            return False

        QUERY = """INSERT INTO (Username,Email,Hash_Password,Salt,Saldo,ID_estoque) VALUES (%s,%s,%s,%s,%s,%s)"""
        insert_params = (
            nomeUser.get(),
            emailUser.get(),
            hashed,
            salt,
            0,
            ID
        )
        executeQuery(QUERY,insert_params)
        print("Registrado com sucesso")
        return True
    except Error as e:
        print(Error)

def loginUser(email,password):
    emailUser = Email()
    passwordUser = Senha()
    emailUser.set(email)
    passwordUser.set(password)

    params = (emailUser.get(),)
    try:
        QUERY = "SELECT * FROM Usuario WHERE Email = %s"

        aux = executeQuery(QUERY,params)
        if len(aux) == 0:
            print("Conta nao identificada")
            return None
        
        userInfo = aux[0]
        salt = userInfo['Salt']
        hash_password = userInfo['Hash_Password']
        hashed = gerarHashPassword(passwordUser.get(),salt)
        if hash_password == hashed:
            user = User()
            user.setUser(userInfo['Username'],emailUser.get(),passwordUser.get())
            return user
        else:
            print("Senha incorreta")
            return None     
    except Error as e:
        print(e)
        return None
    