from calendar import month
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
    if datetime.strptime(data_vencimento, "%Y-%m-%d") <= datetime.today():
      conta.status = status = "Vencida"
    #elif (datetime.today().strftime('%Y-%m-%d') + relativedelta(days=3)) <= datetime.strptime(data_vencimento, "%Y-%m-%d"):
    elif (datetime.strptime(data_vencimento, "%Y-%m-%d") + relativedelta(days=-3)) <= 3:
      conta.status = status = "Vencendo"

    if conta.recorrente:
      for repeticao in range(int(conta.numero_repeticao)):
        db.session.add(conta)
        
        nova_data = data_vencimento + relativedelta(months=1)
        nova_data = nova_data.strftime("%Y-%m-%d")
        conta = Conta(data_vencimento = nova_data, data_pagamento='-', valor = conta.valor, recorrente = conta.recorrente, numero_repeticao = conta.numero_repeticao, descricao = conta.descricao, status=status)
    else:
      db.session.add(conta)
    db.session.commit()