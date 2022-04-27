from tkinter import Toplevel
from tkinter import Label, Frame, Entry, Button, RAISED, RIDGE, ttk
from apoio import Apoio

class Param(Apoio):
    def __init__(self):
        self.jn_parametro = Toplevel()
        self.padroes()
        self.tela_parametro()
        self.jn_parametro.mainloop()
    def tela_parametro(self):
        self.jn_parametro.title('')
        self.jn_parametro.geometry('900x500')
        self.jn_parametro.configure(background=self.corjn2)
        self.jn_parametro.resizable(width=False, height=False)
        self.frame_parametros()
        self.label_parametro()
        self.button_parametro()
    def frame_parametros(self):
        self.frame_cima = Frame(self.jn_parametro, width=270, height=50, bg=self.corjn2, relief='flat')
        self.frame_cima.grid(row=0, column=0, pady=1, padx=0)

        self.frame_baixo = Frame(self.jn_parametro, width=270, height=650, bg=self.corjn2, relief='flat')
        self.frame_baixo.grid(row=1, column=0, pady=1, padx=0)
    def label_parametro(self):
        l_nome = Label(self.frame_cima, text = "Definição ", font = ('Candara 25 bold  '), bg=self.corjn2, fg=self.corlt2)
        l_nome.place(x=5, y=1)
        
        l_linha = Label(self.frame_cima, text = "", width= 275, font = ('Candara 1'), bg=self.corjn, fg=self.corlt2)
        l_linha.place(x=10, y=45)
        #configurando frame de baixo
        # nomes em latim pra editar depois com os nomes reais dos parametros
        l_nome0 = Label(self.frame_baixo, text = "insira suas configurações de uso ", font = ('Candara 10 italic'), bg=self.corjn2, fg=self.corlt2)
        l_nome0.place(x=10, y=1)
        l_nome1 = Label(self.frame_baixo, text = "lorem ", font = ('Candara 15 italic'), bg=self.corjn2, fg=self.corlt2)
        l_nome1.place(x=10, y=20)
        e_nome1 = Entry(self.frame_baixo, width=20, justify= 'left', bg = self.corjn2, font = ("", 15), highlightthickness=1, relief='solid')
        e_nome1.place(x=14, y=50)
        
        l_nome2 = Label(self.frame_baixo, text = "ipsum ", font = ('Candara 15 italic'), bg=self.corjn2, fg=self.corlt2)
        l_nome2.place(x=10, y=80)
        e_nome2 = Entry(self.frame_baixo, width=20, justify= 'left', bg = self.corjn2, font = ("", 15), highlightthickness=1, relief='solid')
        e_nome2.place(x=14, y=110)
        
        l_nome3 = Label(self.frame_baixo, text = "ameno ", font = ('Candara 15 italic'), bg=self.corjn2, fg=self.corlt2)
        l_nome3.place(x=10, y=140)
        e_nome3 = Entry(self.frame_baixo, width=20, justify= 'left', bg = self.corjn2, font = ("", 15), highlightthickness=1, relief='solid')
        e_nome3.place(x=14, y=170)


        l_nome4 = Label(self.frame_baixo, text = "interino ", font = ('Candara 15 italic'), bg=self.corjn2, fg=self.corlt2)
        l_nome4.place(x=10, y=200)
        # -------------------------------Combobox com a lista de timeframes
        lista = ('H1', 'H4', 'D1', 'WE')
        self.entipo = ttk.Combobox(self.frame_baixo, width=14, font=self.fonte16, values=lista, validate='key')
        self.entipo.place(x=14, y=230)

        l_nome5 = Label(self.frame_baixo, text = "adapare ", font = ('Candara 15 italic'), bg=self.corjn2, fg=self.corlt2)
        l_nome5.place(x=10, y=260)
        e_nome5 = Entry(self.frame_baixo, width=20, justify= 'left', bg = self.corjn2, font = ("", 15), highlightthickness=1, relief='solid')
        e_nome5.place(x=14, y=290)
        
        l_nome6 = Label(self.frame_baixo, text = "dorime ", font = ('Candara 15 italic'), bg=self.corjn2, fg=self.corlt2)
        l_nome6.place(x=10, y=320)
        e_nome6 = Entry(self.frame_baixo, width=20, justify= 'left', bg = self.corjn2, font = ("", 15), highlightthickness=1, relief='solid')
        e_nome6.place(x=14, y=350)
        
        l_nome6 = Label(self.frame_baixo, text = "ave ", font = ('Candara 15 italic'), bg=self.corjn2, fg=self.corlt2)
        l_nome6.place(x=10, y=380)
        e_nome6 = Entry(self.frame_baixo, width=20, justify= 'left', bg = self.corjn2, font = ("", 15), highlightthickness=1, relief='solid')
        e_nome6.place(x=14, y=410)
        
        l_nome6 = Label(self.frame_baixo, text = "sentin ", font = ('Candara 15 italic'), bg=self.corjn2, fg=self.corlt2)
        l_nome6.place(x=10, y=440)
        e_nome6 = Entry(self.frame_baixo, width=20, justify= 'left', bg = self.corjn2, font = ("", 15), highlightthickness=1, relief='solid')
        e_nome6.place(x=14, y=470)
        
        l_pass = Label(self.frame_baixo, text = "URL API: ", font = ('Candara 15 italic'), bg=self.corjn2, fg=self.corlt2)
        l_pass.place(x=10, y=500)
        e_pass = Entry(self.frame_baixo, width=20, justify= 'left', bg = self.corjn2, font = ("", 15), highlightthickness=1, relief='solid')
        e_pass.place(x=14, y=530)
    def button_parametro(self):
        self.b_confirmar = Button(self.frame_baixo,  text = 'CONFIRMAR' ,width=20, height=2, font = ('Candara 10 bold'), bg=self.corjn2, fg=self.corlt1, relief=RAISED, overrelief=RIDGE)
        self.b_confirmar.place(x=14, y=580)
