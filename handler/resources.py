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
    def build_resources_AnnounceAvailability(self, row):
        result = {}
        result['name'] = row[0]
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

    def build_resources_addresources(rname, rquantity, rprice, type, rlocation):
        result = {}
        result['Name'] = rname
        result['Quantity'] = rquantity
        result['Price'] = rprice
        result['Type'] = type
        result['Location'] = rlocation
        return result

    def build_dailyResourcesAvailable(self,row):
        result = {}
        result['Name'] = row[0]
        result['Location'] = row[1]
        result['Quantity'] = row[2]
        return result

    def build_locationMatch(self,row):
        result = {}
        result['Resources'] = row[0]
        result['Available'] = row[1]
        result['Needed'] = row[2]
        result['Location'] = row[3]
        return result

    def build_locationAvailable(self,row):
        result = {}
        result['Resources'] = row[0]
        result['Location'] = row[1]
        result['Quantity'] = row[2]
        return result

    def build_locationNeeded(self,row):
        result = {}
        result['Resources'] = row[0]
        result['Quantity'] = row[1]
        result['Location'] = row[2]
        return result


    def getreAvailability(self):
        dao = ResourcesDAO()
        result = dao.getreAvailability()
        result_list = []
        for row in result:
            result = self.build_resources_Availability(row)
            result_list.append(result)
        return jsonify(Availability = result_list), 200

    def getreAnnounceAvailability(self):
        dao = ResourcesDAO()
        result = dao.getreAnnounceAvailability()
        result_list = []
        for row in result:
            result = self.build_resources_AnnounceAvailability(row)
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


    def dailyResourcesAvailable(self):
        dao = ResourcesDAO()
        result = dao.dailyResourcesAvailable()
        result_list = []
        for row in result:
            result = self.build_dailyResourcesAvailable(row)
            result_list.append(result)
        return jsonify(dailyResourcesAvailable=result_list), 200

    def locationMatching(self):
        dao = ResourcesDAO()
        result = dao.locationMatching()
        result_list = []
        for row in result:
            result = self.build_locationMatch(row)
            result_list.append(result)
        return jsonify(locationMatching=result_list), 200

    def locationAvailable(self):
        dao = ResourcesDAO()
        result = dao.locationAvailable()
        result_list = []
        for row in result:
            result = self.build_locationAvailable(row)
            result_list.append(result)
        return jsonify(locationAvailable=result_list), 200

    def locationNeeded(self):
        dao = ResourcesDAO()
        result = dao.locationNeeded()
        result_list = []
        for row in result:
            result = self.build_locationNeeded(row)
            result_list.append(result)
        return jsonify(locationNeeded=result_list), 200

    def insertresourcesJson(json):
        rname = json['rname']
        rquantity = json['rquantity']
        rprice = json['rprice']
        type = json['rtype']
        rlocation = json['rlocation']
        if rname and rquantity and rprice and type and rlocation:
            dao = ResourcesDAO()
            pid = dao.insertresources(rname, rquantity, rprice, type, rlocation)
            result = ResourcesHandler.build_resources_addresources(rname, rquantity, rprice, type, rlocation)
            return jsonify(Resources=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400