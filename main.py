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

@app.route('/estoque')
def estoquePage():
    username = None
    if 'userID' in session:
        idUser = session['userID']
        email = session['Email']
        username = session['username']
        livros = selectBooks(idUser)
        return render_template('estoque.html',Books=livros,Username = session['userID'])
    return redirect(url_for('loginPage'))

@app.route('/login',methods=['GET','POST'])
def loginPage():
    if request.method == 'POST':
        data = request.json
        ACTION = data.get('action')
        if ACTION == 'login':
            EMAIL = data.get('email')
            PASSWORD = data.get('password')
            user = loginUser(EMAIL,PASSWORD)
            if user:
                session['userID'] = user.getID()
                session['username'] = user.getName()
                session['Email'] = user.getEmail()
                return jsonify({"message":"Login Valido","status":"sucess","redirect":url_for('storePage')}),200
            
            return jsonify({"message":"Login invalido","status":"fail"}),401
        
        elif ACTION == 'register':
            USERNAME = data.get('username')
            EMAIL = data.get('email')
            PASSWORD = data.get('password')
            CONFIRM = data.get('confirm')

            user = registerUser(USERNAME,EMAIL,PASSWORD,CONFIRM)
            if user:
                session['userID'] = user.getID()
                session['username'] = user.getName()
                session['Email'] = user.getEmail()
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
