from peewee import *

database = MySQLDatabase('chinaa94_criptobot', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': 'br654.hostgator.com.br', 'port': 3306, 'user': 'chinaa94_bot', 'password': '197200197200'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Cliente(BaseModel):
    coluna_5 = CharField(column_name='Coluna 5')
    api_key = CharField()
    cod_cli = CharField(primary_key=True)
    nome = CharField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    telefone = CharField()

    class Meta:
        table_name = 'Cliente'

class Ativos(BaseModel):
    cliente = ForeignKeyField(column_name='cliente', field='cod_cli', model=Cliente)
    cod_opera = IntegerField(unique=True)
    moeda_base = CharField()
    moeda_compra = CharField()
    valor_lote = FloatField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'ativos'
        indexes = (
            (('cliente', 'moeda_base', 'moeda_compra'), True),
        )
        primary_key = CompositeKey('cliente', 'moeda_base', 'moeda_compra')

class Operacoes(BaseModel):
    aberto = IntegerField(null=True)
    ativo = ForeignKeyField(column_name='ativo', field='cod_opera', model=Ativos, null=True)
    dataarma = DateTimeField(null=True)
    datahoraabertura = DateTimeField(null=True)
    datahorafhecamento = DateTimeField(null=True)
    lote = CharField(null=True)
    preco_abertura = CharField()
    preco_fechamento = CharField(null=True)

    class Meta:
        table_name = 'operacoes'
        indexes = (
            (('ativo', 'preco_abertura'), True),
        )
        primary_key = False

