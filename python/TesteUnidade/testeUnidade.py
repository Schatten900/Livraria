from dominios.Usuario import *

class TUName:
    def __init__(self):
        self.VALOR_VALIDO = 'Thiago Marthins'
        self.VALOR_INVALIDO = 'ricardo Fred'
        self.estado = 0
        self.SUCESSO = 0
        self.FALHA = -1

    def CenarioSucesso(self):
        try:
            aux = Nome()
            aux.set(self.VALOR_VALIDO)
            if aux.get() != self.VALOR_VALIDO:
                self.estado = self.FALHA

        except Exception as e:
            self.estado = self.FALHA

    def CenarioFalha(self):
        try:
            aux = Nome()
            aux.set(self.VALOR_INVALIDO)
            self.estado = self.FALHA

        except Exception as e:
            if aux.get() == self.VALOR_INVALIDO:
                self.estado = self.FALHA

    def run(self):
        self.CenarioSucesso()
        self.CenarioFalha()
        return self.estado
    
class TUSenha:
    def __init__(self):
        self.VALOR_VALIDO = '153862'
        self.VALOR_INVALIDO = '123123'
        self.estado = 0
        self.SUCESSO = 0
        self.FALHA = -1

    def CenarioSucesso(self):
        try:
            aux = Senha()
            aux.set(self.VALOR_VALIDO)
            if aux.get() != self.VALOR_VALIDO:
                self.estado = self.FALHA

        except Exception as e:
            self.estado = self.FALHA

    def CenarioFalha(self):
        try:
            aux = Senha()
            aux.set(self.VALOR_INVALIDO)
            self.estado = self.FALHA

        except Exception as e:
            if aux.get() == self.VALOR_INVALIDO:
                self.estado = self.FALHA

    def run(self):
        self.CenarioSucesso()
        self.CenarioFalha()
        return self.estado
    
class TUEmail:
    def __init__(self):
        self.VALOR_VALIDO = 'roberto@gmail.com'
        self.VALOR_INVALIDO = 'robertin@unb'
        self.estado = 0
        self.SUCESSO = 0
        self.FALHA = -1

    def CenarioSucesso(self):
        try:
            aux = Email()
            aux.set(self.VALOR_VALIDO)
            if aux.get() != self.VALOR_VALIDO:
                self.estado = self.FALHA

        except Exception as e:
            self.estado = self.FALHA

    def CenarioFalha(self):
        try:
            aux = Email()
            aux.set(self.VALOR_INVALIDO)
            self.estado = self.FALHA

        except Exception as e:
            if aux.get() == self.VALOR_INVALIDO:
                self.estado = self.FALHA

    def run(self):
        self.CenarioSucesso()
        self.CenarioFalha()
        return self.estado
    
    
teste0 = TUName()
if (teste0.run() == 0):
    print('Yeyy')
else:
    print('Droga')

teste1 = TUSenha()
if (teste1.run() == 0):
    print('Yeyy')
else:
    print('Droga')

teste2 = TUEmail()
if (teste2.run() == 0):
    print('Yeyy')
else:
    print('Droga')
