from flask import Flask
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import re

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
    return 'Index page'

@app.route("/add_customer", methods=['POST'])
def add_customer():
    #Assuming that the request will be in the JSON form
    request_data = request.get_json()

    #Create a cursor for the database connection
    cur = mysql.connection.cursor()

    #Get customer details from the JSON request
    customer_id = request_data["customer_id"]
    customer_name = request_data["customer_name"]
    customer_address = request_data["customer_address"]
    phone = request_data['phone']
    email = request_data["email"]

    #Create a regex for checking email format
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    #Make sure that the customer ID doesn't exists already
    cur.execute("SELECT * FROM customer where customer_id = " + customer_id + " ;")
    result = cur.fetchall()
    if len(result) > 0:
        return "Customer ID already exists."

    #Make sure that the customer ID is not null
    elif customer_id == "":
        return "Please enter customer ID."    

    #Make sure that the customer ID is numbers
    elif not customer_id.isnumeric():
        return "Custome ID must be numbers."

    #Make sure that the customer name is not null
    elif customer_name == "":
        return "Please enter customer name."

    #Make sure that the customer address is not null
    elif customer_address == "":
        return "Please enter customer address."
    
    #Make sure that the customer email is in the right format if it exists
    elif (email != "") and (not re.fullmatch(email_regex, email)):
        return "Please enter a valid email address."
    
    #Make sure that customer phone is not null
    elif len(phone) == 0:
        return "Please enter phone number."
    
    #Make sure that all the customer phone numbers are numbers
    for number in phone:
        if not number.isnumeric():
            return "Please enter a valid phone number."

    #Create a SQL query for inserting a new customer into customer table
    sql = "INSERT INTO customer (customer_id, customer_name, customer_address, email) VALUES (%s, %s, %s, %s) ;"
    val = (customer_id, customer_name, customer_address, email)
    cur.execute(sql, val)

    #Create a SQL query for inserting new customer phone numbers into customer_phone table
    for number in phone:
        sql = "INSERT INTO customer_phone (phone, customer_id) VALUES (%s, %s) ;"
        val = (number, customer_id)
        cur.execute(sql, val)
    mysql.connection.commit()
    
    return "Customer Created Successfully"
    
    
@app.route("/delete_customer", methods=['POST'])
def delete_customer():
    #Assuming that the request will be in the JSON form
    request_data = request.get_json()

    #Create a cursor for the database connection
    cur = mysql.connection.cursor()

    #Get customer ID from the JSON request
    customer_id = request_data["customer_id"]

    #Make sure that the customer ID exists
    cur.execute("SELECT * FROM customer where customer_id = " + customer_id + " ;")
    result = cur.fetchall()
    if len(result) == 0:
        return "Customer ID doesn't exists."

    #Create a SQL query for deleting a customer from customer table
    sql = "DELETE FROM customer WHERE customer_id = %s ;"
    val = customer_id
    cur.execute(sql, val)
    mysql.connection.commit()

    return "Customer Deleted Successfully"

    


if __name__ == '__main__':
    app.run(debug=True)