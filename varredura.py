from tkinter import Tk, Button, Label, DISABLED, ACTIVE
from operacional import Operacional
from datetime import datetime
from msgtelegram import Telegram
from bancomysq import Operacoes, EntradasAbertas, Historico, Ativos, Cliente
from concurrent.futures import ThreadPoolExecutor

class Varredura(Operacional,Telegram):
    def __init__(self, timeframe):
        self.timeframe = timeframe
        self.contador = 0
        self.contador2 = 0
        self.sair = False
        self.padroes()
        self.telavarredura = Tk()
        self.janelavarredura()
        self.telavarredura.mainloop()

    def janelavarredura(self):
        self.telavarredura.title('Busca ativa do sistema')
        self.telavarredura.geometry('700x400+400+200')
        self.telavarredura.configure(bg=self.corjn2)
        self.lab_conta = Label(self.telavarredura, text=self.contador, font=self.fonte16, bg=self.corjn2, fg=self.corlt1)
        self.lab_conta.place(x=200, y=10)
        self.lab_conta2 = Label(self.telavarredura, text=self.contador2, font=self.fonte16, bg=self.corjn2, fg=self.corlt1)
        self.lab_conta2.place(x=200, y=80)
        self.varre_buton()

    def varre_buton(self):
        self.btn_iniciar = Button(self.telavarredura, text='Iniciar', command=self.inicio)
        self.btn_iniciar.place(x=600, y=1)
        self.btn_sair = Button(self.telavarredura, text='Sair', command=self.sairfunc)
        self.btn_sair.place(x=600, y=40)

    def inicio(self):
        self.sair = False
        self.btn_iniciar.configure(state=DISABLED)
        exe = ThreadPoolExecutor(max_workers=1)
        resposta = exe.map(self.pesquisa_oportunidades, self.timeframe)

    def pesquisa_oportunidades(self,time):
        #import ipdb ; ipdb.set_trace()
        dt_testehora = ''
        while True:
            if self.sair:
                print('Botão sair foi pressionado pesquisa encerrada')
                break
            dt_data = str(datetime.now())[0:10]
            dt_dia = int(dt_data[8:])
            dt_hora = int(str(datetime.now())[11:13])
            if self.timeframe == 'H1':
                if dt_hora != dt_testehora:
                    dt_testehora = dt_hora
                    self.contador += 1
                    self.lab_conta.configure(text=self.contador)
                    self.testaparescompra(3, 'h4', self.vl_cliente)
            elif self.timeframe == 'H4':
                if int(dt_hora)%4 == 0 and dt_hora != dt_testehora:
                    dt_testehora = dt_hora
                    self.contador += 1
                    self.lab_conta.configure(text=self.contador)
                    self.testaparescompra(0, 'h4', self.vl_cliente)
            #self.testaparescompra(3, 'h1', self.vl_cliente)
            self.contador2 += 1
            self.lab_conta2.configure(text=self.contador2)

            self.pesquisa_entradas()

    def pesquisa_entradas(self):
        for x in Operacoes.select().where(Operacoes.aberto == 0):
            ativo = Ativos.select().where(Ativos.cod_opera == x.cod_opera).get()
            par = ativo.moeda_base + ativo.moeda_compra
            preco = float(x.preco_abertura)
            if preco >= self.cotacao(par) and x.aberto == 0:
                cliente = Cliente.get(Cliente.cod_cli == self.cliente)
                print(preco, self.cotacao(par))
                print(f'a operação é: {x.operacao} \ne o código da operação é: {x.cod_opera}')
                self.send_mensage(f'Comprar o par {par} \n Valor de compra {preco}')
                atualiza = Operacoes.update(datahoraabertura=datetime.now(),
                                            aberto=1).where(
                    (Operacoes.cod_opera == x.cod_opera) & (Operacoes.preco_abertura == preco))
                atualiza.execute()
                EntradasAbertas.create(opeacao=int(x.operacao),
                                       code_opera=int(x.cod_opera),
                                       preco_abertura=x.preco_abertura,
                                       abertura=x.datahoraabertura,
                                       alvo=str(float(x.preco_abertura)*(1+(cliente.margem_lucro/100))))

                # linha_excluir = Operacoes.get(Operacoes.operacao == x.operacao)
                # linha_excluir.delete_instance()

    def teste_fechamento(self):  #Testa se uma operação atingiu o alvo e a encerra
        for x in EntradasAbertas.select():
            par = Ativos.get(Ativos.cod_opera==x.cod_opera)
            if x.alvo <= self.cotacao(par):
                atualiza = Historico.create(abertura=x.datahoraabertura,
                                            operacao=x.operacao,
                                            cod_opera=x.cod_opera,
                                            fechamento=datetime.now(),
                                            preco_fechamento=str(self.cotacao(par)))

    def sairfunc(self):
        self.sair = True
        self.btn_iniciar.configure(state=ACTIVE)
