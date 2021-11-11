from flask import Flask, render_template, session, flash, request, redirect
app= Flask(__name__)
@app.route('/')

def index():
  return render_template("index.html")

if __name__=="__main__":   # Asegúrese de que este archivo se ejecute directamente y no desde un módulo diferente
    app.run(debug=True)    # ejecuta la aplicación en modo depuracion