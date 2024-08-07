from flask import Flask, request, render_template, jsonify,redirect,url_for, session
from servicos.connection import load_dotenv,dotenv_path,flaskSecret
from servicos.loginConnection import *
from servicos.managmentEstoque import *

app = Flask(__name__)
app.secret_key = flaskSecret
load_dotenv(dotenv_path=dotenv_path)

@app.route('/')
def storePage():    
    username = None
    if 'userID' in session:
        idUser = session['userID']
        email = session['Email']
        username = session['username']
        return render_template('index.html', username = username)
    return redirect(url_for('loginPage'))
    

@app.route('/favoritos')
def favPage():
    username = None
    if 'userID' in session:
        idUser = session['userID']
        email = session['Email']
        username = session['username']
        return render_template('favoritos.html')
    return redirect(url_for('loginPage'))

@app.route('/historico')
def histPage():
    username = None
    if 'userID' in session:
        idUser = session['userID']
        email = session['Email']
        username = session['username']
        return render_template('historico.html')
    return redirect(url_for('loginPage'))

@app.route('/estoque',methods=['GET','POST'])
def estoquePage():
    username = None
    #checar se o usuario ja foi logado
    if 'userID' in session:
        estoque = Estoque()
        idUser = session['userID']
        estoque.set(idUser)
        username = session['username']
        if request.method == 'POST':
            data = request.json
            titulo = data.get('title')
            autor = data.get('author')
            ACTION = data.get('action')
            if ACTION == 'add':
                quantidade = data.get('quantity')
                preco = float(data.get('price'))
                adicionou = estoque.adicionar(titulo,autor,quantidade,preco)
                if (adicionou):
                    return jsonify({"message":"sucesso ao adicionar","status":"sucess"}),200
                return jsonify({"message":"Erro na adicao","status":"fail"}),401

            elif ACTION == 'remove':
                removeu = estoque.remover(titulo,autor)
                if removeu:
                    return jsonify({"message":"sucesso ao remover","status":"sucess"}),200
                return jsonify({"message":"Erro ao remover","status":"fail"}),401
            else:
                return jsonify({"message":"Acao invalida","status":"fail"}),401
        
        #Para mostrar todos os livros do estoque
        elif request.method == 'GET':
            livros = estoque.select()
            if livros:
                return render_template('estoque.html',Books=livros,username = username)
            return render_template('estoque.html',username=username)
        
    #caso o usuario não esteja logado
    return redirect(url_for('loginPage'))

@app.route('/login',methods=['GET','POST'])
def loginPage():
    if request.method == 'POST':
        data = request.json
        ACTION = data.get('action')
        EMAIL = data.get('email')
        PASSWORD = data.get('password')

        if ACTION == 'login':
            user = Usuario()
            user.login(EMAIL,PASSWORD)
            if user:
                session['userID'] = user.getUser().getID()

                session['username'] = user.getUser().getName()

                session['Email'] = user.getUser().getEmail()

                return jsonify({"message":"Login Valido","status":"sucess","redirect":url_for('storePage')}),200
            
            return jsonify({"message":"Login invalido","status":"fail"}),401
        
        elif ACTION == 'register':
            USERNAME = data.get('username')
            user = Usuario()
            user.registrar(USERNAME,EMAIL,PASSWORD)
            if user:
                session['userID'] = user.getUser().getID()
                session['username'] = user.getUser().getName()
                session['Email'] = user.getUser().getEmail()

                #Criar o estoque do usuario no BD
                estoque = Estoque()
                idAux = user.getUser().getID()
                estoque.set(idAux)
                if estoque.criar():
                    return jsonify({"message":"Registro Valido","status":"sucess","redirect":url_for('storePage')}),200
            return jsonify({"message":"Registro invalido","status":"fail"}),401
        else:
            return jsonify({"message": "Ação inválida", "status": "fail"}), 400
        
    #Caso seja metodo GET
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('storePage'))

if __name__ == '__main__':
    app.run(debug=True, port =5500) 
