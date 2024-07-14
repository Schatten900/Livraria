import bcrypt
import random
from servicos.connection import executeQuery,Error
from dominios.Usuario import User,Nome,Senha,Email

def gerarID():
    return random.randint(0,2**16-1)

def uniqueID(user_id):
    QUERY_UNIQUE = "SELECT ID_Estoque FROM Usuario WHERE ID_Estoque = %s"
    params = (user_id,)
    result = executeQuery(QUERY_UNIQUE,params)
    if len(result) == 0:
        return True
    return False

def gerarHashPassword(password,salt):
    hashed = bcrypt.hashpw(password,salt)
    return hashed

def registerUser(username,email,password,confirm):
    nomeUser = Nome()
    emailUser = Email()
    passwordUser = Senha()
    nomeUser.set(username)
    emailUser.set(email)
    passwordUser.set(password)

    salt = bcrypt.gensalt()
    convertPassword = passwordUser.get().encode('utf-8')
    hashed = gerarHashPassword(convertPassword,salt)
    try:
        while True:
            id = gerarID()
            unique = uniqueID(id)
            if unique:
                break
        CHECK_QUERY = "SELECT * FROM Usuario WHERE Email = %s"
        check_params = (emailUser.get(),)
        result = executeQuery(CHECK_QUERY,check_params)
        if len(result) > 0:
            print("Email ja registrado")
            return False
        
        if confirm != password:
            print("Senhas devem ser iguais")
            return False

        QUERY = """
        INSERT INTO Usuario (Username,Email,Hash_Password,Salt,Saldo,ID_estoque) 
        VALUES (%s,%s,%s,%s,%s,%s)
        """
        insert_params = (
            nomeUser.get(),
            emailUser.get(),
            hashed,
            salt,
            0,
            id
        )
        executeQuery(QUERY,insert_params)
        user = User()
        user.setUser(nomeUser.get(),emailUser.get(),passwordUser.get(),id)
        return user
    except Error as e:
        print(f"Erro: {e}")
        return None


def loginUser(email,password):
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
        saltDB = userInfo[3].encode('utf-8')
        passwordUserConvert = passwordUser.get().encode('utf-8')
        hashPasswordDB = userInfo[2].encode('utf-8')
        checkHashed = gerarHashPassword(passwordUserConvert,saltDB)

        #if bcrypt.checkpw(checkHashed, hashPasswordDB):
        if checkHashed == hashPasswordDB:
            user = User()
            user.setUser(userInfo[0],emailUser.get(),passwordUser.get(),userInfo[5])
            return user
        else:
            return None     
        
    except Error as e:
        print(e)
        return None
