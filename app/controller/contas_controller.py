from flask import render_template, request, jsonify

from app import app

@app.route("/contas")
def lista_contas():
  return render_template('lista_contas.html', title="Lista de Contas")

@app.route("/contas/adicionar")
def adicionar_conta():
  pass #Adicionar no banco
