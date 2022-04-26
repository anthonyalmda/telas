from plotly.graph_objects import Figure,Candlestick
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc



class graficos:
    def grafar(self, par, time, velas):
        dados = self.historico(par=par, time=time, velas=velas)
        # dados.set_index('data', inplace=True)
        print(dados)
        fig = Figure(data=[Candlestick(x=dados['data'], open=dados['open'],
                                       high=dados['high'],
                                       low=dados['low'],
                                       close=dados['close']
                                       )])
        fig.update_layout(title="Teste de grafia ")
        fig.show()
    def grafa2(self, par, time, velas):
        dados = self.historico(par=par, time=time, velas=velas)
        # dados['data'] = dados['data'].map(mdates.date2num())
        # ++print(dados)
        ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
        ax1.xaxis_date()
        candlestick_ohlc(ax1, dados.values, width=2, colorup='g', colordown='r')
