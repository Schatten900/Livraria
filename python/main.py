from flask import Flask, request, render_template, jsonify
from bancoDados.connection import connectSQL,load_dotenv,dotenv_path
from bancoDados.loginConnection import *
from bancoDados.managmentEstoque import *
import requests
import os

app = Flask(__name__)

load_dotenv(dotenv_path=dotenv_path)

@app.route('/estoque')
def estoque():
    pass

@app.route('/login',methods=['POST'])
def loginOrRegister():
    data = request.json
    ACTION = data.get('action')
    if ACTION == 'login':
        EMAIL = data.get('email')
        PASSWORD = data.get('password')
        user = loginUser(EMAIL,PASSWORD)
        if user:
            return jsonify({"message":"Logado com Sucesso", "status":"sucess"})
        return jsonify({"message":"Login invalido","status":"fail"}),401
    else:
        USERNAME = data.get('username')
        EMAIL = data.get('email')
        PASSWORD = data.get('password')
        CONFIRM = data.get('confirm')
        registrou = registerUser(USERNAME,EMAIL,PASSWORD,CONFIRM)
        if registrou:
            return jsonify({"message":"Logado com Sucesso", "status":"sucess"})
        return jsonify({"message":"Login invalido","status":"fail"}),401


if __name__ == '__main__':
    app.run(debug=True, port =5500) 
