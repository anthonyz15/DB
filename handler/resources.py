from flask import jsonify
from dao.resources import ResourcesDAO

class ResourcesHandler:
    def build_resources_quantity(self, row):
        result = {}
        result['rid'] = row[0]
        result['name'] = row[1]
        result['rquantity'] = row[2]
        result['rprice'] = row[3]
#        result['rlocation'] = row[4]
        return result

    def build_resources_Requested(self, row):
        result = {}
        result['name'] = row[0]
        result['rprice'] = row[1]
        result['quantity'] = row[2]
        result['date'] = row[3]
        #        result['rlocation'] = row[4]
        return result

    def build_resources_Available(self, row):
            result = {}
            result['name'] = row[0]
            result['type'] = row[1]
            result['rquantity'] = row[2]
            result['rlocation'] = row[3]
            return result

    def getreQuantity(self):
        dao = ResourcesDAO()
        result = dao.getreQuantity()
        result_list = []
        for row in result:
            result = self.build_resources_quantity(row)
            result_list.append(result)
        return jsonify(PartCounts = result_list), 200

    def getresourcesRequested(self):
        dao = ResourcesDAO()
        result = dao.getresourcesRequested()
        result_list = []
        for row in result:
            result = self.build_resources_Requested(row)
            result_list.append(result)
        return jsonify(PartCounts = result_list), 200

    def getresourcesAvailable(self):
        dao = ResourcesDAO()
        result = dao.getresourcesAvailable()
        result_list = []
        for row in result:
            result = self.build_resources_Available(row)
            result_list.append(result)
        return jsonify(PartCounts = result_list), 200