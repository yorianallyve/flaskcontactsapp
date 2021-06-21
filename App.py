from flask import Flask
from flask_mysqldb import MySQL

app=Flask(__name__)


# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'secret'
app.config['MYSQL_DB'] = 'flaskcontact'
mysql = MySQL(app)

@app.route('/')
def index():
    return 'test'

@app.route('/add_contact')
def add_contact():
    return 'add contact'

@app.route('/edit')
def edit_contact():
    return 'edit contact'

@app.route('/delete')
def delete_contact():
    return 'delete contact'


if __name__ == '__main__':
    app.run(port=3000, debug=True)