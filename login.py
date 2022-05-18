from tkinter import Toplevel, Tk
from tkinter import *
from tkinter import messagebox
from apoio import Apoio


class Login(Apoio):
    def __init__(self):
        self.jn_login = Tk()
        self.padroes()
        self.tela_login()
        self.jn_login.mainloop()

    def tela_login(self):
        self.jn_login.title('')
        self.jn_login.geometry('350x250')
        self.jn_login.configure(background=self.corjn)
        self.jn_login.resizable(width=False, height=False)
        self.frame_login()
        self.label_login()
        self.button_login()
        self.button_esqueceu()

    def frame_login(self):
        self.frame_cima = Frame(self.jn_login, width=350, height=50, bg=self.corjn, relief='flat')
        self.frame_cima.grid(row=0, column=0, pady=1, padx=1)

        self.frame_baixo = Frame(self.jn_login, width=350, height=300, bg=self.corjn, relief='flat')
        self.frame_baixo.grid(row=1, column=0, pady=1, padx=1)


    def label_login(self):
        l_nome = Label(self.frame_cima, text="LOGIN", font=('Candara 30 bold italic  '), bg=self.corjn, fg=self.corjn3)
        l_nome.place(x=125, y=1)

        l_linha = Label(self.frame_cima, text=" ", width=800, font=('Candara 1'), bg=self.corjn3, fg=self.corjn3)
        l_linha.place(x=0, y=45)

        l_nome0 = Label(self.frame_baixo, text=" ", font=('Candara 10 italic'),
                        bg=self.corjn, fg=self.corlt4)
        l_nome0.place(x=10, y=1)
        l_nome1 = Label(self.frame_baixo, text="USUÁRIO", font=('Candara 20 bold italic'), bg=self.corjn, fg=self.corjn3)
        l_nome1.place(x=35, y= 31)
        e_nome1 = Entry(self.frame_baixo, width=15, bg=self.corjn, font=("", 13), highlightthickness=1,
                        relief='sunken')
        e_nome1.place(x=155, y=40)



        l_pass = Label(self.frame_baixo, text="SENHA ", font=('Candara 20 bold italic'), bg=self.corjn, fg=self.corjn3)
        l_pass.place(x=35, y=71)
        e_pass = Entry(self.frame_baixo, width=15, bg=self.corjn, font=("", 13), highlightthickness=1,
                       relief='sunken')
        e_pass.place(x=155, y=81)


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
    def button_login(self):
        self.b_confirmar = Button(self.frame_baixo, text='CONFIRMAR',  width=15, height=2, font=('Candara 10 italic bold'),
                                  bg=self.corjn3, fg=self.corlt1, relief=FLAT, overrelief=RIDGE)
        self.b_confirmar.place(x=125, y=120)
    def button_esqueceu(self):
        self.b_confirmar = Button(self.frame_baixo, text='ESQUECEU A SENHA?', width=15, height=2,
                                  font=('Candara 7 italic bold'),
                                  bg=self.corjn, fg=self.corjn3, relief=FLAT, overrelief=RIDGE)
        self.b_confirmar.place(x=135, y=165)

if __name__ == "__main__":
    Login()