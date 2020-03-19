from flask import jsonify
from dao.request import RequestDAO

class RequestHandler:

    def build_requested(self, row):
        result = {}
        result['rqname'] = row[0]
        result['type'] = row[1]
        result['rquantity'] = row[2]
        result['rqlocation'] = row[3]
        return result


    def addrequest(date,adress,quantity):
        dao = RequestDAO()
        dao.addrequest(date,quantity,adress)

    def searchrequested(self,name):
        dao = RequestDAO()
        result = dao.searchrequested(name)
        result_list = []
        for row in result:
            result = self.build_requested(row)
            result_list.append(result)
        return jsonify(PartCounts = result_list), 200