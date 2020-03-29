from flask import jsonify
from dao.register import RegisterDAO

class RegisterHandler:


    def signup(username, password, email):
        dao = RegisterDAO()
        dao.signup(username, password, email)