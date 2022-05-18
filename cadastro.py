from tkinter import Toplevel, Tk
from tkinter import Label, Frame, Entry, Button, RAISED, RIDGE, ttk
from tkinter import messagebox
from apoio import Apoio


class Cadastro(Apoio):
    def __init__(self):
        self.jn_cadastro = Tk()
        self.padroes()
        self.tela_cadastro()
        self.jn_cadastro.mainloop()

    def tela_cadastro(self):
        self.jn_cadastro.title('')
        self.jn_cadastro.geometry('350x250')
        self.jn_cadastro.configure(background=self.corjn)
        self.jn_cadastro.resizable(width=False, height=False)
        self.frame_cadastro()
        self.label_cadastro()
        self.button_cadastro()

    def frame_cadastro(self):
        self.frame_cima = Frame(self.jn_cadastro, width=350, height=50, bg=self.corjn, relief='flat')
        self.frame_cima.grid(row=0, column=0, pady=1, padx=1)

        self.frame_baixo = Frame(self.jn_cadastro, width=350, height=300, bg=self.corjn, relief='flat')
        self.frame_baixo.grid(row=1, column=0, pady=1, padx=1)


    def label_cadastro(self):
        l_nome = Label(self.frame_cima, text="CADASTRO", font=('Candara 30 bold italic  '), bg=self.corjn, fg=self.corjn3)
        l_nome.place(x=80, y=1)

        l_linha = Label(self.frame_cima, text=" ", width=800, font=('Candara 1'), bg=self.corjn3, fg=self.corjn3)
        l_linha.place(x=0, y=45)

        l_nome0 = Label(self.frame_baixo, text=" ", font=('Candara 10 italic'),
                        bg=self.corjn, fg=self.corlt4)
        l_nome0.place(x=10, y=1)
        l_nome1 = Label(self.frame_baixo, text="EMAIL", font=('Candara 15 bold italic'), bg=self.corjn, fg=self.corjn3)
        l_nome1.place(x=1, y= 1)
        e_nome1 = Entry(self.frame_baixo, width=15, bg=self.corjn, font=("", 13), highlightthickness=1,
                        relief='solid')
        e_nome1.place(x=1, y=30)


        l_nome2 = Label(self.frame_baixo, text="SENHA", font=('Candara 15 bold italic'), bg=self.corjn,
                        fg=self.corjn3)
        l_nome2.place(x=1, y=61)
        e_nome2 = Entry(self.frame_baixo, width=15, bg=self.corjn, font=("", 13), highlightthickness=1,
                        relief='solid')
        e_nome2.place(x=1, y=90)


        l_nome2 = Label(self.frame_baixo, text="NOME DE USUÁRIO", font=('Candara 15 bold italic'), bg=self.corjn,
                        fg=self.corjn3)
        l_nome2.place(x=180, y=1)
        e_nome2 = Entry(self.frame_baixo, width=15, bg=self.corjn, font=("", 13), highlightthickness=1,
                        relief='solid')
        e_nome2.place(x=180, y=30)


        l_nome2 = Label(self.frame_baixo, text="CONTATO", font=('Candara 15 bold italic'), bg=self.corjn,
                        fg=self.corjn3)
        l_nome2.place(x=180, y=61)
        e_nome2 = Entry(self.frame_baixo, width=15, bg=self.corjn, font=("", 13), highlightthickness=1,
                        relief='solid')
        e_nome2.place(x=180, y=90)





    ##def verificar_senha(self):
     #  self.nome = e_nome0.get()
     #   self.senha = Entry.get()
        # credencial de teste
      #  self.credenciais = ['joao', '12345678']
        # credencial de teste
       # if self.nome == 'admin' and self.senha == 'admin':
         #   messagebox.showinfo('LOGIN', 'ACESSO CONCEDIDO')
        #elif self.credenciais[0] == self.nome and self.credenciais[1] == self.senha:
          #  messagebox.showinfo('Login', 'Acesso concedido, ' + self.credenciais[0])
        #else:
         #   messagebox.showwarning('ERRO', 'TENTE NOVAMENTE')

    #command = self.verificar_senha,
    def button_cadastro(self):
        self.b_confirmar = Button(self.frame_baixo, text='SALVAR',  width=15, height=2, font=('Candara 10 italic bold'),
                                  bg=self.corjn3, fg=self.corlt1, relief=RAISED, overrelief=RIDGE)
        self.b_confirmar.place(x=115, y=135)

if __name__ == "__main__":
    Cadastro()