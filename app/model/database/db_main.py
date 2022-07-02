from flask_sqlalchemy import SQLAlchemy
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///conta.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Conta(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  data_vencimento = db.Column(db.String(10), nullable=True)
  data_pagamento = db.Column(db.String(10), nullable=True) # Alterar quando apertar o botão de conta paga
  valor = db.Column(db.Float())
  recorrente = db.Column(db.Boolean())
  numero_repeticao = db.Column(db.Integer())
  descricao = db.Column(db.Text())
  status = db.Column(db.Text()) # Alterar de acordo com o vencimento e pagamento. status: À pagar(azul), Paga(verde), Vencida(vermelha) ou Vencendo(amarela)

  def __repr__(self):
        return f'<Conta {self.data_vencimento}>'
