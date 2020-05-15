from flask import jsonify
from dao.company import CompanyDAO

class CompanyHandler:


    def build_resources_addcompany(name,location):
        result = {}
        result['Name'] = name
        result['Location'] = location
        return result

    def getCompany(self):
        dao = CompanyDAO()
        result = dao.getCompany()
        result_list = []
        for row in result:
            result = self.build_resources_request(row)
            result_list.append(result)
        return jsonify(Companies=result_list), 200

    def insertcompanyJson(json):
        name = json['name']
        location = json['location']
        if name and location:
            dao = CompanyDAO()
            pid = dao.insertcompany(name, location)
            result = CompanyHandler.build_resources_addcompany(name, location)
            return jsonify(Company=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400