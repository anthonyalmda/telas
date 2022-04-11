from ComandosBinance import Bnbcomand
from apoio import Apoio
class CriptoBot(Apoio,Bnbcomand):
    def __init__(self):
        self.carrega()
        self.ativa(chave=self.chave_api,senha=self.senha_api)
        #teste = self.converte(origem='USDT',destino='BRL', capital=10)
        #teste = self.testevela('BNBBRL','h4',velas=15)
        self.grafar(par='BNBBRL',time='h4',velas=15)
if __name__=="__main__":
    root = CriptoBot()