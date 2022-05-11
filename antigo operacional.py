from dados import Dados
from tkinter import messagebox
from datetime import datetime
from comandosBinance import Bnbcomand
from threading import Event, Thread
from queue import Queue
#from functions import target
event = Event()
fila = Queue(maxsize=10000)


class Operacional(Dados, Bnbcomand):
    def testaparescompra(self, vl_diferenca, st_time_teste):
        """
        Funcão de teste de possível entrada
        :param vl_diferenca: tamanho da vela de fuga para considerar um operação
        :param time: timeframe da operação
        :return:
        """
        st_time_teste = st_time_teste.upper()         #ajusta o valor passado para caixa alta
        #criar o dataframe com as informações da tabela
        df_tabela = self.geradf('ativos','*',('cliente', 'moeda_Base', 'moeda_compra', 'cod_opera', 'lote'), chave='cliente', vlchave=f'{self.cliente}')
        # varredura do dataframe
        for x in range(len(df_tabela)):
            st_ativo = df_tabela.loc[x, 'moeda_Base']+df_tabela.loc[x, 'moeda_compra']  # pega o par de moedas para avaliação
            vl_cod_opera = df_tabela.loc[x, 'cod_opera']
            event.set()
            fila.put([st_ativo, st_time_teste])
        fila.put('Kill')
        self.target = self.pipeline(self.pega_ativo, self.testa_ativo)
        ths = self.pool(3)
        [th.start() for th in ths]
        [th.join() for th in ths]
    def pega_ativo(self, arg):
        st_ativo, st_time_teste = arg
        df_teste = self.testevela(par=st_ativo, time=st_time_teste, velas=4)  # gerar dataframe com o teste de validação da vela
        lo_valido = True
        vl_velaindefinida = vl_velafuga = vl_ponto_compra = 0
        if df_teste.loc[1, 'teste'] == True:  # verifica se com 1 cadlestick já atinge o ponto de fuga
            vl_velaindefinida = float(df_teste.loc[1, 'close']) - float(df_teste.loc[1, 'open'])
            vl_ponto_compra = df_teste.loc[1, 'high']
            if vl_velaindefinida < 0:
                vl_velaindefinida *= -1
            vl_velafuga = float(df_teste.loc[2, 'close']) - float(df_teste.loc[2, 'open'])
            if (vl_velaindefinida * vl_diferenca) <= vl_velafuga:
                lo_valido = False
        return df_teste, lo_valido, vl_velaindefinida,vl_velafuga,vl_cod_opera,vl_diferenca, vl_ponto_compra

    def testa_ativo(self,arg):
        df_teste,lo_valido,vl_velaindefinida,vl_velafuga,vl_cod_opera,vl_diferenca, vl_ponto_compra = arg
        #import ipdb; ipdb.set_trace()
        if lo_valido and df_teste.loc[0, 'teste'] == True:  # Caso o teste anterior não tenha sido válido, verifica se com 2 cadlestick atinge o ponto de fuga
            vl_velaindefinida = float(df_teste.loc[0, 'close']) - float(df_teste.loc[0, 'open'])
            vl_ponto_compra = float(df_teste.loc[0, 'high'])
            if vl_velaindefinida < 0:
                vl_velaindefinida *= -1
            vl_velafuga = float(df_teste.loc[2, 'close']) - float(df_teste.loc[1, 'open'])
        if df_teste.loc[0, 'teste'] == True or df_teste.loc[1, 'teste'] == True:  #
            if (
                    vl_velaindefinida * vl_diferenca) <= vl_velafuga:  # Se a fuga for adequada grava na tabela para aguardar o ponto de entrada
                if not self.ptab(operacao='p', tabela='operacoes', chave=('ativo', 'preco_abertura'),
                                 vlchave=(vl_cod_opera, f'{vl_ponto_compra}'),
                                 condicao=f'where ativo={vl_cod_opera} and preco_abertura={vl_ponto_compra}'):  # Testa se esse ponto já foi gravado
                    valorc = (f"'{vl_cod_opera}','{vl_ponto_compra}','{datetime.now()}'")
                    self.ptab(operacao='C', tabela='operacoes', campos='(ativo,preco_abertura,dataarma)',
                              valores=valorc)  # grava o registro na tabela

    def pipeline(self,*funcs):
        def inner(argument):
            state = argument
            for func in funcs:
                state = func(state)
        return inner
    def testacompra(self, st_par, vl_valor):
        if vl_valor >= self.cotacao(par=st_par):
            messagebox(f'o par {st_par} encontra-se no preço de compra valor: {vl_valor}')
            return True
        return False

    def pool(self, instacias:int):
        """ Esta função cria um pool de threads de forma dinâmica"""
        return [Worker(target=self.target, queue=fila, name=f'trabalho {n}')
                for n in range(instacias)]

class Worker(Thread):  # Esta clase é utilizada para realiza operações em paralelo no sistema
    def __init__(self, target, queue, *, name='Worker'):
        super().__init__()
        self.name = name
        self.queue = queue
        self._target = target
        self._stoped = False
        print(self.name, 'Started')

    def run(self):
        event.wait()
        while not self.queue.empty():
            acao = self.queue.get()
            if acao == 'Kill':
                self.queue.put(acao)
                self.stoped = True
                break
            self._target(acao)

    def join(self):
        while not self._stoped:
            pass

