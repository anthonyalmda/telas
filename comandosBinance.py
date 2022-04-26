from binance.client import Client
from binance.enums import *


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
    def desativa(self):
        self.cliente.close_connection()
        #self.cliente.d
    def moedas(self,filtro = True):
        self.ativa(chave=self.chave_api,senha=self.senha_api)
        self.info = self.cliente.get_account()
        self.lista = self.info['balances']
        self.desativa()
        df = DataFrame(self.lista)
        df['free'] = df['free'].astype('float')
        if filtro:
            df = df[df['free'] > 0]
        df.rename(columns={'asset':'ativo','free':'valor','locked':'bloqueado'}, inplace=True)
        return df
    def compra(self,quantidade,par):
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
    def venda(self,qtd_venda,moeda):
        self.ativa(chave=self.chave_api,senha=self.senha_api)
        ordem = self.cliente.create_order(
            symbol=moeda,
            side=SIDE_SELL,
            type=ORDER_TYPE_MARKET,
            quantity=qtd_venda
        )                               # ordem de Venda enviada a Binance
        self.desativa()
    def converte(self, origem,destino, vlmoeda=0 , capital=0):
        self.ativa(chave=self.chave_api,senha=self.senha_api)
        valor = self.cotacao(origem+destino)
        self.desativa()
        if vlmoeda == 0 and capital == 0:
            return 0
        resutado = 0
        if capital != 0:
            resutado = capital*valor
        return resutado
    def historico(self,par,time,velas=10):
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
