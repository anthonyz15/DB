from flask import jsonify
from dao.request import RequestDAO

class RequestHandler:

    def build_requested(self, row):
        result = {}
        result['rqname'] = row[0]
        result['type'] = row[1]
        result['rqquantity'] = row[2]
        result['rqaddress'] = row[3]
        result['rqdate'] = row[4]
        return result
    def build_resources_addrequest(self,row):
        result = {}
        result['Date'] = row[0]
        result['Quantity'] = row[1]
        result['Address'] = row[2]
        return result
    def build_resources_request(self,row):
        result = {}
        result['Address'] = row[0]
        result['Quantity'] = row[1]
        result['Date'] = row[2]
        return result
    def build_resources_addrequest(rqaddress,quantity,rqdate):
        result = {}
        result['Address'] = rqaddress
        result['Quantity'] = quantity
        result['Date'] = rqdate
        return result
    def build_resources_requestbycoid(self,row):
        result = {}
        result['Name'] = row[0]
        result['Lastname'] = row[1]
        result['Address'] = row[2]
        result['Quantity'] = row[3]
        result['Date'] = row[4]
        return result
    def build_dailyinneed(self,row):
        result = {}
        result['Name'] = row[0]
        result['Quantity'] = row[1]
        result['Date'] = row[2]
        return result


    def addrequest(date,adress,quantity):
        dao = RequestDAO()
        result=dao.addrequest(date,quantity,adress)
        result_list = []
        for row in result:
            result = RequestHandler.build_resources_addrequest(row)
            result_list.append(result)
        return jsonify(Requested=result_list), 200

    def searchrequested(self,name):
        dao = RequestDAO()
        result = dao.searchrequested(name)
        result_list = []
        for row in result:
            result = self.build_requested(row)
            result_list.append(result)
        return jsonify(Search_Requested = result_list), 200

    def getrequest(self):
        dao = RequestDAO()
        result = dao.getrequest()
        result_list = []
        for row in result:
            result = self.build_resources_request(row)
            result_list.append(result)
        return jsonify(Requests=result_list), 200

    def searchrequest(self, request):
        dao = RequestDAO()
        result = dao.searchrequest(request)
        result_list = []
        for row in result:
            result = self.build_resources_request(row)
            result_list.append(result)
        return jsonify(Request=result_list), 200

    def getRequestbyCoid(self, coid):
        dao = RequestDAO()
        result = dao.getRequestbyCoid(coid)
        result_list = []
        for row in result:
            result = self.build_resources_requestbycoid(row)
            result_list.append(result)
        return jsonify(RequestbyCoid=result_list), 200

    def dailyResourcesinNeed(self,date):
        dao = RequestDAO()
        result = dao.dailyResourcesinNeed(date)
        result_list = []
        for row in result:
            result = self.build_dailyinneed(row)
            result_list.append(result)
        return jsonify(ResourcesinNeed=result_list), 200

    def build_weeklyinneed(self, row):
        result = {}
        result['Name'] = row[0]
        result['Quantity'] = row[1]
        result['Date'] = row[2]
        return result

    def weeklyResourcesinNeed(self, date):
        dao = RequestDAO()
        result = dao.weeklyResourcesinNeed(date)
        result_list = []
        for row in result:
            result = self.build_weeklyinneed(row)
            result_list.append(result)
        return jsonify(ResourcesinNeed=result_list), 200

    def insertrequestJson(json):
        rqaddress = json['rqaddress']
        quantity = json['quantity']
        rqdate = json['rqdate']
        if rqaddress and quantity and rqdate:
            dao = RequestDAO()
            pid = dao.insertrequest(rqaddress,quantity,rqdate)
            result = RequestHandler.build_resources_addrequest(rqaddress,quantity,rqdate)
            return jsonify(request=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400
