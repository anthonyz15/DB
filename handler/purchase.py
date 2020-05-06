from flask import jsonify
from dao.purchase import PurchaseDAO

class PurchaseHandler:

    def build_resources_purchase(self,row):
        result = {}
        result['Date'] = row[0]
        result['Address'] = row[1]
        result['Quantity'] = row[2]
        result['Cost'] = row[3]
        return result

    def build_resources_Order(self,row):
        result = {}
        result['Date'] = row[0]
        result['Address'] = row[1]
        result['TotalPrice'] = row[2]
        return result

    '''def purchase(Date,Address,Quantity,Cost):
        dao = PurchaseDAO()
        result=dao.purchase(Date,Address,Quantity,Cost)
        result_list = []
        for row in result:
            result = PurchaseHandler.build_resources_purchase(row)
            result_list.append(result)
        return jsonify(Purchase=result_list), 200

    def reserve(Date,Address,Quantity,Cost):
        dao = PurchaseDAO()
        result=dao.reserve(Date,Address,Quantity,Cost)
        result_list = []
        for row in result:
            result = PurchaseHandler.build_resources_purchase(row)
            result_list.append(result)
        return jsonify(Reserve=result_list), 200'''

    def getPurchase(self):
        dao = PurchaseDAO()
        result=dao.getPurchase()
        result_list = []
        for row in result:
            result = self.build_resources_purchase(row)
            result_list.append(result)
        return jsonify(Purchases=result_list), 200
    def searchPurchasebyId(self,id):
        dao = PurchaseDAO()
        result=dao.searchPurchasebyId(id)
        result_list = []
        for row in result:
            result = self.build_resources_purchase(row)
            result_list.append(result)
        return jsonify(Purchase=result_list), 200

    def getOrderPurchase(self):
        dao = PurchaseDAO()
        result=dao.getOrderPurchase()
        result_list = []
        for row in result:
            result = self.build_resources_Order(row)
            result_list.append(result)
        return jsonify(Purchases=result_list), 200
    def searchOrderPurchasebyId(self,id):
        dao = PurchaseDAO()
        result=dao.searchOrderPurchasebyId(id)
        result_list = []
        for row in result:
            result = self.build_resources_Order(row)
            result_list.append(result)
        return jsonify(Purchase=result_list), 200

    def getOrderReserve(self):
        dao = PurchaseDAO()
        result=dao.getOrderReserve()
        result_list = []
        for row in result:
            result = self.build_resources_Order(row)
            result_list.append(result)
        return jsonify(Reserves=result_list), 200
    def searchOrderReservebyId(self,id):
        dao = PurchaseDAO()
        result=dao.searchOrderReservebyId(id)
        result_list = []
        for row in result:
            result = self.build_resources_Order(row)
            result_list.append(result)
        return jsonify(Purchase=result_list), 200