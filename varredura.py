from tkinter import Tk
from operacional import Operacional
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
    def rodapesquisa(self,time='h4'):
        time = time.upper()
        data = ''
        tdia = thora = 0
        teste = False
        while True:
            data = str(datetime.now())[0:10]
            tempo = str(datetime.now())[11:19]
            dia = int(data[8:])
            hora = int(tempo[0:2])
            if time == 'H1':
                if hora != thora:
                    thora = hora
                    teste = True
            self.testaparescompra(3,'h4')
            quit()
