from flask import jsonify
from dao.purchase import PurchaseDAO

class PurchaseHandler:


    def purchase(Date,Address,Quantity,Cost):
        dao = PurchaseDAO()
        dao.purchase(Date,Address,Quantity,Cost)

    def reserve(Date,Address,Quantity,Cost):
        dao = PurchaseDAO()
        dao.reserve(Date,Address,Quantity,Cost)