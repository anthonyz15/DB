from flask import jsonify
from dao.register import RegisterDAO

class RegisterHandler:

    def build_resources_register(self,row):
        result = {}
        result['firstname'] = row[0]
        result['lastname'] = row[1]
        return result

    def build_resources_register2(self,row):
        result = {}
        result['firstname'] = row[0]
        result['lastname'] = row[1]
        result['address'] = row[2]
        return result
    def build_resources_users(self,row):
        result = {}
        result['username'] = row[0]
        result['password'] = row[1]
        result['email'] = row[2]
        return result

    def build_resources_addAdmin(uname,passwrd,email,firstname,lastname):
        result = {}
        result['Username'] = uname
        result['Password'] = passwrd
        result['Email'] = email
        result['Firstname'] = firstname
        result['Lastname'] = lastname
        return result


    def signup(self,username, password, email):
        dao = RegisterDAO()
        result=dao.signup(username, password, email)
        result_list = []
        for row in result:
            result = self.build_resources_register(row)
            result_list.append(result)
        return jsonify(Users=result_list), 200

    def Admin(self,username, password, email):
        dao = RegisterDAO()
        result=dao.signup(username, password, email)
        result_list = []
        for row in result:
            result = self.build_resources_register(row)
            result_list.append(result)
        return jsonify(Admins=result_list), 200

    def getUsers(self):
        dao = RegisterDAO()
        result=dao.getUsers()
        result_list = []
        for row in result:
            result = self.build_resources_users(row)
            result_list.append(result)
        return jsonify(Users=result_list), 200

    def searchUsersbyId(self,id):
        dao = RegisterDAO()
        result=dao.searchUsersbyId(id)
        result_list = []
        for row in result:
            result = self.build_resources_users(row)
            result_list.append(result)
        return jsonify(User=result_list), 200

    def getAdmins(self):
        dao = RegisterDAO()
        result=dao.getAdmins()
        result_list = []
        for row in result:
            result = self.build_resources_register(row)
            result_list.append(result)
        return jsonify(Admins=result_list), 200

    def searchAdmin(self,admin):
        dao = RegisterDAO()
        result=dao.searchAdmin(admin)
        result_list = []
        for row in result:
            result = self.build_resources_register(row)
            result_list.append(result)
        return jsonify(Admins=result_list), 200

    def getsupplier(self):
        dao = RegisterDAO()
        result=dao.getsupplier()
        result_list = []
        for row in result:
            result = self.build_resources_register2(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list), 200
    def searchsupplierbyId(self,supplier):
        dao = RegisterDAO()
        result=dao.searchsupplierbyId(supplier)
        result_list = []
        for row in result:
            result = self.build_resources_register2(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list), 200

    def getConsumers(self):
        dao = RegisterDAO()
        result=dao.getConsumers()
        result_list = []
        for row in result:
            result = self.build_resources_register2(row)
            result_list.append(result)
        return jsonify(Consumers=result_list), 200
    def searchConsumersbyId(self,id):
        dao = RegisterDAO()
        result=dao.searchConsumersbyId(id)
        result_list = []
        for row in result:
            result = self.build_resources_register2(row)
            result_list.append(result)
        return jsonify(Consumers=result_list), 200


    def insertAdminJson(json):
        uname = json['uname']
        passwrd = json['passwrd']
        email= json['email']
        firstname = json['firstname']
        lastname = json['lastname']
        if uname and passwrd and email and firstname and lastname:
            dao = RegisterDAO()
            pid = dao.insertAdmin(uname,passwrd,email,firstname,lastname)
            result = RegisterHandler.build_resources_addAdmin(uname,passwrd,email,firstname,lastname)
            return jsonify(Admin=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400