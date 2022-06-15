from tkinter import Toplevel, Tk
from tkinter import Label, Frame, Entry, Button, RAISED, RIDGE, GROOVE, ttk
from apoio import Apoio



class Param(Apoio):
    def __init__(self):
        self.jn_parametro = Tk()
        self.padroes()
        self.tela_parametro()
        self.jn_parametro.mainloop()

    def tela_parametro(self):
        self.jn_parametro.title('PARAMETROS')
        self.jn_parametro.geometry('450x500')
        self.jn_parametro.configure(background=self.corjn2)
        self.jn_parametro.resizable(width=False, height=False)
        self.frame_parametros()
        self.label_parametro()
        self.button_parametro()

    def frame_parametros(self):
        self.frame_cima = Frame(self.jn_parametro, width=450, height=50, bg=self.corjn2, relief='flat')
        self.frame_cima.grid(row=0, column=0, pady=1, padx=1)

        self.frame_baixo = Frame(self.jn_parametro, width=450, height=450, bg=self.corjn2, relief='flat')
        self.frame_baixo.grid(row=1, column=0, pady=1, padx=1)

    def label_parametro(self):
        lab_nome = Label(self.frame_cima, text=" ", font=('Candara 30 bold  '), bg=self.corjn2,
                       fg=self.corjn3)
        lab_nome.place(x=160, y=1)

        lab_linha = Label(self.frame_cima, text=" ", width=800, font=('Candara 1'), bg=self.corjn2, fg=self.corjn3)
        lab_linha.place(x=0, y=45)
        # configurando frame de baixo
        # nomes em latim pra editar depois com os nomes reais dos parametros
        lab_nome0 = Label(self.frame_baixo, text=" ", font=('Candara 10 italic'),
                        bg=self.corjn2, fg=self.corlt4)
        lab_nome0.place(x=10, y=1)

        ent_nome1 = Entry(self.frame_baixo, width=16, justify='center', bg=self.corjn2, font=("", 15), highlightthickness=1,
                        relief='flat')
        ent_nome1.place(x=40, y=71)
        ent_nome1.insert(0, "VALOR DE ENTRADA")
        ent_nome1.bind("<FocusIn>", lambda args: ent_nome1.delete('0', 'end'))
        ent_nome1.config(fg=self.corjn3, insertbackground=self.corjn3)
        ent_nome1.config(font= self.fontecandara2)



        ent_nome2 = Entry(self.frame_baixo, width=16, justify='center', bg=self.corjn2, font=("", 15), highlightthickness=1,
                        relief='flat')
        ent_nome2.place(x=240, y=71)
        ent_nome2.insert(0, "VALOR DA BANCA")
        ent_nome2.bind("<FocusIn>", lambda args: ent_nome2.delete('0', 'end'))
        ent_nome2.config(fg=self.corjn3, font= self.fontecandara2, insertbackground=self.corjn3)
        ent_nome2.config(state="disabled", disabledbackground=self.corjn2, disabledforeground=self.corjn)




        lista = ('BITCOIN - BTC', 'ETHEREUM - ETH', 'TETHER - USDT', 'BNB - BNB', 'USD COIN - USDT', 'CARDANO - ADA',
                 'SOLANA - SOL',
                 'XRP - XRP', 'POLKADOT - DOT', 'DOGE COIN - DOGE', 'TERRA - LUNA', 'AVALANCHE - AVAX',
                 'BINANCE USD - BUSD', 'POLYGON - MATIC',
                 'SHIBA INU - SHIB', 'TERRA USD - UST', 'CRYPTO.COM COIN - CRO', 'WRAPPED COIN - WBTC', 'DAI - DAI',
                 'COSMOS - ATOM')
        lab_nome3 = Label(self.frame_baixo, text="ATIVOS", font=('Candara 15 bold italic'), bg=self.corjn2,
                          fg=self.corjn3)
        lab_nome3.place(x=245, y=275)
        self.entipo1 = ttk.Combobox(self.frame_baixo, width=10,font=self.fontecandara,values=lista, validate='key')



        self.entipo1.place(x=245, y=300)




        lab_nome4 = Label(self.frame_baixo, text="TIMEFRAME", font=('Candara 15 bold italic'), bg=self.corjn2, fg=self.corjn3)
        lab_nome4.place(x=40, y=275)

        # -------------------------------Combobox com a lista de timeframes
        lista = ('H1', 'H4', 'DIARIO','D1', 'WE')
        self.entipo = ttk.Combobox(self.frame_baixo, width=10,font=self.fontecandara, values=lista, validate='key')
        self.entipo.place(x=40, y=300)







        ent_nome5 = Entry(self.frame_baixo, width=34, justify='center', bg=self.corjn2, font=("", 15), highlightthickness=1,
                          relief='flat')
        ent_nome5.place(x=40, y=110)

        ent_nome5.insert(0, "LIMITE DE GANHO")
        ent_nome5.bind("<FocusIn>", lambda args: ent_nome5.delete('0', 'end'))
        ent_nome5.config(fg=self.corjn3, font=self.fontecandara2, insertbackground=self.corjn3)


        ent_nome6 = Entry(self.frame_baixo, width=34, justify='center', bg=self.corjn2, font=("", 15), highlightthickness=1,
                        relief='flat')
        ent_nome6.place(x=40, y=150)
        ent_nome6.insert(0, "TEMPO")
        ent_nome6.bind("<FocusIn>", lambda args: ent_nome6.delete('0', 'end'))
        ent_nome6.config(fg=self.corjn3, font=self.fontecandara2, insertbackground=self.corjn3)



        ent_nome7 = Entry(self.frame_baixo, width=34, justify='center', bg=self.corjn2, font=("", 15), highlightthickness=1,
                        relief='flat')
        ent_nome7.place(x=40, y=190)
        ent_nome7.insert(0, "QUANTIDADE DE ORDEM")
        ent_nome7.bind("<FocusIn>", lambda args: ent_nome7.delete('0', 'end'))
        ent_nome7.config(fg=self.corjn3, font=self.fontecandara2, insertbackground=self.corjn3)


        ent_pass = Entry(self.frame_baixo, width=34, justify='center', bg=self.corjn2, font=("", 15), highlightthickness=1,
                       relief='flat')
        ent_pass.place(x=40, y=230)
        ent_pass.insert(0, "URL API")
        ent_pass.bind("<FocusIn>", lambda args: ent_pass.delete('0', 'end'))
        ent_pass.config(fg=self.corjn3, font=self.fontecandara2, insertbackground=self.corjn3)




    def button_parametro(self):
        self.btn_confirmar = Button(self.frame_baixo, text='CONFIRMAR', width=25, height=2, font=("Candara 10 bold"),
                                  bg=self.corjn3, fg='black', relief=GROOVE, overrelief=GROOVE)
        self.btn_confirmar.place(x=140, y=370)

if __name__ == "__main__":
    Param()