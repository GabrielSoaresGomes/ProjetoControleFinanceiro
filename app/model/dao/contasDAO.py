from calendar import month

from sqlalchemy import null
from app.model.database.db_main import db, Conta
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class ContaDAO:
  def __init__(self):
    pass

  def listar_contas(self):
    contas = Conta.query.all()
    return contas

  def adicionar_conta(self, data_vencimento, data_pagamento, valor, recorrente, numero_repeticao, descricao, status):
    conta = Conta(data_vencimento = data_vencimento, data_pagamento='-', valor = valor, recorrente = recorrente, numero_repeticao = numero_repeticao, descricao = descricao, status=status)
    proximos_dias = []
    proximos_dias.append( datetime.today() + relativedelta(days=1) )
    proximos_dias.append( datetime.today() + relativedelta(days=2) )
    proximos_dias.append( datetime.today() + relativedelta(days=3) )

    if datetime.strptime(data_vencimento, "%Y-%m-%d") <= datetime.today():
      conta.status = status = "Vencida"
    elif datetime.strptime(data_vencimento, "%Y-%m-%d") in proximos_dias:
      conta.status = status = "Vencendo"

    if conta.recorrente:
      nova_data = data_vencimento
      for repeticao in range(int(conta.numero_repeticao)):
        db.session.add(conta)
        nova_data = datetime.strptime(nova_data, "%Y-%m-%d")
        nova_data = nova_data + relativedelta(months=1)
        print(nova_data)
        nova_data = nova_data.strftime("%Y-%m-%d")
        conta = Conta(data_vencimento = nova_data, data_pagamento='-', valor = conta.valor, recorrente = conta.recorrente, numero_repeticao = conta.numero_repeticao, descricao = conta.descricao, status=status)
    else:
      db.session.add(conta)
    db.session.commit()

  def verificar_status(self):
    proximos_dias = []
    proximos_dias.append( (datetime.today() + relativedelta(days=1)).strftime('%Y-%m-%d') )
    proximos_dias.append(( datetime.today() + relativedelta(days=2)).strftime('%Y-%m-%d') )
    proximos_dias.append( (datetime.today() + relativedelta(days=3)).strftime('%Y-%m-%d') )
    contas = Conta.query.all()
    for conta in contas:
      data_atual_string = datetime.strftime( datetime.strptime(conta.data_vencimento, "%Y-%m-%d"),"%Y-%m-%d" )
      if conta.data_pagamento != null and conta.data_pagamento != '-':
        conta.status = "Paga"
      elif datetime.strptime(conta.data_vencimento, "%Y-%m-%d") <= datetime.today():
        conta.status = "Vencida"
      elif data_atual_string in proximos_dias:
        conta.status = "Vencendo"
      else:
        conta.status = "À pagar"