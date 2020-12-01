from CarDao import carDao

car1 = {
    'reg': '2019-D-1234',
    'manu_code': 'TOY',
    'mileage': 8045,
    'price': 23500,
    'colour': 'silver',
    'fuel': 'petrol'
}

car2 = {
    'reg': '2018-D-12522',
    'manu_code': 'TOY',
    'mileage': 16398,
    'price': 20500,
    'colour': 'blue',
    'fuel': 'petrol'
}


#returnvalue = carDao.create(car1)
returnvalue = carDao.getAll()
print("Get All")
print(returnvalue)
#returnvalue = carDao.findById(car2['reg'])
#print("Find By Id")
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
