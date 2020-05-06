from flask import jsonify
from dao.resources import ResourcesDAO

class ResourcesHandler:
    def build_resources_Availability(self, row):
        result = {}
        result['name'] = row[0]
        result['rquantity'] = row[1]
        result['rprice'] = row[2]
        result['rlocation'] = row[3]
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

    def build_resources_sAvailable(self, row):
        result = {}
        result['name'] = row[0]
        result['type'] = row[1]
        result['quantity'] = row[2]
        result['price'] = row[3]
        result['location'] = row[4]
        return result

    def getreAvailability(self):
        dao = ResourcesDAO()
        result = dao.getreAvailability()
        result_list = []
        for row in result:
            result = self.build_resources_Availability(row)
            result_list.append(result)
        return jsonify(Availability = result_list), 200

    def getresourcesRequested(self):
        dao = ResourcesDAO()
        result = dao.getresourcesRequested()
        result_list = []
        for row in result:
            result = self.build_resources_Requested(row)
            result_list.append(result)
        return jsonify(Resources_requested = result_list), 200

    def getresourcesInRequest(self,id):
        dao = ResourcesDAO()
        result = dao.getresourcesInRequest(id)
        result_list = []
        for row in result:
            result = self.build_resources_Requested(row)
            result_list.append(result)
        return jsonify(Resources_requested = result_list), 200

    def getresourcesAvailable(self):
        dao = ResourcesDAO()
        result = dao.getresourcesAvailable()
        result_list = []
        for row in result:
            result = self.build_resources_Available(row)
            result_list.append(result)
        return jsonify(Resources = result_list), 200

    def searchresourcesAvailable(self,name):
        dao = ResourcesDAO()
        result = dao.searchresourcesAvailable(name)
        result_list = []
        for row in result:
            result = self.build_resources_sAvailable(row)
            result_list.append(result)
        return jsonify(ResourcesCount = result_list), 200

    def getresourcesDetails(self):
        dao = ResourcesDAO()
        result = dao.getresourcesDetails()
        result_list = []
        for row in result:
            result = self.build_resources_Availability(row)
            result_list.append(result)
        return jsonify(PartCounts = result_list), 200


    def searchResourcesbyId(self,id):
        dao = ResourcesDAO()
        result = dao.searchResourcesbyId(id)
        result_list = []
        for row in result:
            result = self.build_resources_Availability(row)
            result_list.append(result)
        return jsonify(ResourcesCount = result_list), 200