import tkinter
from tkinter import Toplevel, Tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import base64
from PIL import ImageTk, Image


from apoio import Apoio





class Login(Apoio, tkinter.Tk):

    def __init__(self):
        self.jn_login = Tk()
        self.padroes()
        self.tela_login()
        self.jn_login.mainloop()




    def tela_login(self):
        self.jn_login.title('LOGIN')
        self.jn_login.geometry('450x500')
        self.jn_login.configure(background=self.corjn2)
        self.jn_login.resizable(width=False, height=False)
        self.frame_login()
        self.label_login()

        self.button_login()
        self.button_esqueceu()

    def frame_login(self):
        self.frame_cima = Frame(self.jn_login, width=450, height=200, bg=self.corjn2, relief='flat')
        self.frame_cima.grid(row=0, column=0, pady=1, padx=1)

        self.frame_baixo = Frame(self.jn_login, width=350, height=300, bg=self.corjn2, relief='flat')
        self.frame_baixo.grid(row=1, column=0, pady=1, padx=1)





    def imagelobinho (self):
        self.imglobinho = PhotoImage(data=base64.b64decode(self.imglobo))
        self.imglobinho = ImageTk.PhotoImage(self.imglobo)
        self.imagelobinho = self.imglobinho.subsample(4,4)
        self.imagelobinho = self.imglobinho.place(x=1, y=1, width = 10)
        label = Label(self.frame_cima, image=self.tkpic)
        label.pack()
    def label_login(self ):
        lab_nome = Label(self.frame_cima,   font=('Candara 30 bold italic  '), bg=self.corjn2, fg=self.corjn3)
        lab_nome.place(x=0, y=1)



        lab_linha = Label(self.frame_cima, text=" ", width=600, font=('Candara 1'), bg=self.corjn2, fg=self.corjn2)
        lab_linha.place(x=0, y=45)

        lab_nome = Label(self.frame_baixo, text=" ", font=('candara 10 italic'),
                        bg=self.corjn2, fg=self.corlt4)
        lab_nome.place(x=10, y=1)


        ent_nome = Entry(self.frame_baixo,width=15,justify='center' ,bg=self.corjn3,  font=("Candara bold italic", 25), fg= 'white',
                        relief='flat')
        ent_nome.configure(insertbackground=self.corjn2)
        ent_nome.place(x=45, y=50)
        ent_nome.insert(0, "Login")
        ent_nome.bind("<FocusIn>", lambda args: ent_nome.delete('0', 'end'))




        ent_pass = Entry(self.frame_baixo,width=15,justify='center', bg=self.corjn3, font=("Candara bold italic", 25),
                         fg= 'white',
                        relief='flat')
        ent_pass.configure(insertbackground=self.corjn2)
        ent_pass.place(x=45, y=120)
        ent_pass.insert(0, "Senha")


        ent_pass.bind("<FocusIn>", lambda args: ent_pass.delete('0', 'end'))


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
        self.btn_confirmar = Button(self.frame_baixo, text='CONFIRMAR',  width=15, height=2, font=('Candara 15 italic bold'),
                                  bg=self.corjn2, fg=self.corlt1, relief=FLAT, overrelief=FLAT)
        self.btn_confirmar.place(x=95, y=180)
    def button_esqueceu(self):
        self.btn_confirmar = Button(self.frame_baixo, text='ESQUECEU A SENHA?', width=15, height=2,
                                  font=('Candara 7 italic bold'),
                                  bg=self.corjn2, fg=self.corjn3, relief=FLAT, overrelief=FLAT)
        self.btn_confirmar.place(x=135, y=250)

if __name__ == "__main__":
    Login()
