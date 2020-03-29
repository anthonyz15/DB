from flask import Flask, jsonify, request,redirect, url_for
from handler.resources import ResourcesHandler
from handler.request import RequestHandler
from handler.register import RegisterHandler
from handler.purchase import PurchaseHandler
# Import Cross-Origin Resource Sharing to enable
# services on other ports on this machine or on other
# machines to access this app
from flask_cors import CORS, cross_origin

# Activate
app = Flask(__name__)
# Apply CORS to this app
CORS(app)

systempass="!@#$%^&*()"
admin=False



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
                      <h1> Add request</h1>
                      Date: <input type="text" name="Date"><br>
                      Address: <input type="text" name="Address"><br>
                      Quantity: <input type="text" name="Quantity"><br>
                      <input type="submit" value="Submit"><br>
              </form>'''

@app.route('/ResourceManagement/resources/resourcesRequested')
def getresourcesRequested():
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

@app.route('/ResourceManagement/resources/signup', methods=['GET', 'POST'])
def signup():
    global admin
    if request.method == 'POST':  # this block is only entered when the form is submitted
        username = request.form.get('username')
        password = request.form['password']
        email = request.form['Email']
        if email and username and password:
            RegisterHandler.signup(username, password, email)
            admin=False
            return '<h1>Thanks for the registration</h1>'
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400
    return '''<form method="POST">
                      Username: <input type="text" name="username"><br>
                      Password: <input type="password" name="password"><br>
                      Email: <input type="text" name="Email"><br>
                      <input type="submit" value="Sign up"><br>
                  </form>'''

@app.route('/ResourceManagement/resources/signup/admin', methods=['GET', 'POST'])
def admin():
    global admin
    if request.method == 'POST':  # this block is only entered when the form is submitted
        password = request.form['password']
        if systempass==password:
            admin=True
            return redirect(url_for('signup'))
        else:
            return jsonify(Error="Password incorrect"), 400
    return '''<form method="POST">
                      <h1> Register as admin</h1>
                      System Password: <input type="password" name="password"><br>
                      <input type="submit" value="Submit"><br>
                  </form>'''

@app.route('/ResourceManagement/resources/purchase', methods=['GET', 'POST'])
def purchase():
    if request.method == 'POST':  # this block is only entered when the form is submitted
        Date = request.form.get('Date')
        Address = request.form['Address']
        Quantity = request.form['Quantity']
        Cost = request.form['Cost']
        if Address and Quantity and Date and Cost:
            Cost=int(Cost)
            if Cost<1:
                PurchaseHandler.reserve(Date,Address,Quantity,Cost)
                return'<h1>reserve Added</h1>'
            else:
                PurchaseHandler.purchase(Date, Address, Quantity, Cost)
                return '<h1>purchase Added</h1>'
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400
    return '''<form method="POST">
                      Date: <input type="text" name="Date"><br>
                      Address: <input type="text" name="Address"><br>
                      Quantity: <input type="text" name="Quantity"><br>
                      Cost: <input type="text" name="Cost"><br>
                      <input type="submit" value="Submit"><br>
              </form>'''


if __name__ == '__main__':
    app.run()