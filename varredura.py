from tkinter import Tk, Button
from operacional import Operacional
from datetime import datetime
from asyncio import get_event_loop, coroutine, get_running_loop
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor


class Varredura(Operacional):
    def __init__(self):
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

    async def inicio(self):
        loop = get_running_loop()
        with ProcessPoolExecutor() as pool:
            resultado = await loop.run_in_executor(self.pesquisa_oportunidades,'h1')
        # loop.run_until_complete(self.pesquisa_oportunidades('h1'))
        # loop.close()

        #targete = Pesquisa_oportunidades
        #lista = ['H1']
        #trabalhovarre = Pool(1)
        #respostavarre = trabalhovarre.map(targete, lista)

    def pesquisa_oportunidades(self, timeframe):
        timeframe = timeframe.upper()
        dt_data = ''
        dt_tdia = dt_thora = 0
        bo_teste = False
        #import ipdb ; ipdb.set_trace()
        while True:
       # for x in range(3):
            dt_data = str(datetime.now())[0:10]
            dt_dia = int(dt_data[8:])
            dt_hora = int(str(datetime.now())[11:13])
            self.testaparescompra(3, 'h4', self.cliente)
            if timeframe == 'H1':
                if dt_hora != dt_thora:
                    dt_thora = dt_hora
                    bo_teste = True
                    self.testaparescompra(3, 'h4', self.cliente)
            elif timeframe == 'H4':
                if int(dt_hora)%4 == 0 and dt_hora != dt_thora:
                    dt_thora = dt_hora
                    bo_teste = True
                    self.testaparescompra(0, 'h4')
            #break
