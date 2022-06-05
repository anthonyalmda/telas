from bancomysq import Operacoes,Ativos
from datetime import datetime

df = Operacoes.select().where(Operacoes.ativo == '2')
for x in df:
    dado = x.get()
    ativo = x.get().ativo.cod_opera
    preco = x.preco_abertura
    data = x.dataarma
    #x.create(ativo=ativo,preco_abertura=preco, dataarma=data, datahoraabertura=datetime.now(), aberto=1)
    print(ativo, preco)
    atualiza = Operacoes.update(datahoraabertura=datetime.now(), aberto=1).where((Operacoes.ativo == '2') & (Operacoes.preco_abertura==preco))
    print(atualiza)
    atualiza.execute()
    # print(dado.ativo, dado.preco_abertura,dado.dataarma,dado.datahoraabertura,dado.aberto,dado.datahorafhecamento)
    # dado.datahoraabertura =datetime.now()
    # dado.aberto = 1
    # dado.save()

   # dado.save()
# for linha in teste:
#     print(linha.datahoraabertura,linha.ativo)
#     atualiza = linha.get()
#     atualiza.update(datahoraabertura = datetime.now())
#     atualiza.save()
#     print(linha.datahoraabertura)