from flask import render_template, request, jsonify

from app import app
from app.model.dao import contaDAO
from app.model.database.db_main import db, Conta

@app.route("/contas", methods=['POST', "GET"])
def lista_contas():
  if request.method == "POST":
    data_vencimento = request.form.get('data_vencimento', '')
    valor = request.form.get('valor', '')
    recorrente = request.form.get('recorrente', False)
    recorrente = False if recorrente == 'false' else True

    numero_repeticao = request.form.get('numero_repeticao', '')
    descricao = request.form.get('descricao', '')

    contaDAO.adicionar_conta(data_vencimento = data_vencimento, data_pagamento='-', valor = valor, recorrente = recorrente, numero_repeticao = numero_repeticao, descricao = descricao, status='À pagar')
  contas = contaDAO.listar_contas()
  return render_template('lista_contas.html', title="Lista de Contas", contas=contas)