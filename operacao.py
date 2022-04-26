from dados import Dados
from tkinter import messagebox
from comandosBinance import Bnbcomand


class Operacional(Dados, Bnbcomand):
    def testaparescompra(self,diferenca,time):
        time = time.upper()
        df = self.geradf('ativos','*',['cliente','moeda_Base','moeda_compra','cod_opera','lote'])
        #print(df)
        for x in range(len(df)):
            ativo = df.loc[x,'moeda_Base']+df.loc[x,'moeda_compra']
            cod_opera = df.loc[x,'cod_opera']
            teste = self.testevela(par=ativo,time=time,velas=4)
            if teste.loc[1,'teste']==True:
                vl_velaindefinida = teste.loc[1,'close']-teste.loc[1,'open']
                ponto_compra =  teste.loc[1,'high']
                if vl_velaindefinida < 0:
                    vl_velaindefinida *= -1
                vl_velafuga = teste.loc[2,'close']-teste.loc[2,'open']
            elif teste.loc[0,'teste']==True:
                vl_velaindefinida = teste.loc[0,'close']-teste.loc[0,'open']
                ponto_compra =  teste.loc[0,'high']
                if vl_velaindefinida < 0:
                    vl_velaindefinida *= -1
                vl_velafuga = teste.loc[2,'close']-teste.loc[1,'open']
            if teste.loc[0,'teste'] == True or teste.loc[1,'teste'] == True:
                if (vl_velaindefinida*diferenca) <= vl_velafuga:
                    print(f'O par {ativo} está confirmado para operar {vl_velaindefinida,vl_velafuga}')
                    if not self.ptab(operacao='p', tabela='operacoes', chave=('cod_opera','preco_abertura'), vlchave=(cod_opera,ponto_compra)):
                        self.ptab(valores=())
                else:
                    print(f'O par {ativo} não tem diferença suficiente {vl_velaindefinida, vl_velafuga}')
            else:
                print(f'O par {ativo} não se encontra em indefinição')
        # self.desativa()
        # print(self.cotacao('BNBBRL'))

    def abreordem(self):
        pass
            #if df['preco_abertura'] == self.cotacao():
            #    valores = [df['preco_abertura'], True, datetime.now()]
            #    self.ptab(valores=valores, operacao='P', tabela='operacoes', campos=('preco_abertura','aberto','datahoraabertura'), chave='ativo', vlchave=df['ativo'])

    def carrega(self, par, valor):
        if valor == self.cotacao(par=par):
            messagebox(f'o par {par} encontra-se no preço de compra valor: {valor}')
            return True
        return False

    def varredura(self):
        pass
