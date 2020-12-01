import mysql.connector

class CarDao:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'Root',
            database = 'vehicles'
        )
    
    def create(self, car):
        cursor = self.db.cursor()
        sql = "Insert into cars (reg, manu_code, mileage, price, colour, fuel) values (%s,%s,%s,%s,%s,%s)"
        values= [
            car["reg"],
            car["manu_code"],
            car["mileage"],
            car["price"],
            car["colour"],
            car["fuel"]
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid
    
    def getAll(self):
        cursor = self.db.cursor()
        sql = "select * from cars"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results) # This is an array of tuples
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)
        return returnArray # This will be an array of dict objects
    
    def findById(self, reg):
        cursor = self.db.cursor()
        sql = "select * from cars where reg = %s"
        values = [reg]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)
    
    def update(self, car):
        cursor = self.db.cursor()
        sql = "update cars set manu_code = %s, mileage = %s, price = %s, colour = %s, fuel = %s where reg = %s"
        values= [
            car["manu_code"],
            car["mileage"],
            car["price"],
            car["colour"],
            car["fuel"],
            car["reg"],
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return car
    
    def delete(self, reg):
        cursor = self.db.cursor()
        sql = "delete from cars where reg = %s"
        values = [reg]
        cursor.execute(sql, values)
        self.db.commit()
        return {}


    # function to convert a tuple to a dict object
    def convertToDict(self, result):
        colnames = ['reg', 'manu_code', 'mileage', 'price', 'colour', 'fuel']
        car = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                car[colName] = value
        return car



carDao = CarDao()