from flask import Flask, url_for, request, abort, jsonify
from CarDao import carDao

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
    return "hello"

@app.route('/cars')
def getAll():
    return jsonify(carDao.getAll())

@app.route('/cars/<string:reg>')
def fingById(reg):
    return jsonify(carDao.findById(reg))

@app.route('/cars', methods=['POST'])
def create():
    if not request.json:
        abort(400)
    
    car = {
        "reg": request.json["reg"],
        "manu_code": request.json["manu_code"],
        "mileage": request.json["mileage"],
        "price": request.json["price"],
        "colour": request.json["colour"],
        "fuel": request.json["fuel"]
    }
    return jsonify({})

@app.route('/cars/<string:reg>', methods=['PUT'])
def update(reg):
    foundCars=[]
    return jsonify({})

@app.route('/cars/<string:reg>', methods=["DELETE"])
def fingByIddelete(reg):
    return jsonify({"done": True})

if __name__ == "__main__":
    app.run(debug=True)




    


