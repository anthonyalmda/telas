from dados import Dados
from tkinter import messagebox
from comandosBinance import Bnbcomand


class Operacional(Dados, Bnbcomand):
    def testaparescompra(self,diferenca,time):
        """
        Funcão de teste de possível entrada
        :param diferenca: tamanho da vela de fuga para considerar armar a operação
        :param time: timeframe da operação
        :return:
        """
        time = time.upper()         #ajusta o valor passado para caixa alta
        #criar o dataframe com as informações da tabela
        df = self.geradf('ativos','*',('cliente', 'moeda_Base', 'moeda_compra', 'cod_opera', 'lote'), chave='cliente', vlchave=f'{self.cliente}')
        # varredura do dataframe
        for x in range(len(df)):
            ativo = df.loc[x, 'moeda_Base']+df.loc[x, 'moeda_compra']  # pega o par de moedas para avaliação
            cod_opera = df.loc[x, 'cod_opera']
            teste = self.testevela(par=ativo,time=time,velas=4)  # gerar dataframe com o teste de validação da vela
            #self.desativa()
            valido = True
            if teste.loc[1,'teste']==True:   # verifica se com 1 cadlestick já atinge o ponto de fuga
                vl_velaindefinida = teste.loc[1,'close']-teste.loc[1,'open']
                ponto_compra =  teste.loc[1,'high']
                if vl_velaindefinida < 0:
                    vl_velaindefinida *= -1
                vl_velafuga = teste.loc[2,'close']-teste.loc[2,'open']
                if (vl_velaindefinida*diferenca) <= vl_velafuga:
                    valido = False

            if valido and teste.loc[0,'teste']==True:  # Caso o teste anterior não tenha sido válido, verifica se com 2 cadlestick atinge o ponto de fuga
                vl_velaindefinida = teste.loc[0,'close']-teste.loc[0,'open']
                ponto_compra =  teste.loc[0,'high']
                if vl_velaindefinida < 0:
                    vl_velaindefinida *= -1
                vl_velafuga = teste.loc[2,'close']-teste.loc[1,'open']

            if teste.loc[0,'teste'] == True or teste.loc[1,'teste'] == True:  #
                if (vl_velaindefinida*diferenca) <= vl_velafuga:  # Se a fuga for adequada grava na tabela para aguardar o ponto de entrada
                    if not self.ptab(operacao='p', tabela='operacoes',
                                     chave=('ativo','preco_abertura'), vlchave=(cod_opera,ponto_compra)):  # Testa se esse ponto já foi gravado
                        valorc = (f"'{cod_opera}','{ponto_compra}'")
                        self.ptab(operacao='C', tabela='operacoes', campos='(ativo,preco_abertura)', valores=valorc)  # grava o registro na tabela

    def testacompra(self, par, valor):
        if valor >= self.cotacao(par=par):
            messagebox(f'o par {par} encontra-se no preço de compra valor: {valor}')
            return True
        return False

