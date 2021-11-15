from flask import Flask, render_template, session, flash, request, redirect
app= Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

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
  return render_template(
    "resultados.html",
    ccomuna = ccomuna,
    mcuadrados = mcuadrados,
    dcorreo = dcorreo,
    nnombre = nnombre,
    comuna = comuna
    ) 

  

@app.route('/bibliografía')
def links():
  return render_template("bibliografía.html")


if __name__=="__main__":   # Asegúrese de que este archivo se ejecute directamente y no desde un módulo diferente
    app.run(debug=True)    # ejecuta la aplicación en modo depuracion