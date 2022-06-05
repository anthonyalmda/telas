from tkinter import Tk, Button, Label, DISABLED, ACTIVE
from time import sleep
from operacional import Operacional
from datetime import datetime
from msgtelegram import Telegram
from bancomysq import Operacoes, EntradasAbertas, Historico, Ativos, Cliente
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

class Varredura(Operacional,Telegram):
    def __init__(self, timeframe):
        self.timeframe = timeframe
        self.dt_testehora = ''
        self.contador = 0
        self.contador2 = 0
        self.contador3 = 0
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
        self.lab_conta3 = Label(self.telavarredura, text=self.contador3, font=self.fonte16, bg=self.corjn2, fg=self.corlt1)
        self.lab_conta3.place(x=200, y=150)
        self.varre_buton()

    def varre_buton(self):
        self.btn_iniciar = Button(self.telavarredura, text='Iniciar', command=self.inicio)
        self.btn_iniciar.place(x=600, y=1)
        self.btn_sair = Button(self.telavarredura, text='Sair', command=self.sairfunc)
        self.btn_sair.place(x=600, y=40)

    def inicio(self):
        self.sair = False
        self.btn_iniciar.configure(state=DISABLED)

        exe2 = ThreadPoolExecutor(max_workers=1)
        exe2.map(self.pesquisa_oportunidades, self.timeframe)

    def sairfunc(self):
        self.sair = True
        self.btn_iniciar.configure(state=ACTIVE)

    def pesquisa_oportunidades(self, time):
        #import ipdb ; ipdb.set_trace()
        pesquisa_entrada = True
        while True:
            if pesquisa_entrada:
                exe1 = ThreadPoolExecutor(max_workers=1)
                exe1.submit(self.pesquisa_entradas, self.timeframe)
                pesquisa_entrada = False
            if self.sair:
                print('Botão sair foi pressionado pesquisa encerrada')
                break
            dt_data = str(datetime.now())[0:10]
            dt_dia = int(dt_data[8:])
            dt_minuto = int(str(datetime.now())[15:18])
            print(f' esse é o minuto atual: {dt_minuto}')
            # if dt_minuto != self.dt_testehora:
            #     self.dt_testehora = dt_minuto
            #     self.contador += 1
            #     self.lab_conta.configure(text=self.contador)
            #     self.testaparescompra(3, 'h1', self.vl_cliente)
            #sleep(0.5)

    def pesquisa_entradas(self, time):
        while True:
            exe3 = ThreadPoolExecutor(max_workers=1)
            exe3.submit(self.teste_fechamento, self.timeframe)
            if self.sair:
                print('Botão sair foi pressionado pesquisa entradas encerrada')
                break
            self.contador2 += 1
            self.lab_conta2.configure(text=self.contador2)
            for x in Operacoes.select():
                ativo = Ativos.select().where(Ativos.cod_opera == x.cod_opera).get()
                par = ativo.moeda_base + ativo.moeda_compra
                preco = float(x.preco_abertura)
                if preco >= self.cotacao(par) and x.aberto == 0:
                    cliente = Cliente.get(Cliente.cod_cli == self.cliente)
                    print(preco, self.cotacao(par))
                    print(f'a operação é: {x.operacao} \ne o código da operação é: {x.cod_opera}')
                    self.send_mensage(f'-------------------------------------------------------')
                    self.send_mensage(f'Comprar o par {par} \n Valor de compra {preco}')
                    self.send_mensage(f'-------------------------------------------------------')
                    atualiza = Operacoes.update(datahoraabertura=datetime.now(),
                                                aberto=1).where(
                        (Operacoes.cod_opera == x.cod_opera) & (Operacoes.preco_abertura == preco))
                    atualiza.execute()
                    entrada = EntradasAbertas(opeacao=int(x.operacao),
                                           code_opera=int(x.cod_opera),
                                           preco_abertura=x.preco_abertura,
                                           abertura=x.datahoraabertura,
                                           alvo=str(float(x.preco_abertura)*(1+(cliente.margem_lucro/100))))
                    entrada.operacao = int(x.operacao)
                    entrada.cod_opera = int(x.cod_opera)
                    entrada.save()
                # linha_excluir = Operacoes.get(Operacoes.operacao == x.operacao)
                # linha_excluir.delete_instance()

    def teste_fechamento(self, time):  #Testa se uma operação atingiu o alvo e a encerra
        self.contador3 += 1
        self.lab_conta3.configure(text=self.contador3)
        for x in EntradasAbertas.select():
            ativo = Ativos.select().where(Ativos.cod_opera == x.cod_opera).get()
            par = ativo.moeda_base + ativo.moeda_compra
            preco = float(x.preco_abertura)
            #par = Ativos.get(Ativos.cod_opera==x.cod_opera)
            if x.alvo <= self.cotacao(par):
                self.send_mensage(f'-------------------------------------------------------')
                self.send_mensage(f'Vender o par {par} \n Valor de compra {preco}\n operação concluida com exito')
                self.send_mensage(f'-------------------------------------------------------')
                atualiza = Historico(abertura=x.datahoraabertura,
                                            operacao=x.operacao,
                                            cod_opera=x.cod_opera,
                                            fechamento=datetime.now(),
                                            preco_fechamento=str(self.cotacao(par)))
                atualiza.save()

