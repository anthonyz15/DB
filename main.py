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



@app.route('/')
def greeting():
    return 'Hello, this is the resources DB App!'


@app.route('/ResourceManagement/resources/resourcesQuantity')
def getreQuantity():
    return ResourcesHandler().getreQuantity()

@app.route('/ResourceManagement/resources/addrequest', methods=['GET', 'POST'])
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

@app.route('/ResourceManagement/resources/resourcesRequested')
def getresourcesRequestedy():
    return ResourcesHandler().getresourcesRequested()

@app.route('/ResourceManagement/resources/resourcesDetails')
def getresourcesDetails():
    return ResourcesHandler().getresourcesDetails()

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

@app.route('/ResourceManagement/resources/searchRequested', methods=['GET', 'POST'])
def searchrequested():
    if request.method == 'POST':  # this block is only entered when the form is submitted
        Name = request.form.get('Name')
        if Name:
            return RequestHandler().searchrequested(Name)
        else:
            return jsonify(Error="Unexpected attributes in request"), 400
    return '''<form method="POST">
                          Name: <input type="text" name="Name"><br>
                          <input type="submit" value="Submit"><br>
                  </form>'''



if __name__ == '__main__':
    app.run()