tkinter import Toplevel, Tk
from tkinter import Label, Frame, Entry, Button, RAISED, RIDGE, ttk
from apoio import Apoio


class Param(Apoio):
    def __init__(self):
        self.jn_parametro = Tk()
        self.padroes()
        self.tela_parametro()
        self.jn_parametro.mainloop()

    def tela_parametro(self):
        self.jn_parametro.title('')
        self.jn_parametro.geometry('550x401')
        self.jn_parametro.configure(background=self.corjn)
        self.jn_parametro.resizable(width=False, height=False)
        self.frame_parametros()
        self.label_parametro()
        self.button_parametro()

    def frame_parametros(self):
        self.frame_cima = Frame(self.jn_parametro, width=600, height=50, bg=self.corjn, relief='flat')
        self.frame_cima.grid(row=0, column=0, pady=1, padx=1)

        self.frame_baixo = Frame(self.jn_parametro, width=600, height=500, bg=self.corjn, relief='flat')
        self.frame_baixo.grid(row=1, column=0, pady=1, padx=1)

    def label_parametro(self):
        l_nome = Label(self.frame_cima, text="DEFINIÇÕES ", font=('Candara 30 bold  '), bg=self.corjn,
                       fg=self.corjn3)
        l_nome.place(x=160, y=1)

        l_linha = Label(self.frame_cima, text=" ", width=800, font=('Candara 1'), bg=self.corjn3, fg=self.corjn3)
        l_linha.place(x=0, y=45)
        # configurando frame de baixo
        # nomes em latim pra editar depois com os nomes reais dos parametros
        l_nome0 = Label(self.frame_baixo, text=" ", font=('Candara 10 italic'),
                        bg=self.corjn, fg=self.corlt4)
        l_nome0.place(x=10, y=1)
        l_nome1 = Label(self.frame_baixo, text="VALOR DE ENTRADA", font=('Candara 15 bold italic'), bg=self.corjn, fg=self.corjn3)
        l_nome1.place(x=15, y= 1)
        e_nome1 = Entry(self.frame_baixo, width=20, justify='left', bg=self.corjn, font=("", 15), highlightthickness=1,
                        relief='solid')
        e_nome1.place(x=15, y=31)

        l_nome2 = Label(self.frame_baixo, text="VALOR DA BANCA", font=('Candara 15 bold italic'), bg=self.corjn, fg=self.corjn3)
        l_nome2.place(x=15, y=71)
        e_nome2 = Entry(self.frame_baixo, width=20, justify='left', bg=self.corjn, font=("", 15), highlightthickness=1,
                        relief='solid')
        e_nome2.place(x=15, y=101)

        l_nome3 = Label(self.frame_baixo, text="PARAMETRO A DEFINIR", font=('Candara 15 bold italic'), bg=self.corjn, fg=self.corjn3)
        l_nome3.place(x=15, y=141)
        e_nome3 = Entry(self.frame_baixo, width=20, justify='left', bg=self.corjn, font=("", 15), highlightthickness=1,
                        relief='solid')
        e_nome3.place(x=15, y=171)

        l_nome4 = Label(self.frame_baixo, text="TIMEFRAME", font=('Candara 15 bold italic'), bg=self.corjn, fg=self.corjn3)
        l_nome4.place(x=15, y=211)
        # -------------------------------Combobox com a lista de timeframes
        lista = ('H1', 'H4', 'DIARIO','D1', 'WE')
        self.entipo = ttk.Combobox(self.frame_baixo, width=17, font=self.fonte16, values=lista, validate='key')
        self.entipo.place(x=15, y=241)

        l_nome5 = Label(self.frame_baixo, text="PARAMETRO A DEFINIR ", font=('Candara 15 bold italic'), bg=self.corjn, fg=self.corjn3)
        l_nome5.place(x=300, y=1)
        e_nome5 = Entry(self.frame_baixo, width=20, justify='left', bg=self.corjn, font=("", 15), highlightthickness=1, relief='solid')
        e_nome5.place(x=300, y=31)

        l_nome6 = Label(self.frame_baixo, text="PARAMETRO A DEFINIR", font=('Candara 15 bold italic'), bg=self.corjn, fg=self.corjn3)
        l_nome6.place(x=300, y=71)
        e_nome6 = Entry(self.frame_baixo, width=20, justify='left', bg=self.corjn, font=("", 15), highlightthickness=1,
                        relief='solid')
        e_nome6.place(x=300, y=101)

        l_nome6 = Label(self.frame_baixo, text="PARAMETRO A DEFINIR", font=('Candara 15 bold italic'), bg=self.corjn, fg=self.corjn3)
        l_nome6.place(x=300, y=141)
        e_nome6 = Entry(self.frame_baixo, width=20, justify='left', bg=self.corjn, font=("", 15), highlightthickness=1,
                        relief='solid')
        e_nome6.place(x=300, y=171)

        l_pass = Label(self.frame_baixo, text="URL API: ", font=('Candara 15 bold italic'), bg=self.corjn, fg=self.corjn3)
        l_pass.place(x=300, y=211)
        e_pass = Entry(self.frame_baixo, width=20, justify='left', bg=self.corjn, font=("", 15), highlightthickness=1,
                       relief='solid')
        e_pass.place(x=300, y=241)




    def button_parametro(self):
        self.b_confirmar = Button(self.frame_baixo, text='CONFIRMAR', width=20, height=2, font=('Candara 10 bold'),
                                  bg=self.corjn3, fg=self.corjn, relief=RAISED, overrelief=RIDGE)
        self.b_confirmar.place(x=200, y=300)

if __name__ == "__main__":
    Param()