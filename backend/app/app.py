from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_mysqldb import MySQL
import logging
import os

template_dir = os.path.join(os.getcwd(), 'frontend')

app = Flask(__name__, template_folder=template_dir)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'banco'
app.config['MYSQL_HOST'] = 'localhost'  

logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return render_template('../../frontend/templates/login.html')

if __name__ == '__main__':
    app.run(debug=True)