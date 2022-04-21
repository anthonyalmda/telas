from tkinter import Tk
from datetime import datetime
from ComandosBinance import Bnbcomand
from apoio import Apoio
class CriptoBot(Apoio,Bnbcomand):
    def __init__(self):
        #self.root = Tk()
        self.carrega()
        self.padroes()
        self.ativa(chave=self.chave_api,senha=self.senha_api)
        #teste = self.converte(origem='USDT',destino='BRL', capital=10)
        print(datetime.now())
        for x in range(100):
            teste = self.testevela('BNBBRL','h4',3)
            valor = teste.loc[2]['close']
            print(f'vez {x} valor {valor}')
        print(datetime.now())
        #self.tela()
        #self.grafa2(par='BNBBRL',time='h4',velas=15)
        #self.root.mainloop()
    def tela(self):
        self.root.title("Robô de operações no mercado financeiro")
        self.root.configure(bg=self.corjanela)
        self.root.geometry('630x540+10+20')
        #self.root.wm_iconbitmap('iconesistema.ico')
        #self.root.resizable(False, False)
if __name__=="__main__":
    root = CriptoBot()