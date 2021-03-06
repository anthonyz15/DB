from flask import Flask, jsonify, request,redirect, url_for
from handler.resources import ResourcesHandler
from handler.request import RequestHandler
from handler.register import RegisterHandler
from handler.purchase import PurchaseHandler
from handler.company import CompanyHandler
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

#get of all isa table from resources##############

@app.route('/ResourceManagement/resources/water')
def getwater():
    return ResourcesHandler().getwater()

@app.route('/ResourceManagement/resources/food')
def getfood():
    return ResourcesHandler().getfood()

@app.route('/ResourceManagement/resources/ice')
def getice():
    return ResourcesHandler().getice()

@app.route('/ResourceManagement/resources/medications')
def getmedications():
    return ResourcesHandler().getmedications()

@app.route('/ResourceManagement/resources/fuel')
def getfuel():
    return ResourcesHandler().getfuel()

@app.route('/ResourceManagement/resources/medicaldevices')
def getmedicaldevices():
    return ResourcesHandler().getmedicaldevices()

@app.route('/ResourceManagement/resources/heavyequipment')
def getheavyequipment():
    return ResourcesHandler().getheavyequipment()

@app.route('/ResourceManagement/resources/tools')
def gettools():
    return ResourcesHandler().gettools()

@app.route('/ResourceManagement/resources/clothing')
def getclothing():
    return ResourcesHandler().getclothing()

@app.route('/ResourceManagement/resources/powergenerators')
def getpowergenerators():
    return ResourcesHandler().getpowergenerators()

@app.route('/ResourceManagement/resources/batteries')
def getbatteries():
    return ResourcesHandler().getbatteries()

#######################################################################



@app.route('/ResourceManagement/resources/resourcesAvailability')
def getreAvailability():
    return ResourcesHandler().getreAvailability()

@app.route('/ResourceManagement/resources/resourcesAnnounceAvailability')
def getreAnnounceAvailability():
    return ResourcesHandler().getreAnnounceAvailability()

@app.route('/ResourceManagement/resources/dailyResourcesinNeed', methods=['GET', 'POST'])
def dailyResourcesinNeed():
        if not request.args:
            return jsonify(Error="Missing value"), 400
        else:
            return RequestHandler().dailyResourcesinNeed(request.args.get('value'))

@app.route('/ResourceManagement/resources/dailyResourcesAvailable', methods=['GET', 'POST'])
def dailyResourcesAvailable():
    return ResourcesHandler().dailyResourcesAvailable()

@app.route('/ResourceManagement/resources/dailyMatching', methods=['GET', 'POST'])
def dailyMatching():
        if not request.args:
            return jsonify(Error="Missing value"), 400
        else:
            return ResourcesHandler().dailyMatching(request.args.get('value'))

@app.route('/ResourceManagement/resources/weeklyResourcesinNeed', methods=['GET', 'POST'])
def weeklyResourcesinNeed():
        if not request.args:
            return jsonify(Error="Missing value"), 400
        else:
            return RequestHandler().weeklyResourcesinNeed(request.args.get('value'))

@app.route('/ResourceManagement/resources/weeklyMatching', methods=['GET', 'POST'])
def weeklyMatching():
        if not request.args:
            return jsonify(Error="Missing value"), 400
        else:
            return ResourcesHandler().weeklyMatching(request.args.get('value'))




@app.route('/ResourceManagement/resources/LocationMatching', methods=['GET', 'POST'])
def locationMatching():
    return ResourcesHandler().locationMatching()
@app.route('/ResourceManagement/resources/LocationAvailable', methods=['GET', 'POST'])
def locationAvailable():
    return ResourcesHandler().locationAvailable()

@app.route('/ResourceManagement/resources/LocationNeeded', methods=['GET', 'POST'])
def locationNeeded():
    return ResourcesHandler().locationNeeded()


@app.route('/ResourceManagement/resources/addrequest', methods=['GET', 'POST'])
def addrequest():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return RequestHandler.insertrequestJson(request.json)
    else:
        if not request.args:
            return RequestHandler().getrequest()
        else:
            return RequestHandler().searchrequest(request.args.get('value'))

@app.route('/ResourceManagement/resources/resourcesRequested')
def getresourcesRequested():
    return ResourcesHandler().getresourcesRequested()

@app.route('/ResourceManagement/resources/resourcesRequested')
def getresourcesInRequest():
    if not request.args:  # this block is only entered when the form is submitted
        return jsonify(Error="Missing value"), 400
    else:
        return ResourcesHandler().getresourcesInRequest(request.args.get('value'))


@app.route('/ResourceManagement/resources/searchRequested', methods=['GET', 'POST'])
def searchrequested():
    if not request.args:  # this block is only entered when the form is submitted
        return jsonify(Error="Missing value"), 400
    else:
        return RequestHandler().searchrequested(request.args.get('value'))

@app.route('/ResourceManagement/resources/resourcesDetails')
def getresourcesDetails():
    if request.method == 'POST':
        pass
        #return RequestHandler.insertPartJson(request.json)
    else:
        if not request.args:
            return ResourcesHandler().getresourcesDetails()
        else:
            return ResourcesHandler().searchResourcesbyId(request.args.get('value'))


@app.route('/ResourceManagement/resources/resourcesAvailable')
def getresourcesAvailable():
    return ResourcesHandler().getresourcesAvailable()

@app.route('/ResourceManagement/resources/searchresourcesAvailable', methods=['GET', 'POST'])
def searchresourcesAvailable():
    if not request.args:  # this block is only entered when the form is submitted
        return jsonify(Error="Missing value"), 400
    else:
        return ResourcesHandler().searchresourcesAvailable(request.args.get('value'))

@app.route('/ResourceManagement/resources/addresources', methods=['GET', 'POST'])
def addresources():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ResourcesHandler.insertresourcesJson(request.json)
    else:
        if not request.args:
            return ResourcesHandler().getresourcesAvailable()
        else:
            return ResourcesHandler().searchresourcesAvailable(request.args.get('value'))


@app.route('/ResourceManagement/resources/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        # return RequestHandler.insertPartJson(request.json)
    else:
        if not request.args:
            return RegisterHandler().getUsers()
        else:
            return RegisterHandler().searchUsersbyId(request.args.get('value'))


@app.route('/ResourceManagement/resources/signup/consumer', methods=['GET', 'POST'])
def consumer():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return RegisterHandler.insertConsumerJson(request.json)
    else:
        if not request.args:
            return RegisterHandler().getConsumers()
        else:
            return RegisterHandler().searchConsumersbyId(request.args.get('value'))


@app.route('/ResourceManagement/resources/signup/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return RegisterHandler.insertAdminJson(request.json)
    else:
        if not request.args:
            return RegisterHandler().getAdmins()
        else:
            return RegisterHandler().searchAdmin(request.args.get('value'))

@app.route('/ResourceManagement/resources/signup/supplier', methods=['GET', 'POST'])
def supplier():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return RegisterHandler.insertSupplierJson(request.json)
    else:
        if not request.args:
            return RegisterHandler().getsupplier()
        else:
            return RegisterHandler().searchsupplierbyId(request.args.get('value'))

@app.route('/ResourceManagement/resources/company', methods=['GET', 'POST'])
def addcompany():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return CompanyHandler.insertcompanyJson(request.json)
    else:
        return CompanyHandler().getCompany()



@app.route('/ResourceManagement/resources/purchase', methods=['GET', 'POST'])
def purchase():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        # return RequestHandler.insertPartJson(request.json)
    else:
        if not request.args:
            return PurchaseHandler().getPurchase()
        else:
            return PurchaseHandler().searchPurchasebyId(request.args.get('value'))

@app.route('/ResourceManagement/resources/reserve', methods=['GET', 'POST'])
def reserve():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        # return RequestHandler.insertPartJson(request.json)
    else:
        if not request.args:
            return PurchaseHandler().getReserve()
        else:
            return PurchaseHandler().searchReservebyId(request.args.get('value'))

@app.route('/ResourceManagement/resources/OrderPurchase', methods=['GET', 'POST'])
def OrderPurchase():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return PurchaseHandler.insertOrderJson(request.json)
    else:
        if not request.args:
            return PurchaseHandler().getOrderPurchase()
        else:
            return PurchaseHandler().searchOrderPurchasebyId(request.args.get('value'))

@app.route('/ResourceManagement/resources/OrderReserve', methods=['GET', 'POST'])
def OrderReserve():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return PurchaseHandler.insertOrderJson(request.json)
    else:
        if not request.args:
            return PurchaseHandler().getOrderReserve()
        else:
            return PurchaseHandler().searchOrderReservebyId(request.args.get('value'))


@app.route('/ResourceManagement/resources/purchasebycoid', methods=['GET', 'POST'])
def getPurchasebyCoid():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        # return RequestHandler.insertPartJson(request.json)
    else:
        if not request.args:
            return jsonify(Error="Missing value"), 400
        else:
            return PurchaseHandler().getPurchasebyCoid(request.args.get('value'))

@app.route('/ResourceManagement/resources/reservebycoid', methods=['GET', 'POST'])
def getReservebyCoid():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        # return RequestHandler.insertPartJson(request.json)
    else:
        if not request.args:
            return jsonify(Error="Missing value"), 400
        else:
            return PurchaseHandler().getReservebyCoid(request.args.get('value'))

@app.route('/ResourceManagement/resources/requestbycoid', methods=['GET', 'POST'])
def getRequestbyCoid():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        # return RequestHandler.insertPartJson(request.json)
    else:
        if not request.args:
            pass
        else:
            return RequestHandler().getRequestbyCoid(request.args.get('value'))



if __name__ == '__main__':
    app.run()