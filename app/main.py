from flask import Flask, render_template, session, flash, request, redirect, jsonify
app= Flask(__name__)

import gspread
from oauth2client.service_account import ServiceAccountCredentials

credential = ServiceAccountCredentials.from_json_keyfile_name("credentials.json",
                                                              ["https://spreadsheets.google.com/feeds",                                                               "https://www.googleapis.com/auth/spreadsheets",                                                        "https://www.googleapis.com/auth/drive.file",                                                        "https://www.googleapis.com/auth/drive"])
client = gspread.authorize(credential)
users_gs = client.open("Correos").sheet1


@app.route('/')
def index():
  return render_template("index.html")

@app.route('/excel')
def excel():
  return jsonify(users_gs.get_all_records())



@app.route('/objetivos')
def objectives():
  return render_template("objetivos.html")

@app.route('/equipo')
def team():
  return render_template("equipo.html")

@app.route('/calculadora')
def calculator():
  return render_template("calculadora.html")

@app.route('/resultados', methods=['POST'])
def results():
  
  ccomuna = request.form['ccomuna']
  mcuadrados = request.form['mcuadrados']
  dcorreo = request.form['dcorreo']
  nnombre = request.form['nnombre']
  comuna = request.form['comuna']
  users = users_gs.get_all_records()
  users_new_id = int(users[0]['id']) + 1
  row = [users_new_id,dcorreo,nnombre,comuna,ccomuna]
  users_gs.insert_row(row,2)
  posible_energía= (((int(mcuadrados)/1.95)*180*8.67*0.9)/1000)
  cdiario = (int(ccomuna))/30
  ev = posible_energía - cdiario
  gv = ev * 78
  gv_anual = gv*364
  valor = 34000
  costo= valor * int(mcuadrados)
  ganancia = gv_anual - costo
  

  return render_template(
    "resultados.html",
    ccomuna = ccomuna,
    mcuadrados = mcuadrados,
    dcorreo = dcorreo,
    nnombre = nnombre,
    comuna = comuna,
    posible_energía = posible_energía,
    ganancia = ganancia,
    costo = costo,
    gv_anual = gv_anual
    ) 

  

@app.route('/bibliografía')
def links():
  return render_template("bibliografía.html")


if __name__=="__main__":   # Asegúrese de que este archivo se ejecute directamente y no desde un módulo diferente
    app.run(debug=True)    # ejecuta la aplicación en modo depuracion