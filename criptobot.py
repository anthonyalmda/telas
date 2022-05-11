#from tkinter import Tk
from parametros import Param
from varredura import Varredura

class Criptobot(Param,Varredura):
    def __init__(self):
        #self.root = Tk()
        self.padroes()
        #self.tela()
        #print(self.historico('ethbRL','h4',5))
        Varredura()
        #print(self.moedas())
        #self.root.mainloop()
    def tela(self):
        self.root.title('Robô de criptomoedas')
        self.root.geometry('400x200+500+100')

if __name__ == '__main__':
    DASH = Criptobot()
