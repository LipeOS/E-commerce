from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_mysqldb import MySQL
import logging

app = Flask (__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'banco'
app.config['MYSQL_HOST'] = 'localhost'  



