from dominios.Usuario import *

class TUUser:
    def __init__(self):
        self.VALOR_VALIDO_EMAIL = 'roberto@gmail.com'
        self.VALOR_INVALIDO_EMAIL = 'robertin#unb'
        self.VALOR_VALIDO_NOME = 'Jorge Souza'
        self.VALOR_INVALIDO_NOME = 'elyn smith'
        self.VALOR_VALIDO_SENHA = '143852'
        self.VALOR_INVALIDO_SENHA = '987654'

        self.estado = 0
        self.SUCESSO = 0
        self.FALHA = -1

    def CenarioSucesso(self):
        try:
            aux = Email()
            aux.set(self.VALOR_VALIDO_EMAIL)
            if aux.get() != self.VALOR_VALIDO_EMAIL:
                self.estado = self.FALHA

        except:
            self.estado = self.FALHA

        try:
            aux = Senha()
            aux.set(self.VALOR_VALIDO_SENHA)
            if aux.get() != self.VALOR_VALIDO_SENHA:
                self.estado = self.FALHA

        except:
            self.estado = self.FALHA

        try:
            aux = Nome()
            aux.set(self.VALOR_VALIDO_NOME)
            if aux.get() != self.VALOR_VALIDO_NOME:
                self.estado = self.FALHA

        except:
            self.estado = self.FALHA

    def CenarioFalha(self):
        try:
            aux = Email()
            aux.set(self.VALOR_INVALIDO_EMAIL)
            self.estado = self.FALHA

        except:
            if aux.get() == self.VALOR_INVALIDO_EMAIL:
                self.estado = self.FALHA

        try:
            aux = Senha()
            aux.set(self.VALOR_INVALIDO_SENHA)
            self.estado = self.FALHA

        except:
            if aux.get() == self.VALOR_INVALIDO_SENHA:
                self.estado = self.FALHA

        try:
            aux = Nome()
            aux.set(self.VALOR_INVALIDO_NOME)
            self.estado = self.FALHA

        except:
            if aux.get() == self.VALOR_INVALIDO_NOME:
                self.estado = self.FALHA

    

    def run(self):
        self.CenarioSucesso()
        self.CenarioFalha()
        return self.estado
    


teste = TUUser()
if (teste.run() == 0):
    print('Yeyy')
else:
    print('Droga')