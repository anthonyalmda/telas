from binance.client import Client
from binance.enums import *
from plotly.graph_objects import Figure,Candlestick
import matplotlib.pyplot as plt
import matplotlib.pyplot as fig
from mplfinance.original_flavor import candlestick_ohlc


#import cufflinks as cf
from pandas import DataFrame, to_datetime
#from plotly import init_notebook_mode
#init_notebook_mode(connected=True)
#cf.go_offline()
class Bnbcomand:
    def ativa(self, chave, senha):
        self.chave = chave
        self.senha = senha
        self.cliente = Client(api_key=self.chave, api_secret=self.senha) # faz a conexão com a binance
    def moedas(self,filtro = True):
        self.info = self.cliente.get_account()
        self.lista = self.info['balances']
        df = DataFrame(self.lista)
        df['free'] = df['free'].astype('float')
        if filtro:
            df = df[df['free'] > 0]
        df.rename(columns={'asset':'ativo','free':'valor','locked':'bloqueado'}, inplace=True)
        return df
    def compra(self,quantidade,par):
        ordem = self.cliente.create_order(
            symbol=par,
            side=SIDE_BUY,
            type=ORDER_TYPE_MARKET,
            quantity=quantidade
        )                               # ordem de compra enviada a Binance
        for item in ordem:
            print(item)
        return ordem
    def venda(self,qtd_venda,moeda):
        ordem = self.cliente.create_order(
            symbol=moeda,
            side=SIDE_SELL,
            type=ORDER_TYPE_MARKET,
            quantity=qtd_venda
        )                               # ordem de Venda enviada a Binance
    def converte(self, origem,destino, vlmoeda=0 , capital=0):
        valor = self.cotacao(origem+destino)
        if vlmoeda == 0 and capital == 0:
            return 0
        resutado = 0
        if capital != 0:
            resutado = capital*valor
        return resutado
    def historico(self,par,time,velas=10):
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
        df = DataFrame(lista,columns=['data','open','high','low','close','5','6','7','8','9','10','11'])
        #df['data'] = to_datetime(df['data'], unit='ms')
        df['open'] = df['open'].astype('float')
        df['close'] = df['close'].astype('float')
        df['high'] = df['high'].astype('float')
        df['low'] = df['low'].astype('float')
        #df['volume'] = df['volume'].astype('float')
        return df.drop(['5','6','7','8','9','10','11'], axis=1)
    def cotacao(self,par):
        lista = self.cliente.get_recent_trades(symbol=par)
        return float(lista[-1]['price'])
    def testevela(self,par,time,velas):
        df = self.historico(par,time=time,velas=velas)
        df['candr'] = (df['high'] - df['low'])
        df['bodyr'] = (df['open'] - df['close'])
        df['borat'] = df['bodyr']*100/ df['candr']
        df['teste'] = False
        df = df.drop(['candr','bodyr'], axis=1)
        for x in range(df.count()[1]):
            if (df['borat'][x] > -50) and (df['borat'][x] < 50):
                df.loc[x, 'teste'] = True

        return df
    def grafar(self,par,time,velas):
        dados = self.historico(par=par,time=time,velas=velas)
        #dados.set_index('data', inplace=True)
        print(dados)
        fig = Figure(data=[Candlestick(x=dados['data'], open=dados['open'],
                                        high=dados['high'],
                                        low=dados['low'],
                                       close=dados['close']
                                             )])
        fig.update_layout(title="Teste de grafia ")
        fig.show()
    def grafa2(self,par,time,velas):
        dados = self.historico(par=par,time=time,velas=velas)
        #dados['data'] = dados['data'].map(mdates.date2num())
        #++print(dados)
        ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
        ax1.xaxis_date()
        candlestick_ohlc(ax1, dados.values, width=2, colorup='g', colordown='r')
