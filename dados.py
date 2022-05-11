import mysql
from mysql.connector import Error
from pandas import DataFrame


class Dados():
    def __init__(self):
        self.padroes()

    def abredb(self,hostc,usuarioc,senhac,bancoc,porta):
        """
        Cria uma conexão com o banco de dados
        :param hostc: Hoste de conexão
        :param usuarioc: Usuário de conexão com o banco de dados
        :param senhac: Senha de conexão com o banco de dados
        :param bancoc: Nome do banco de dados a ser conectado
        :param porta: Porta de conexão com o banco de dados
        :return: Retorna verdadeiro caso a conexão seja bem sucedida
        """
        # Faz a conexão ao banco de dados MySQL
        conexao = mysql.connector.connect(host=hostc, port=porta, user=usuarioc, password=senhac, database=bancoc, autocommit=True, compress=True)
        if conexao.is_connected(): # testa se a conexão foi bem sucedida
            return conexao
        else:
            return False

    def fechadb(self,conexao):
        """
        Fecha a conexão com o banco de dados
        :param conexao: variavel de conexão com o banco
        :return:
        """
        if conexao.is_connected():  # Testa se a conexão ainda é válida
            #conexao.cursor.close()  # Encerra o cursor
            conexao.close()  # Encerra a conexão

    def geradf(self,tabela,colunas='*',cadecalho='',chave='', vlchave=''):
        """
        Gera um dataframe apartir de uma tabela do banco de dados podendo ser feito uma filtragem dos dados
        :param tabela: Nome da tabela onde sera extraido os dados
        :param colunas: se não informado pega todas as colunas da tabela
        :param cadecalho: titulo das colunas no dataframe
        :param chave: Campo para filtrar a tabela pode ser passada uma tupla com os campos a pesquisar
        :param vlchave: Valores para filtrar a tabela pode ser passada uma tupla com os valores da pesquisar
        :return:
        """
        condicao=''
        # avalia se existe condição e monta a pesquisa
        if type(chave) == str and chave != '':
            condicao += f'where {chave} = {vlchave}'
        elif chave != '':
            condicao += 'where '
            ct = 0
            for x in chave:
                condicao += f'{x} = {vlchave[ct]}'
                if ct < len(chave) - 1:
                    condicao += ' and '
                ct += 1
        print(f'select {colunas} from {tabela} {condicao}')
        self.cursor.execute(f'select {colunas} from {tabela} {condicao}') #executa a instrução no banco de dados
        df = self.cursor.fetchall() # Carrega as lishas retornadas pelo cursor
        self.fechadb(self.mys_con)
        return DataFrame(df, columns=cadecalho) # gera o dataframe e o retorna como resposta da função

    def ptab(self, valores='', operacao='P', tabela='', campos='', chave='', vlchave='', condicao=''):
        """
        função para operações em tabelas do banco de dados faz musca, alteração e cadastro
        :param valores: pode ser uma tupla com a relação de valores a serem lançados ou uma variavel simples
        :param operacao: tipo de operação a ser feito valores: A= Alterar, C= Cadastrar, E= excluir ou P= pesquisar
        :param tabela: tabela onde sera realizada a operação
        :param campos:  pode ser uma tupla com a relação de campos que seram afetados ou apenas um campo simples
        :param chave: campo para a pesquisa, pode ser passada uma tupla com os campos
        :param vlchave: valor procurado, pode ser passada uma tupla com os valores
        :return:
        """
        self.mys_con = self.abredb(hostc=self.host,bancoc=self.banco,usuarioc=self.usuario,senhac=self.senha,porta=3306)
        self.cursor = self.mys_con.cursor()
        operacao = operacao.upper() # joga o valor para caixa alta
        retorno = True
        sql = ''
        if condicao == '':
            teste_condicao = ''
            # Montagem da condição where-------------------------------
            if type(chave) == str and chave != '': # verifica se a chave é uma string e se está vazia
                teste_condicao += f'where {chave} = {vlchave}'  # so for string e não estiver vazia cria uma condição simples
            elif chave != '':
                teste_condicao = 'where '
                ct = 0
                for x in chave:  # Varre a tupla para a montagem da condição
                    teste_condicao += f'{x} = {vlchave[ct]}'
                    if ct < len(chave) - 1:
                        teste_condicao += ' and '
                    ct += 1
        else:
            teste_condicao = condicao
        # Testa o tipo de operação
        if operacao == 'C':  # se é um cadastro
            sql = f'insert into {tabela} {campos} values ({valores})'
        elif operacao == 'A': # se é uma alteração
            sql = f'update {tabela} set '
            cont = 0
            if type(valores)== tuple:
                for z in valores:
                    sql += f'{campos[cont]} = {z}'
                    if cont < len(campos)-1:
                        sql += ', '
                    cont += 1
            else:
                sql += f'{campos} = {valores}'
            sql += teste_condicao
        elif operacao == 'E': # se é uma exclusão
            sql = f'delete from {tabela} {teste_condicao};'
        elif operacao == 'P': # se é uma pesquisa
            sql = f'select * from {tabela} {teste_condicao}'
        print(sql)
        self.cursor.execute(sql) # Executa a instrução no banco de dados
        self.ptabret = self.cursor.fetchall()
        if operacao=='P':
            if self.cursor.rowcount == 0:
                retorno = False  # Se a pesquisa não encontrar nada retorna Falso
            self.fechadb(self, self.mys_con)
        return retorno
        # except Error:
        #     print(F'Ocorreu o erro: {Error}')
