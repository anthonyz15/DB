from flask import jsonify
from dao.request import RequestDAO

class RequestHandler:


    def addrequest(date,adress,quantity):
        dao = RequestDAO()
        dao.addrequest(date,quantity,adress)