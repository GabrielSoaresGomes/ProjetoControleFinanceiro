from flask_sqlalchemy import SQLAlchemy
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contas.db'
db = SQLAlchemy(app)

class Contas(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  data_vencimento = db.Column(db.String(10), nullable=True)
  data_pagamento = db.Column(db.String(10), nullable=True) # Alterar quando apertar o botão de conta paga
  valor = db.Column(db.Float())
  recorrente = db.Column(db.Boolean())
  numero_repeticao = db.Column(db.Integer())
  descricao = db.Column(db.Text())

  def __repr__(self):
        return '<Contas %r>' % self.data_vencimento
