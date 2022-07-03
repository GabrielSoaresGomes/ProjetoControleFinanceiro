from flask import render_template
from app import app

from app.model.dao import contaDAO

@app.route('/')
def index():
  contaDAO.verificar_status()
  contas_mes = contaDAO.lista_contas_mes()
  valor_contas_mes = contaDAO.valor_contas_mes()
  contaDAO.verificar_status()
  return render_template("home.html", title="Home", contas_mes=contas_mes, valor_contas_mes=valor_contas_mes)