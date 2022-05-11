from dados import Dados
from tkinter import messagebox
from datetime import datetime
from comandosBinance import Bnbcomand
#from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
from bancomysql import Ativos, Operacoes
from threading import Event, Thread
from queue import Queue
event = Event()
fila = Queue(maxsize=10000)


class Operacional(Dados, Bnbcomand):
    def __init__(self):
        self.padroes()
        #self.testaparescompra(0,'h1','003')
        # self.mys_con = self.abredb(hostc=self.host,bancoc=self.banco,usuarioc=self.usuario,senhac=self.senha,porta=3306)
        # self.cursor = self.mys_con.cursor()

    def testaparescompra(self, vl_diferenca, st_time_teste,cliente):
        """
        Funcão de teste de possível entrada
        :param vl_diferenca: tamanho da vela de fuga para considerar um operação
        :param time: timeframe da operação
        :return:
        """
        st_time_teste = st_time_teste.upper()         #ajusta o valor passado para caixa alta
        #criar o dataframe com as informações da tabela
        #df_tabela = self.geradf('ativos','*',('cliente', 'moeda_Base', 'moeda_compra', 'cod_opera', 'lote'), chave='cliente', vlchave=f'{self.cliente}')
        # varredura do dataframe
        lista=[]
        for x in Ativos.select().where(Ativos.cliente == cliente):
            st_ativo = x.moeda_base+x.moeda_compra
            vl_cod_opera = f'{x.cod_opera}'
            event.set()
            fila.put([st_ativo, vl_diferenca, st_time_teste, vl_cod_opera])
            lista += [[st_ativo, vl_diferenca, st_time_teste, vl_cod_opera]]
        #fila.put('Kill')
        self.target = self.pipeline(self.pega_ativo, self.testa_ativo)
        execucao = ThreadPoolExecutor(max_workers=5)
        resultado = execucao.map(self.target, lista)

        print('acabou')
        # ths = self.pool(3)
        # [th.start() for th in ths]
        # [th.join() for th in ths]
        # targete = Pipeline(self.pega_ativo, self.testa_ativo)
        # trabalho = Pool(5)
        # resposta = trabalho.map(targete, lista)

    def pega_ativo(self, arg):
        st_ativo,  vl_diferenca, st_time_teste,vl_cod_opera  = arg
        df_teste = self.testevela(par=st_ativo, time=st_time_teste, velas=4)  # gerar dataframe com o teste de validação da vela
        lo_valido = True
        vl_velaindefinida = vl_velafuga = vl_ponto_compra = 0
        print(f'passei pega ativo {st_ativo}')
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
        print(f'passei testa ativo {vl_cod_opera}')
        if df_teste.loc[0, 'teste'] == True or df_teste.loc[1, 'teste'] == True:  #
            print('entrei primeiro if')
            if (vl_velaindefinida * vl_diferenca) <= vl_velafuga:  # Se a fuga for adequada grava na tabela para aguardar o ponto de entrada
                print('entrei segundo if')
                vl_cod_opera = int(vl_cod_opera)
                p = Operacoes.select().where(Operacoes.ativo == vl_cod_opera and Operacoes.preco_abertura == vl_ponto_compra)
                if p.count() == 0:
                    Operacoes.create(
                        ativo=vl_cod_opera,
                        preco_abertura=str(vl_ponto_compra),
                        dataarma=datetime.now())
                    #salvar.save()
                    print(f'deveria ter salvo ')
                    # valorc = (f"'{vl_cod_opera}','{vl_ponto_compra}','{datetime.now()}'")
                    # self.ptab(operacao='C', tabela='operacoes', campos='(ativo,preco_abertura,dataarma)',
                    #           valores=valorc)  # grava o registro na tabela
                return True

    def testacompra(self, st_par, vl_valor):
        if vl_valor >= self.cotacao(par=st_par):
            messagebox(f'o par {st_par} encontra-se no preço de compra valor: {vl_valor}')
            return True
        return False

    # def pool(self, instacias:int):
    #     """ Esta função cria um pool de threads de forma dinâmica"""
    #     return [Worker(target=self.target, queue=fila, name=f'trabalho {n}')
    #             for n in range(instacias)]
    def pool(self, instacias:int):
        """ Esta função cria um pool de threads de forma dinâmica"""
        return [Worker(target=self.target, queue=fila, name=f'trabalho {n}')
                for n in range(instacias)]
    def pipeline(self,*funcs):
        def inner(argument):
            state = argument
            for func in funcs:
                state = func(state)
        return inner

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


class Pipeline:
    def __init__(self,*funcs):
        self.funcs= funcs
    def __call__(self, argument):
        state = argument
        for func in self.funcs:
            state = func(state)
        return state

if __name__ == '__main__':
    Operacional()