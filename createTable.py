import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root",
    database="vehicles"
)

cursor = db.cursor()
sql="CREATE TABLE suppliers (`supplierID` int NOT NULL AUTO_INCREMENT,\
`name` varchar(50) NOT NULL,\
`location` varchar(50) DEFAULT NULL,\
`phone` int NOT NULL,\
PRIMARY KEY (`supplierID`))"
cursor.execute(sql)


cursor = db.cursor()
sql="CREATE TABLE cars (`cid` int NOT NULL AUTO_INCREMENT,\
`kind` enum('new','used') NOT NULL,\
`chassisID` varchar(20) NOT NULL,\
`manu_code` varchar(3) DEFAULT NULL,\
`manu_model` varchar(12) DEFAULT NULL,\
`year` int DEFAULT NULL,\
`mileage` int DEFAULT NULL,\
`price` int NOT NULL,\
`colour` varchar(20) DEFAULT NULL,\
`fuel` enum('petrol','diesel') DEFAULT NULL,\
`supplierID` int NOT NULL,\
PRIMARY KEY (`cid`), KEY `supplierID` (`supplierID`),\
CONSTRAINT `cars_ibfk_1` FOREIGN KEY (`supplierID`) REFERENCES `suppliers` (`supplierID`) ON DELETE CASCADE)"
cursor.execute(sql)

 
  