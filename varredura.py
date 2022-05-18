import asyncio
from tkinter import Tk, Button
from operacional import Operacional
from datetime import datetime
from msgtelegram import Telegram
#from multiprocessing import Pool
from multiprocessing.dummy import Pool

class Varredura(Operacional,Telegram):
    def __init__(self):
        self.sair = False
        self.padroes()
        self.telavarredura = Tk()
        self.janelavarredura()
        self.telavarredura.mainloop()

    def janelavarredura(self):
        self.telavarredura.title('Busca ativa do sistema')
        self.telavarredura.geometry('700x400+400+200')
        self.telavarredura.configure(bg=self.corjn2)
        self.varre_buton()

    def varre_buton(self):
        self.btn_iniciar = Button(self.telavarredura, text='Iniciar', command=self.inicio)
        self.btn_iniciar.place(x=600, y=1)
        self.btn_sair = Button(self.telavarredura, text='Sair', command=self.sairfunc)
        self.btn_sair.place(x=600, y=40)


    def pesquisa_oportunidades(self, timeframe):
        timeframe = timeframe.upper()
        #import ipdb ; ipdb.set_trace()
        while True:
            if self.sair:
                break
            dt_data = str(datetime.now())[0:10]
            dt_dia = int(dt_data[8:])
            dt_hora = int(str(datetime.now())[11:13])
            #self.testaparescompra(3, 'h4', self.cliente)
            if timeframe == 'H1':
                if dt_hora != dt_thora:
                    dt_thora = dt_hora
                    self.testaparescompra(3, 'h4', self.cliente)
            elif timeframe == 'H4':
                if int(dt_hora)%4 == 0 and dt_hora != dt_thora:
                    dt_thora = dt_hora
                    self.testaparescompra(0, 'h4')
            self.testacompra()

    def inicio(self):
        self.sair = False
        funcao = self.pesquisa_oportunidades
        workers = Pool(1)
        workers.map_async(funcao, 'h1')

    def sairfunc(self):
        self.sair = True
