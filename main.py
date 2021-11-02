from flask import Flask, render_template, session, flash, request, redirect
app= Flask(__name__)
@app.route('/')
def index():
  return "<h1>Welcome to CodingX</h1>"