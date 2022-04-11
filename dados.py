import mysql.connector
from mysql.connector import Error
from pandas import DataFrame
from tkinter import messagebox

class Dados():
    def __init__(self):
        self.padroes()
    def abredb(self,hostc,usuarioc,senhac,bancoc,porta):
        # Faz a conexão ao banco de dados MySQL
        conexao = mysql.connector.connect(host=hostc, port=porta, user=usuarioc, password=senhac, database=bancoc, autocommit=True, compress=True)
        if conexao.is_connected():
            return conexao
        else:
            return False
    def fechadb(self,conexao,cursor):
        if conexao.is_connected():
            cursor.close()
            conexao.close()
    def geradf(self,Tabela):
        # Gera um dataframe a partir de um select
        dftemp = DataFrame(Tabela)
        return dftemp
    def ptab(self, valores='', operacao='P', tabela='', campos='', chave='', vlchave=''):
        try:
            self.con = self.abredb(self.host, self.usuario, self.senha, self.banco, 3306)
            if self.con == False:
                messagebox('Atenção', 'Falha ao tentar abrir o banco de dados')
            self.cursor = self.con.cursor()
            operacao = operacao.upper()
            sql = ''
            retorno = True
            if operacao == 'C':
                sql = f'insert into {tabela} {campos} values ({valores})'
            elif operacao == 'A':
                sql = f'update {tabela} set '
                cont = 0
                for z in valores:
                    sql += f'{campos[cont]} = {z}'
                    if cont < len(campos)-1:
                        sql += ', '
                    cont += 1
                sql += f' Where {chave} = {vlchave};'
            elif operacao == 'E':
                sql = f'delete from {tabela} where {chave} = {vlchave};'
            elif operacao == 'P':
                sql = f'select * from {tabela} where {chave}={vlchave}'
            self.cursor.execute(sql)
            self.ptabret = self.cursor.fetchall()
            if operacao=='P':
                if self.cursor.rowcount == 0:
                    retorno = False
            return retorno
        except Error:
            messagebox.showwarning('Falha',F'Ocorreu o erro: {Error}')


