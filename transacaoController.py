import json
from datetime import *
from Models.models import Transacao, Conta

class TransacaoController():
    def __init__(self, extratosList, extratosDir):
        self.extratosList = extratosList
        self.extratosDir = extratosDir
    def updateJson(self):
        with open(self.extratosDir, 'w') as updateFile:
            json.dump(self.extratosList, updateFile, indent=4)
    def registrarTransacao(self, tipo, valor, conta, data):
        data = datetime.now()
        novaTransacao = Transacao(tipo, valor, conta, data)
        converteTransacao = vars(novaTransacao)
        self.extratosList.append(converteTransacao)
        self.updateJson()
