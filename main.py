from flask import Flask, jsonify, request
from handler.parts import PartHandler
from handler.supplier import SupplierHandler
from handler.resources import ResourcesHandler
from handler.request import RequestHandler
# Import Cross-Origin Resource Sharing to enable
# services on other ports on this machine or on other
# machines to access this app
from flask_cors import CORS, cross_origin

# Activate
app = Flask(__name__)
# Apply CORS to this app
CORS(app)

value_add={(1,'3/17/2020','mayaguez,calle acasia',3)}


@app.route('/')
def greeting():
    return 'Hello, this is the parts DB App!'

@app.route('/PartApp/parts', methods=['GET', 'POST'])
def getAllParts():
    if request.method == 'POST':
        # cambie a request.json pq el form no estaba bregando
        # parece q estaba poseido por satanas ...
        # DEBUG a ver q trae el json q manda el cliente con la nueva pieza
        print("REQUEST: ", request.json)
        return PartHandler().insertPartJson(request.json)
    else:
        if not request.args:
            return PartHandler().getAllParts()
        else:
            return PartHandler().searchParts(request.args)

@app.route('/PartApp/parts/<int:pid>', methods=['GET', 'PUT', 'DELETE'])
def getPartById(pid):
    if request.method == 'GET':
        return PartHandler().getPartById(pid)
    elif request.method == 'PUT':
        return PartHandler().updatePart(pid, request.form)
    elif request.method == 'DELETE':
        return PartHandler().deletePart(pid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/PartApp/parts/<int:pid>/suppliers')
def getSuppliersByPartId(pid):
    return PartHandler().getSuppliersByPartId(pid)

@app.route('/PartApp/suppliers', methods=['GET', 'POST'])
def getAllSuppliers():
    if request.method == 'POST':
        return SupplierHandler().insertSupplier(request.form)
    else :
        if not request.args:
            return SupplierHandler().getAllSuppliers()
        else:
            return SupplierHandler().searchSuppliers(request.args)

@app.route('/PartApp/suppliers/<int:sid>',
           methods=['GET', 'PUT', 'DELETE'])
def getSupplierById(sid):
    if request.method == 'GET':
        return SupplierHandler().getSupplierById(sid)
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify(Error = "Method not allowed"), 405


@app.route('/PartApp/suppliers/<int:sid>/parts')
def getPartsBySuplierId(sid):
    return SupplierHandler().getPartsBySupplierId(sid)

@app.route('/PartApp/parts/countbypartid')
def getCountByPartId():
    return PartHandler().getCountByPartId()

@app.route('/PartApp/parts/resourcesQuantity')
def getreQuantity():
    return ResourcesHandler().getreQuantity()

@app.route('/PartApp/parts/addrequest', methods=['GET', 'POST'])
def addrequest():
    if request.method == 'POST':  # this block is only entered when the form is submitted
        Date = request.form.get('Date')
        Address = request.form['Address']
        Quantity = request.form['Quantity']
        if Address and Quantity and Date:
            RequestHandler.addrequest(Date,Address,Quantity)
            return'<h1>Added</h1>'
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400
    return '''<form method="POST">
                      Date: <input type="text" name="Date"><br>
                      Address: <input type="text" name="Address"><br>
                      Quantity: <input type="text" name="Quantity"><br>
                      <input type="submit" value="Submit"><br>
              </form>'''

@app.route('/PartApp/parts/resourcesRequested')
def getresourcesRequestedy():
    return ResourcesHandler().getresourcesRequested()

@app.route('/ResourceManagement/resources/resourcesAvailable')
def getresourcesAvailable():

    return ResourcesHandler().getresourcesAvailable()

@app.route('/ResourceManagement/resources/searchresourcesAvailable', methods=['GET', 'POST'])
def searchresourcesAvailable():
    if request.method == 'POST':  # this block is only entered when the form is submitted
        Name = request.form.get('Name')
        if Name:
            return ResourcesHandler().searchresourcesAvailable(Name)
        else:
            return jsonify(Error="Unexpected attributes in request"), 400
    return '''<form method="POST">
                          Name: <input type="text" name="Name"><br>
                          <input type="submit" value="Submit"><br>
                  </form>'''






if __name__ == '__main__':
    app.run()