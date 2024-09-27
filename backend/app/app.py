from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_mysqldb import MySQL
import logging

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True)