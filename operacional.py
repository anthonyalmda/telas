from dados import Dados
from datetime import datetime
from comandosBinance import Bnbcomand
from bancomysq import Ativos, Operacoes
from concurrent.futures import ThreadPoolExecutor
from msgtelegram import Telegram


class Operacional(Dados, Bnbcomand, Telegram):
    def __init__(self):
        self.padroes()
        #self.bot = Telegram.iniciar()
        #self.testaparescompra(0,'h1','003')
        # self.mys_con = self.abredb(hostc=self.host,bancoc=self.banco,usuarioc=self.usuario,senhac=self.senha,porta=3306)
        # self.cursor = self.mys_con.cursor()

    def testaparescompra(self, vl_diferenca, st_time_teste,vl_cliente):
        """
        Funcão de teste de possível entrada
        :param vl_diferenca: tamanho da vela de fuga para considerar um operação
        :param st_time_teste: timeframe da operação
        :param vl_cliente: Código do cliente
        :return:
        """
        st_time_teste = st_time_teste.upper()         #ajusta o valor passado para caixa alta
        lista=[]
        for x in Ativos.select().where(Ativos.cliente == vl_cliente):  # carrela a lista de ativos para tratamento posterior paralelizado
            # print(f'entrei no for de testa compra e x vale: {x}')
            st_ativo = x.moeda_base+x.moeda_compra
            vl_cod_opera = f'{x.cod_opera}'
            lista += [[st_ativo, vl_diferenca, st_time_teste, vl_cod_opera]]
        funcao = Pipeline(self.pega_ativo, self.testa_ativo)
        executa = ThreadPoolExecutor(max_workers=3)
        resposta = executa.map(funcao, lista)


    def pega_ativo(self, arg):
        st_ativo,  vl_diferenca, st_time_teste, vl_cod_opera = arg
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
        if lo_valido and df_teste.loc[0, 'teste'] == True:  # Caso o teste anterior não tenha sido válido, verifica se com 2 cadlestick atinge o ponto de fuga
            vl_velaindefinida = float(df_teste.loc[0, 'close']) - float(df_teste.loc[0, 'open'])
            vl_ponto_compra = float(df_teste.loc[0, 'high'])
            if vl_velaindefinida < 0:
                vl_velaindefinida *= -1
            vl_velafuga = float(df_teste.loc[2, 'close']) - float(df_teste.loc[1, 'open'])

        return df_teste, lo_valido, vl_velaindefinida, vl_velafuga, vl_cod_opera, vl_diferenca, vl_ponto_compra, st_ativo

    def testa_ativo(self,arg):
        df_teste, lo_valido, vl_velaindefinida, vl_velafuga, vl_cod_opera, vl_diferenca, vl_ponto_compra, st_ativo = arg
        #import ipdb; ipdb.set_trace()
        if df_teste.loc[0, 'teste'] == True or df_teste.loc[1, 'teste'] == True:  #
            if (vl_velaindefinida * vl_diferenca) <= vl_velafuga:  # Se a fuga for adequada grava na tabela para aguardar o ponto de entrada
                vl_cod_opera = int(vl_cod_opera)
                print(f'entrei no if o cod_opera é: {vl_cod_opera} e o valor é: {vl_ponto_compra}')
                p = Operacoes.select().where(Operacoes.ativo == vl_cod_opera & (Operacoes.preco_abertura == vl_ponto_compra))
                print(f'o resultado do select é: {p.count()}')
                if p.count() == 0:
                    self.send_mensage(f'Oportunidade de compra foi armada para o par {st_ativo} \nValor de compra {vl_ponto_compra}')
                    Operacoes.create(
                        ativo=vl_cod_opera,
                        preco_abertura=str(vl_ponto_compra),
                        dataarma=datetime.now())
                return True

    # def pipeline(self,*funcs):
    #     print(f'entrei pipe e funcs é: {funcs}')
    #     def inner(argument):
    #         print(f'Entrei no inner e o argumento é: {argument}')
    #         state = argument
    #         for func in funcs:
    #             state = func(state)
    #     return inner

class Pipeline:
    def __init__(self,*funcs):
        self.funcs= funcs
    def __call__(self, argument):
        state = argument
        for func in self.funcs:
            state = func(state)
        return state

