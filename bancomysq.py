from peewee import *

database = MySQLDatabase('chinaa94_criptobot', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': 'br654.hostgator.com.br', 'port': 3306, 'user': 'chinaa94_teste', 'passwd': '197200197200'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Cliente(BaseModel):
    api_key = CharField(null=True)
    cod_cli = CharField(primary_key=True)
    lote_padrao = FloatField(null=True)
    margem_lucro = FloatField(null=True)
    nome = CharField()
    senha_api = CharField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    tamanho_fuga = IntegerField(null=True)
    telefone = CharField()
    timeframe = CharField(constraints=[SQL("DEFAULT 'H4'")])

    class Meta:
        table_name = 'Cliente'

class Historico(BaseModel):
    abertura = DateTimeField(null=True)
    cod_opera = IntegerField(null=True)
    fechamento = DateTimeField(null=True)
    operacao = IntegerField(null=True)
    preco_abertura = CharField(null=True)
    preco_fechamento = CharField(null=True)

    class Meta:
        table_name = 'Historico'
        primary_key = False

class Ativos(BaseModel):
    cliente = ForeignKeyField(column_name='cliente', field='cod_cli', model=Cliente)
    cod_opera = AutoField()
    moeda_base = CharField()
    moeda_compra = CharField()
    valor_lote = FloatField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'ativos'
        indexes = (
            (('cliente', 'moeda_base', 'moeda_compra'), True),
        )

class EntradasAbertas(BaseModel):
    abertura = DateTimeField(null=True)
    alvo = CharField(null=True)
    cod_opera = IntegerField(null=True)
    fechamento = DateTimeField(null=True)
    operacao = IntegerField(null=True)
    preco_abertura = CharField(null=True)
    preco_fechamento = CharField(null=True)

    class Meta:
        table_name = 'entradas_abertas'
        primary_key = False

class Operacoes(BaseModel):
    aberto = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    cod_opera = ForeignKeyField(column_name='cod_opera', field='cod_opera', model=Ativos, null=True)
    dataarma = DateTimeField(null=True)
    datahoraabertura = DateTimeField(null=True)
    lote = CharField(null=True)
    operacao = AutoField()
    preco_abertura = CharField()

    class Meta:
        table_name = 'operacoes'
        indexes = (
            (('cod_opera', 'preco_abertura'), True),
        )

