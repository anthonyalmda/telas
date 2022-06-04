#from tkinter import Tk
from parametros import Param
from bancomysq import Cliente
from varredura import Varredura
from msgtelegram import Telegram

class Criptobot(Param,Varredura,Telegram):
    def __init__(self):
        #self.root = Tk()
        self.padroes()
        #self.tela()
        #print(self.historico('ethbRL','h4',5))
        #self.temporario('consegui com a função simplificada')
        cliente = Cliente.get(Cliente.cod_cli==self.vl_cliente)
        Varredura(cliente.timeframe)
        #print(self.moedas())
        #self.root.mainloop()
    def tela(self):
        self.root.title('Robô de criptomoedas')
        self.root.geometry('400x200+500+100')

if __name__ == '__main__':
    Criptobot()
