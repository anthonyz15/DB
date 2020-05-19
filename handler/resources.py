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

    def build_resources_addresourcesDetail(rname, rquantity, rprice, type, rlocation,description,brand):
        result = {}
        result['Name'] = rname
        result['Quantity'] = rquantity
        result['Price'] = rprice
        result['Type'] = type
        result['Location'] = rlocation
        result['Descrption'] = description
        result['Brand'] = brand
        return result

    def build_dailyResourcesAvailable(self,row):
        result = {}
        result['Name'] = row[0]
        result['Location'] = row[1]
        result['Quantity'] = row[2]
        return result

    def build_dailyMatching(self, row):
        result = {}
        result['Name'] = row[0]
        result['Available'] = row[3]
        result['Needed'] = row[2]
        result['Address'] = row[1]
        return result

    def build_weeklyMatching(self, row):
        result = {}
        result['Name'] = row[1]
        result['Available'] = row[3]
        result['Needed'] = row[2]
        result['Date'] = row[0]
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


###########################resources details get#############################
    def getwater(self):
        dao = ResourcesDAO()
        result = dao.getwater()
        result_list = []
        for row in result:
            result = self.build_resources_Availability(row)
            result_list.append(result)
        return jsonify(Waters=result_list), 200

    def getfood(self):
        dao = ResourcesDAO()
        result = dao.getfood()
        result_list = []
        for row in result:
            result = self.build_resources_Availability(row)
            result_list.append(result)
        return jsonify(foods=result_list), 200

    def getmedications(self):
        dao = ResourcesDAO()
        result = dao.getmedications()
        result_list = []
        for row in result:
            result = self.build_resources_Availability(row)
            result_list.append(result)
        return jsonify(medications=result_list), 200

    def getfuel(self):
        dao = ResourcesDAO()
        result = dao.getfuel()
        result_list = []
        for row in result:
            result = self.build_resources_Availability(row)
            result_list.append(result)
        return jsonify(fuels=result_list), 200

    def getmedicaldevices(self):
        dao = ResourcesDAO()
        result = dao.getmedicaldevices()
        result_list = []
        for row in result:
            result = self.build_resources_Availability(row)
            result_list.append(result)
        return jsonify(medicaldevices=result_list), 200

    def getheavyequipment(self):
        dao = ResourcesDAO()
        result = dao.getheavyequipment()
        result_list = []
        for row in result:
            result = self.build_resources_Availability(row)
            result_list.append(result)
        return jsonify(heavyequipment=result_list), 200

    def gettools(self):
        dao = ResourcesDAO()
        result = dao.gettools()
        result_list = []
        for row in result:
            result = self.build_resources_Availability(row)
            result_list.append(result)
        return jsonify(tools=result_list), 200

    def getclothing(self):
        dao = ResourcesDAO()
        result = dao.getclothing()
        result_list = []
        for row in result:
            result = self.build_resources_Availability(row)
            result_list.append(result)
        return jsonify(clothing=result_list), 200

    def getpowergenerators(self):
        dao = ResourcesDAO()
        result = dao.getpowergenerators()
        result_list = []
        for row in result:
            result = self.build_resources_Availability(row)
            result_list.append(result)
        return jsonify(powergenerators=result_list), 200

    def getbatteries(self):
        dao = ResourcesDAO()
        result = dao.getbatteries()
        result_list = []
        for row in result:
            result = self.build_resources_Availability(row)
            result_list.append(result)
        return jsonify(batteries=result_list), 200




##############################################################################


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

    def dailyMatching(self,date):
        dao = ResourcesDAO()
        result = dao.dailyMatching(date)
        result_list = []
        for row in result:
            result = self.build_dailyMatching(row)
            result_list.append(result)
        return jsonify(dailyMatching=result_list), 200

    def weeklyMatching(self, date):
        dao = ResourcesDAO()
        result = dao.weeklyMatching(date)
        result_list = []
        for row in result:
            result = self.build_weeklyMatching(row)
            result_list.append(result)
        return jsonify(weeklyMatching=result_list), 200


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
        description= json['description']
        brand = json['brand']
        if rname and rquantity and rprice and type and rlocation and description and brand:
            if rname=="water":
                dao = ResourcesDAO()
                pid = dao.insertwater(rname, rquantity, rprice, type, rlocation,description,brand)
                result = ResourcesHandler.build_resources_addresourcesDetail(rname, rquantity, rprice, type, rlocation,description,brand)
                return jsonify(Water=result), 200
            elif rname=="food":
                dao = ResourcesDAO()
                pid = dao.insertfood(rname, rquantity, rprice, type, rlocation, description, brand)
                result = ResourcesHandler.build_resources_addresourcesDetail(rname, rquantity, rprice, type, rlocation,description, brand)
                return jsonify(Water=result), 200
            elif rname=="medications":
                dao = ResourcesDAO()
                pid = dao.insertmedications(rname, rquantity, rprice, type, rlocation, description, brand)
                result = ResourcesHandler.build_resources_addresourcesDetail(rname, rquantity, rprice, type, rlocation,description, brand)
                return jsonify(Water=result), 200
            elif rname=="ice":
                dao = ResourcesDAO()
                pid = dao.insertice(rname, rquantity, rprice, type, rlocation, description, brand)
                result = ResourcesHandler.build_resources_addresourcesDetail(rname, rquantity, rprice, type, rlocation, description, brand)
                return jsonify(Water=result), 200
            elif rname=="fuel":
                dao = ResourcesDAO()
                pid = dao.insertfuel(rname, rquantity, rprice, type, rlocation, description, brand)
                result = ResourcesHandler.build_resources_addresourcesDetail(rname, rquantity, rprice, type, rlocation,description, brand)
                return jsonify(Water=result), 200
            elif rname=="medicaldevices":
                dao = ResourcesDAO()
                pid = dao.insertmedicaldevices(rname, rquantity, rprice, type, rlocation, description, brand)
                result = ResourcesHandler.build_resources_addresourcesDetail(rname, rquantity, rprice, type, rlocation,description, brand)
                return jsonify(Water=result), 200
            elif rname=="heavyequipment":
                dao = ResourcesDAO()
                pid = dao.insertheavyequipment(rname, rquantity, rprice, type, rlocation, description, brand)
                result = ResourcesHandler.build_resources_addresourcesDetail(rname, rquantity, rprice, type, rlocation,description, brand)
                return jsonify(Water=result), 200
            elif rname=="tools":
                dao = ResourcesDAO()
                pid = dao.inserttools(rname, rquantity, rprice, type, rlocation, description, brand)
                result = ResourcesHandler.build_resources_addresourcesDetail(rname, rquantity, rprice, type, rlocation,description, brand)
                return jsonify(Water=result), 200
            elif rname=="clothing":
                dao = ResourcesDAO()
                pid = dao.insertclothing(rname, rquantity, rprice, type, rlocation, description, brand)
                result = ResourcesHandler.build_resources_addresourcesDetail(rname, rquantity, rprice, type, rlocation,description, brand)
                return jsonify(Water=result), 200
            elif rname=="powergenerators":
                dao = ResourcesDAO()
                pid = dao.insertpowergenerators(rname, rquantity, rprice, type, rlocation, description, brand)
                result = ResourcesHandler.build_resources_addresourcesDetail(rname, rquantity, rprice, type, rlocation,description, brand)
                return jsonify(Water=result), 200
            elif rname=="batteries":
                dao = ResourcesDAO()
                pid = dao.insertbatteries(rname, rquantity, rprice, type, rlocation, description, brand)
                result = ResourcesHandler.build_resources_addresourcesDetail(rname, rquantity, rprice, type, rlocation,description, brand)
                return jsonify(Water=result), 200
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400
        elif rname and rquantity and rprice and type and rlocation:
                dao = ResourcesDAO()
                pid = dao.insertresources(rname, rquantity, rprice, type, rlocation)
                result = ResourcesHandler.build_resources_addresources(rname, rquantity, rprice, type, rlocation)
                return jsonify(Water=result), 200
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400