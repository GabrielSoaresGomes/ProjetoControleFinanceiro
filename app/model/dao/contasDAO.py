from app.model.database.db_main import db, Conta

class ContaDAO:
  def __init__(self):
    pass

  def listar_contas(self):
    contas = Conta.query.all()
    return contas

  def adicionar_conta(self, conta):
    db.session.add(conta)
    db.session.commit()