from binance.client import Client
from binance.enums import *
from apoio import Apoio
from pandas import DataFrame, to_datetime


class Bnbcomand(Apoio):
    def __init__(self):
        self.carrega()

    def ativa(self, chave, senha):
        """
        Ativa a conexão com a API da Binance
        :param chave: Chave API da Binance
        :param senha: Senha da chave API
        :return:
        """
        self.chave = chave
        self.senha = senha
        self.cliente = Client(api_key=self.chave, api_secret=self.senha) # faz a conexão com a binance

    def desativa(self): # Encerra a conexão com a API da Binance
        self.cliente.close_connection()
        #self.cliente.d

    def moedas(self,filtro = True):
        """
        Lista as moedas de negociação na corretora
        :param filtro: Se for especificado como True ou não for informado mostra apenas as moedas com saldo disponível
        :return: retorna um dataframe com a lista das moedas e seus saldos
        """
        self.ativa(chave=self.chave_api,senha=self.senha_api)  # Ativa a conexão com a API da Binance
        self.info = self.cliente.get_account()  # Pega a relação de dados da conta
        self.lista = self.info['balances']  # Seleciona apenas a listagem das moedas
        self.desativa()  # Encerra a conexão com a API
        df = DataFrame(self.lista)  # gera um dataframe com a lista de moedas
        df['free'] = df['free'].astype('float')  # converte a coluna em Float
        if filtro:  # Se a filtragem estiver ativa, filtra apenas as moedas com saldo
            df = df[df['free'] > 0]
        # Altera o nome das colunas do dataframe
        df.rename(columns={'asset': 'ativo', 'free': 'valor', 'locked': 'bloqueado'}, inplace=True)
        return df

    def compra(self, quantidade, par):
        self.ativa(chave=self.chave_api,senha=self.senha_api)
        ordem = self.cliente.create_order(
            symbol=par,
            side=SIDE_BUY,
            type=ORDER_TYPE_MARKET,
            quantity=quantidade
        )                               # ordem de compra enviada a Binance
        self.desativa()
        for item in ordem:
            print(item)
        return ordem

    def venda(self, qtd_venda, moeda):
        self.ativa(chave=self.chave_api,senha=self.senha_api)
        ordem = self.cliente.create_order(
            symbol=moeda,
            side=SIDE_SELL,
            type=ORDER_TYPE_MARKET,
            quantity=qtd_venda
        )                               # ordem de Venda enviada a Binance
        self.desativa()

    def converte(self, origem, destino, capital=0):
        """
        Faz o calculo do lote a ser comprado retornado o montante em criptomoeda a ser comprado
        :param origem: Moeda a ser utilizada para a compra
        :param destino: Moeda a ser comprada
        :param vlmoeda: valor da
        :param capital:
        :return:
        """
        if capital == 0:  # se não for passado o valor do lote a função retorna zero
            return 0
        self.ativa(chave=self.chave_api,senha=self.senha_api)  # Ativa a conexão com a API da Binance
        valor = self.cotacao(origem+destino)  # Pega a cotação atual da moeda
        self.desativa()  # Encerra a conexão com a API
        return capital / valor

    def historico(self,par,time,velas=10):
        """
        Gera um dataframe com a relação das ultimas velas por padrão 10
        :param par: Dupa de moedas a apresentar os resultados
        :param time: Timeframe das velas pode ser H1, H4, D1 ou WE
        :param velas:
        :return:
        """
        self.ativa(chave=self.chave_api,senha=self.senha_api)
        time = time.upper()
        par = par.upper()
        if time =='H1':
            timeframe = self.cliente.KLINE_INTERVAL_1HOUR
        elif time =='H4':
            timeframe = self.cliente.KLINE_INTERVAL_4HOUR
        elif time == 'D1':
            timeframe = self.cliente.KLINE_INTERVAL_1DAY
        elif time == 'WE':
            timeframe = self.cliente.KLINE_INTERVAL_1WEEK

        lista = self.cliente.get_klines(symbol=par,interval = timeframe, limit=velas)
        self.desativa()
        df = DataFrame(lista,columns=['data','open','high','low','close','5','6','7','8','9','10','11'])
        #df['data'] = to_datetime(df['data'], unit='ms')
        df['open'] = df['open'].astype('float')
        df['close'] = df['close'].astype('float')
        df['high'] = df['high'].astype('float')
        df['low'] = df['low'].astype('float')
        #df['volume'] = df['volume'].astype('float')
        return df.drop(['5','6','7','8','9','10','11'], axis=1)
    def cotacao(self,par):
        self.ativa(chave=self.chave_api,senha=self.senha_api)
        lista = self.cliente.get_recent_trades(symbol=par)
        self.desativa()
        return float(lista[-1]['price'])
    def testevela(self,par,time,velas):
        self.ativa(chave=self.chave_api,senha=self.senha_api)
        df = self.historico(par,time=time,velas=velas)
        self.desativa()
        df['candr'] = (df['high'] - df['low'])
        df['bodyr'] = (df['open'] - df['close'])
        df['borat'] = df['bodyr']*100/ df['candr']
        df['teste'] = False
        df = df.drop(['candr','bodyr'], axis=1)
        for x in range(df.count()[1]):
            if (df['borat'][x] > -50) and (df['borat'][x] < 50):
                df.loc[x, 'teste'] = True
        return df
