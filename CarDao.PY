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
    
    def getAllSupplier(self):
        cursor = self.db.cursor()
        sql = "select * from suppliers"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results) # This is an array of tuples
        for result in results:
            resultAsDict = self.convertToDictSupplier(result)
            returnArray.append(resultAsDict)
        return returnArray # This will be an array of dict objects
    
    def findByLocation(self, location):
        cursor = self.db.cursor()
        sql = "select * from suppliers where location = %s"
        values = [location]
        cursor.execute(sql, values)
        results = cursor.fetchall()
        returnArray = []
        #print(results) # This is an array of tuples
        for result in results:
            resultAsDict = self.convertToDictSupplier(result)
            returnArray.append(resultAsDict)
        return returnArray # This will be an array of dict objects
    
    def findByIdSupplier(self, supplierID):
        cursor = self.db.cursor()
        sql = "select * from suppliers where supplierID = %s"
        values = [supplierID]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictSupplier(result)
    
    def getAllCar(self):
        cursor = self.db.cursor()
        sql = "select * from cars"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results) # This is an array of tuples
        for result in results:
            resultAsDict = self.convertToDictCar(result)
            returnArray.append(resultAsDict)
        return returnArray # This will be an array of dict objects
    
    def findByModel(self, model):
        cursor = self.db.cursor()
        sql = "select * from cars where manu_model = %s"
        values = [model]
        cursor.execute(sql, values)
        results = cursor.fetchall()
        returnArray = []
        #print(results) # This is an array of tuples
        for result in results:
            resultAsDict = self.convertToDictCar(result)
            returnArray.append(resultAsDict)
        return returnArray # This will be an array of dict objects
    
    def findByKind(self, kind):
        cursor = self.db.cursor()
        sql = "select * from cars where kind = %s"
        values = [kind]
        cursor.execute(sql, values)
        results = cursor.fetchall()
        returnArray = []
        #print(results) # This is an array of tuples
        for result in results:
            resultAsDict = self.convertToDictCar(result)
            returnArray.append(resultAsDict)
        return returnArray # This will be an array of dict objects
    
    def findByChassis(self, chassisID):
        cursor = self.db.cursor()
        sql = "select * from cars where chassisID = %s"
        values = [chassisID]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictCar(result)
    
    def findByIdCar(self, cid):
        cursor = self.db.cursor()
        sql = "select * from cars where cid = %s"
        values = [cid]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictCar(result)

    # Create operations
    # Create Supplier
    def createSupplier(self, supplier):
        cursor = self.db.cursor()
        sql = "Insert into suppliers (name, location, phone) values (%s,%s,%s)"
        values= [
            supplier["name"],
            supplier["location"],
            supplier["phone"],
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid      
    
    # Create Car
    def createCar(self, car):
        cursor = self.db.cursor()
        sql = "Insert into cars (kind, chassisID, manu_code, manu_model, year, mileage, price, colour, fuel, supplierID)\
        values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values= [
            car["kind"],
            car["chassisID"],
            car["manu_code"],
            car["manu_model"],
            car["year"],
            car["mileage"],
            car["price"],
            car["colour"],
            car["fuel"],
            car["supplierID"]
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid
    
    # Update operations
    # Update Car
    def updateCar(self, car):
        cursor = self.db.cursor()
        sql = "update cars set kind = %s, chassisID = %s, manu_code = %s, manu_model = %s, year = %s, mileage = %s, price = %s, colour = %s, fuel = %s, supplierID = %s where cid = %s"
        values= [
            car["kind"],
            car["chassisID"],
            car["manu_code"],
            car["manu_model"],
            car["year"],
            car["mileage"],
            car["price"],
            car["colour"],
            car["fuel"],
            car["supplierID"],
            car["cid"]
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return car
    
    # Update Supplier
    def updateSupplier(self, supplierID):
        cursor = self.db.cursor()
        sql = "update suppliers set name = %s, location = %s, phone = %s where supplierID = %s"
        values= [
            supplierID["name"],
            supplierID["location"],
            supplierID["phone"],
            supplierID["supplierID"]
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return supplierID
    
    # Delete operations
    # Delete Car
    def deleteCar(self, cid):
        cursor = self.db.cursor()
        sql = "delete from cars where cid = %s"
        values = [cid]
        cursor.execute(sql, values)
        self.db.commit()
        return {}
    
    # Delete Supplier
    def deleteSupplier(self, supplierID):
        cursor = self.db.cursor()
        sql = "delete from suppliers where supplierID = %s"
        values = [supplierID]
        cursor.execute(sql, values)
        self.db.commit()
        return {}


    # function to convert a tuple to a dict object for the suppliers table
    def convertToDictSupplier(self, result):
        colnames = ['supplierID','name', 'location', 'phone']
        supplier = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                supplier[colName] = value
        return supplier
    
    
    # function to convert a tuple to a dict object for the cars table
    def convertToDictCar(self, result):
        colnames = ['cid', 'kind', 'chassisID', 'manu_code', 'manu_model', 'year', 'mileage', 'price', 'colour', 'fuel', 'supplierID']
        car = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                car[colName] = value
        return car



carDao = CarDao()