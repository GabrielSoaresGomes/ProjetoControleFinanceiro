from flask import render_template

from app import app

@app.route("/contas")
def lista_contas():
  return render_template('lista_contas.html', title="Lista de Contas")
