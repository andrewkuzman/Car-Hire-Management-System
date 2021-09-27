from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

#Configuring Database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'MySQL@123'
app.config['MYSQL_DB'] = 'car_hire_management_system'

#Create an object from MySQL module and pass the database configuration parameters to it
mysql = MySQL(app)

@app.route("/")
def index():
    return 'success'

if __name__ == '__main__':
    app.run(debug=True)