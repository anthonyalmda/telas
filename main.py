from operacao import Operacional
from datetime import datetime
from apoio import Apoio
from dados import Dados
class CriptoBot(Apoio,Operacional):
    def __init__(self):
        #self.root = Tk()
        self.carrega()
        self.padroes()
        self.con = self.abredb(hostc=self.host, usuarioc=self.usuario, senhac=self.senha, bancoc=self.banco, porta=3306)
        for x in range(1):
            print(f'Passagem numero {x+1}')
            self.testaparescompra(0,'h1')
    def tela(self):
        self.root.title("Robô de operações no mercado financeiro")
        self.root.configure(bg=self.corjanela)
        self.root.geometry('630x540+10+20')
        #self.root.wm_iconbitmap('iconesistema.ico')
        #self.root.resizable(False, False)
if __name__=="__main__":
    root = CriptoBot()