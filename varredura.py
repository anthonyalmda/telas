from tkinter import Tk
from operacao import Operacional
from time import time,ctime
from  datetime import datetime
class Varredura(Operacional):
    def __init__(self,con):
        self.con=con
        self.padroes()
        self.telavarredura = Tk()
        self.janelavarredura()
        self.rodapesquisa()
        self.telavarredura.mainloop()
    def janelavarredura(self):
        self.telavarredura.title('Busca ativa do sistema')
        self.telavarredura.geometry('700x400+400+200')
        self.telavarredura.configure(bg=self.corjn2)
    def rodapesquisa(self,timeframe='h4'):
        timeframe = timeframe.upper()
        while True:
            data = str(datetime.now())[0:10]
            tempo = str(datetime.now())[11:19]

            hora = tempo[0:2]
            print(tempo, data, hora)
            self.testaparescompra(3,'h4')
            quit()
