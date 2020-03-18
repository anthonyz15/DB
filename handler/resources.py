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

    def getreQuantity(self):
        dao = ResourcesDAO()
        result = dao.getreQuantity()
        result_list = []
        for row in result:
            result = self.build_resources_quantity(row)
            result_list.append(result)
        return jsonify(PartCounts = result_list), 200