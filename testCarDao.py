from CarDao import carDao

supplier1 = {
    'name': 'Barry Clarke',
    'location': 'Dundalk',
    'phone': 42_9312345
}

supplier2 = {
    'name': 'Jimmy Murphy',
    'location': 'Swords',
    'phone': 1_6534271
}

car1 = {
    'kind': 'new',
    'chassisID': '1234567',
    'manu_code': 'TOY',
    'manu_model': 'Corolla',
    'year': 2020,
    'mileage': 0,
    'price': 35000,
    'colour': 'silver',
    'fuel': 'petrol',
    'supplierID': 1
}

car2 = {
    'kind': 'new',
    'chassisID': '1234567',
    'manu_code': 'TOY',
    'manu_model': 'Avensis',
    'year': 2020,
    'mileage': 0,
    'price': 42000,
    'colour': 'blue',
    'fuel': 'petrol',
    'supplierID': 1
}

car3 = {
    'kind': 'new',
    'chassisID': '1234567',
    'manu_code': 'TOY',
    'manu_model': 'Yaris',
    'year': 2020,
    'mileage': 0,
    'price': 18000,
    'colour': 'Yellow',
    'fuel': 'petrol',
    'supplierID': 2
}




#returnvalue = carDao.createSupplier(supplier1)
#returnvalue = carDao.createSupplier(supplier2)

#print("Get All Suppliers")
#returnvalue = carDao.getAllSupplier()
#print(returnvalue)
#returnvalue = carDao.createCar(car1)
returnvalue = carDao.createCar(car2)
#returnvalue = carDao.createCar(car3)
#returnvalue = carDao.getAllCar()
#print("Get All Cars")
#print(returnvalue)
#returnvalue = carDao.findByModel(car2['manu_model'])
#print("Find By car Model")
#print(returnvalue)
#returnvalue = carDao.delete(car1['reg'])
#print(returnvalue)
#returnvalue = carDao.getAll()
#print("Get All")
#print(returnvalue)



#returnvalue = carDao.update(car2)
#print("Updated car 2")
#print(returnvalue)
#returnvalue = carDao.findById(car2['reg'])
#print("Find ById")
#print(returnvalue)
#returnvalue = carDao.delete(car2['reg'])
#print(returnvalue)
#returnvalue = carDao.getAll()
#print("Get All")
#print(returnvalue)
