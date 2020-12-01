import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root",
    database="vehicles"
)

cursor = db.cursor()
sql="CREATE TABLE cars (reg VARCHAR(20) PRIMARY KEY, manu_code VARCHAR(3), mileage INT, price DECIMAL(8,2), colour VARCHAR(20), fuel ENUM('petrol','diesel'))"
cursor.execute(sql)