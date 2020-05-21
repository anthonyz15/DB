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

    def build_resources_Orderbycoid(self,row):
        result = {}
        result['Name'] = row[0]
        result['Lastname'] = row[1]
        result['Address'] = row[3]
        result['Price'] = row[2]
        result['Date'] = row[4]
        return result

    def build_resources_addOrder(odate,olocation,totalprice):
        result = {}
        result['Date'] = odate
        result['Location'] = olocation
        result['TotalPrice'] = totalprice
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

    def getPurchasebyCoid(self, coid):
        dao = PurchaseDAO()
        result = dao.getPurchasebyCoid(coid)
        result_list = []
        for row in result:
            result = self.build_resources_Orderbycoid(row)
            result_list.append(result)
        return jsonify(PurchasebyCoid=result_list), 200

    def getReservebyCoid(self, coid):
        dao = PurchaseDAO()
        result = dao.getReservebyCoid(coid)
        result_list = []
        for row in result:
            result = self.build_resources_Orderbycoid(row)
            result_list.append(result)
        return jsonify(ReservebyCoid=result_list), 200

    def insertOrderJson(json):
        odate = json['odate']
        olocation = json['olocation']
        totalprice= json['totalprice']
        coid = json['coid']
        rid = json['rid']
        quantity = json['quantity']
        if odate and olocation and totalprice and coid and rid and quantity:
            dao = PurchaseDAO()
            pid = dao.insertOrder(odate, olocation, totalprice)
            if totalprice>0:
                dao.insertpurchases(pid, coid)
            else:
                dao.insertreserves(pid, coid)
            for i in range(len(rid)):
                dao.insertcontains(pid, rid[i], quantity[i])
            result = PurchaseHandler.build_resources_addOrder(odate,olocation,totalprice)
            return jsonify(request=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400