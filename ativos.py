from tkinter import Toplevel, Tk
from tkinter import Label, Frame, Entry, Button, RAISED, SOLID, RIDGE, ttk
from apoio import Apoio
from parametros import Param


##precisa integrar banco de dados
class Ativos(Apoio):
    def __init__(self):
        self.jn_ativo = Tk()
        self.padroes()
        self.tela_ativo()
        self.jn_ativo.mainloop()

    def tela_ativo(self):
        self.jn_ativo.title('TROCA DE ATIVOS')
        self.jn_ativo.geometry('350x250')
        self.jn_ativo.configure(background=self.corjn)
        self.jn_ativo.resizable(width=False, height=False)
        self.frame_ativo()
        self.label_ativo()
        self.button_ativo()

    def frame_ativo(self):
        self.frame_cima = Frame(self.jn_ativo, width=350, height=0, bg=self.corjn, relief='flat')
        self.frame_cima.grid(row=0, column=0, pady=1, padx=1)

        self.frame_baixo = Frame(self.jn_ativo, width=350, height=250, bg=self.corjn, relief='flat')
        self.frame_baixo.grid(row=1, column=0, pady=1, padx=1)

    def label_ativo(self):
        l_nome4 = Label(self.frame_baixo, text="TROCA DE ATIVOS", font=('Candara 25 italic bold'), bg=self.corjn,
                        fg=self.corjn3)
        l_nome4.place(x=50, y=1)

        lista = ('BTC', 'REAL', 'DOLAR', 'EURO')

        l_nome4 = Label(self.frame_baixo, text="ATIVO 1", font=('Candara 23 italic bold'), bg=self.corjn,
                        fg=self.corjn3)
        l_nome4.place(x=25, y=60)
        # -------------------------------Combobox com a lista de timeframes
        lista = ('BTC', 'REAL', 'DOLAR', 'EURO')
        self.entipo = ttk.Combobox(self.frame_baixo, width=10, font=self.fonte16, values=lista, validate='key')
        self.entipo.place(x=20, y=110)

        l_nome4 = Label(self.frame_baixo, text="ATIVO 2", font=('Candara 23 italic bold'), bg=self.corjn,
                        fg=self.corjn3)
        l_nome4.place(x=195, y=60)
        # -------------------------------Combobox com a lista de timeframes
        lista2 = ('MOEDA', 'MOEDA', 'DINHEIRO', 'MOEDINHA')
        self.entipo = ttk.Combobox(self.frame_baixo, width=10, font=self.fonte16, values=lista2, validate='key')
        self.entipo.place(x=190, y=110)

    def button_ativo(self):
        self.b_confirmar = Button(self.frame_baixo, text='CONFIRMAR', width=20, height=2, font=('Candara 10 bold'),
                                  bg=self.corjn3, fg=self.corjn, relief=SOLID, overrelief=RIDGE)
        self.b_confirmar.place(x=100, y=180)


if __name__ == "__main__":
    Ativos()