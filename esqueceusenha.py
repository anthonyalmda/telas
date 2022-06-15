from tkinter import Toplevel, Tk, Entry
from tkinter import Label, Frame, Entry, Button, RAISED, RIDGE, GROOVE, ttk
from apoio import Apoio
from login import Login



class Esqueceu(Apoio):
    def __init__(self):
        self.jn_esqueceu = Tk()
        self.padroes()
        self.tela_parametro()
        self.jn_esqueceu.mainloop()

    def tela_parametro(self):
        self.jn_esqueceu.title('PEDIDO DE MUDANÇA DE SENHA')
        self.jn_esqueceu.geometry('450x500')
        self.jn_esqueceu.configure(background=self.corjn2)
        self.jn_esqueceu.resizable(width=False, height=False)
        self.frame_esqueceu()
        self.label_esqueceu()
        self.button_esqueceu()

    def frame_esqueceu(self):
        self.frame_cima = Frame(self.jn_esqueceu, width=450, height=50, bg=self.corjn2, relief='flat')
        self.frame_cima.grid(row=0, column=0, pady=1, padx=1)

        self.frame_baixo = Frame(self.jn_esqueceu, width=450, height=450, bg=self.corjn2, relief='flat')
        self.frame_baixo.grid(row=1, column=0, pady=1, padx=1)

    def label_esqueceu(self):
        ent_nome1 = Entry(self.frame_baixo, width=19, justify='center', bg=self.corjn2, font=("", 15),
                          highlightthickness=1,
                          relief='flat')
        ent_nome1.place(x=40, y=220)
        ent_nome1.insert(0, "NÚMERO CADASTRADO")
        ent_nome1.bind("<FocusIn>", lambda args: ent_nome1.delete('0', 'end'))
        ent_nome1.config(fg=self.corjn3, insertbackground=self.corjn3)
        ent_nome1.config(font=self.fontecandara3)


        ent_nome2 = Entry(self.frame_baixo, width=18, justify='center', bg=self.corjn2, font=("", 15), highlightthickness=1,
                        relief='flat')
        ent_nome2.place(x=245, y=220)
        ent_nome2.insert(0, "EMAIL CADASTRADO")
        ent_nome2.bind("<FocusIn>", lambda args: ent_nome2.delete('0', 'end'))
        ent_nome2.config(fg=self.corjn3, font= self.fontecandara3, insertbackground=self.corjn3)


        ent_nome3 = Entry(self.frame_baixo, width=35, justify='center', bg=self.corjn2, font=("", 15), highlightthickness=1,
                          relief='flat')
        ent_nome3.place(x=40, y=260)

        ent_nome3.insert(0, "NOVA SENHA")
        ent_nome3.bind("<FocusIn>", lambda args: ent_nome3.delete('0', 'end'))
        ent_nome3.config(fg=self.corjn3, font=self.fontecandara2, insertbackground=self.corjn3)


        ent_nome4: Entry = Entry(self.frame_baixo, width=35, justify='center', bg=self.corjn2, font=("", 15), highlightthickness=1,
                        relief='flat')
        ent_nome4.place(x=40, y=300)
        ent_nome4.insert(0, "CONFIRMAR NOVA SENHA")
        ent_nome4.bind("<FocusIn>", lambda args: ent_nome4.delete('0', 'end'))
        ent_nome4.config(fg=self.corjn3, font=self.fontecandara2, insertbackground=self.corjn3)

    def button_esqueceu(self):
        self.btn_confirmar = Button(self.frame_baixo, text='ENVIAR DADOS', width=25, height=2, font=("Candara 10 bold"),
                                  bg=self.corjn3, fg='black', relief=GROOVE, overrelief=GROOVE)
        self.btn_confirmar.place(x=140, y=370)

if __name__ == "__main__":
    Esqueceu()


