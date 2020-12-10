from flask import Flask, session, url_for, redirect, request, abort, jsonify
from CarDao import carDao


app = Flask(__name__, static_url_path='', static_folder='staticpages')
app.secret_key = 'secretoputbhd6wm'

@app.route('/')
def index():
    return "hello"

# Read operations
# Read Cars
@app.route('/cars')
def getAllCar():
    return jsonify(carDao.getAllCar())

@app.route('/cars/model/<string:model>')
def findByModel(model):
    return jsonify(carDao.findByModel(model))

@app.route('/cars/kind/<string:kind>')
def findByKind(kind):
    return jsonify(carDao.findByKind(kind))

@app.route('/cars/chassis/<string:chassisID>')
def findByChassis(chassisID):
    return jsonify(carDao.findByChassis(chassisID))


# Read Suppliers
@app.route('/suppliers')
def getAllSupplier():
    return jsonify(carDao.getAllSupplier())

@app.route('/suppliers/<string:location>')
def findByLocation(location):
    return jsonify(carDao.findByLocation(location))


# Create operations
# Create Cars
@app.route('/cars', methods=['POST'])
def createCar():
    if not request.json:
        abort(400)
    
    car = {
        "kind": request.json["kind"],
        "chassisID": request.json["chassisID"],
        "manu_code": request.json["manu_code"],
        "manu_model": request.json["manu_model"],
        "year": request.json["year"],
        "mileage": request.json["mileage"],
        "price": request.json["price"],
        "colour": request.json["colour"],
        "fuel": request.json["fuel"],
        "supplierID": request.json["supplierID"],
    }
    supplierID = car["supplierID"]
    foundSupplier=carDao.findByIdSupplier(supplierID)
    if foundSupplier == {}:
        return jsonify({}), 404
    return jsonify(carDao.createCar(car))

# Create Suppliers
@app.route('/suppliers', methods=['POST'])
def createSupplier():
    if not request.json:
        abort(400)
    
    supplier = {
        "name": request.json["name"],
        "location": request.json["location"],
        "phone": request.json["phone"],
    }
    return jsonify(carDao.createSupplier(supplier))

# Update operations
# Update Cars
@app.route('/cars/<string:cid>', methods=['PUT'])
def updateCar(cid):
    # If cid reg is not recognised
    foundCar=carDao.findByIdCar(cid)
    if foundCar == {}:
        return jsonify({}), 404
    currentCar = foundCar
    if 'kind' in request.json:
        currentCar['kind'] = request.json['kind']
    if 'chassisID' in request.json:
        currentCar['chassisID'] = request.json['chassisID']
    if 'manu_code' in request.json:
        currentCar['manu_code'] = request.json['manu_code']
    if 'manu_model' in request.json:
        currentCar['manu_model'] = request.json['manu_model']
    if 'year' in request.json:
        currentCar['year'] = request.json['year']
    if 'mileage' in request.json:
        currentCar['mileage'] = request.json['mileage']
    if 'price' in request.json:
        currentCar['price'] = request.json['price']
    if 'colour' in request.json:
        currentCar['colour'] = request.json['colour']
    if 'fuel' in request.json:
        currentCar['fuel'] = request.json['fuel']
    if 'supplierID' in request.json:
        currentCar['supplierID'] = request.json['supplierID']
    carDao.updateCar(currentCar)
    
    return jsonify(currentCar)

# Update Suppliers
@app.route('/suppliers/<string:supplierID>', methods=['PUT'])
def updateSupplier(supplierID):
    # If supplierID is not recognised
    foundSupplier=carDao.findByIdSupplier(supplierID)
    if foundSupplier == {}:
        return jsonify({}), 404
    currentSupplier = foundSupplier
    if 'name' in request.json:
        currentSupplier['name'] = request.json['name']
    if 'location' in request.json:
        currentSupplier['location'] = request.json['location']
    if 'phone' in request.json:
        currentSupplier['phone'] = request.json['phone']
    carDao.updateSupplier(currentSupplier)
    
    return jsonify(currentSupplier)


# Delete operations
# Delete Cars
@app.route('/cars/<string:cid>', methods=["DELETE"])
def deleteCar(cid):
    foundCar=carDao.findByIdCar(cid)
    if foundCar == {}:
        return jsonify({"No such car ID": False})
    else:
        carDao.deleteCar(cid)
        return jsonify({"done": True})

# Delete Suppliers
@app.route('/suppliers/<string:supplierID>', methods=["DELETE"])
def deleteSupplier(supplierID):
    foundSupplier=carDao.findByIdSupplier(supplierID)
    if foundSupplier == {}:
        return jsonify({"No such Supplier ID": False})
    else:
        carDao.deleteSupplier(supplierID)
        return jsonify({"done": True})

if __name__ == "__main__":
    app.run(debug=True)




    


