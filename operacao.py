from dados import Dados
from tkinter import messagebox
from datetime import datetime
from ComandosBinance import Bnbcomand
class operacional(Bnbcomand,Dados):
    def testapares(self,df):
        self.abredb(hostc=self.host, usuarioc=self.usuariodb, senhac=self.senhadb, bancoc=self.banco, porta=3306)
        for linha in df:

            parbase =''
            parcompra= ''
            if df['preco_abertura'] == self.cotacao(parbase+parcompra):
                valores = [df['preco_abertura'],True,datetime.now()]
                self.ptab(valores=valores, operacao='P', tabela='operacoes', campos=['preco_abertura','aberto','datahoraabertura'], chave='ativo', vlchave=df['ativo'])

    def carrega(self, par, valor):
        if valor == self.cotacao(par=par):
            messagebox(f'o par {par} encontra-se no preço de compra valor: {valor}')
            return True
        return False

    def varredura(self):
        pass
