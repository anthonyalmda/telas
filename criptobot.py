from tkinter import Tk
from parametros import Param

class Criptobot:
    def __init__(self):
        self.root = Tk()
        self.tela()
        Param()
        self.root.mainloop()
    def tela(self):
        self.root.title('Robô de criptomoedas')
        self.root.geometry('400x200+500+100')

if __name__ == '__main__':
    DASH = Criptobot()
