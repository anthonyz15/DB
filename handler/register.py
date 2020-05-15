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

    def build_resources_addConsumer(uname, passwrd, email, firstname, lastname, caddress, phone):
        result = {}
        result['Username'] = uname
        result['Password'] = passwrd
        result['Email'] = email
        result['Firstname'] = firstname
        result['Lastname'] = lastname
        result['Address'] = caddress
        result['Phone'] = phone
        return result

    def build_resources_addSupplier(uname, passwrd, email, firstname, lastname, address):
        result = {}
        result['Username'] = uname
        result['Password'] = passwrd
        result['Email'] = email
        result['Firstname'] = firstname
        result['Lastname'] = lastname
        result['Address'] = address
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


    def insertConsumerJson(json):
        uname = json['uname']
        passwrd = json['passwrd']
        email= json['email']
        firstname = json['firstname']
        lastname = json['lastname']
        caddress = json['address']
        phone = json['phone']
        if uname and passwrd and email and firstname and lastname and caddress:
            dao = RegisterDAO()
            pid = dao.insertConsumer(uname,passwrd,email,firstname,lastname,caddress)
            if phone != "":
                dao.insertPhone(pid,phone)
            result = RegisterHandler.build_resources_addConsumer(uname,passwrd,email,firstname,lastname,caddress, phone)
            return jsonify(Consumer=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400


    def insertSupplierJson(json):
        uname = json['uname']
        passwrd = json['passwrd']
        email = json['email']
        firstname = json['firstname']
        lastname = json['lastname']
        address = json['address']
        if uname and passwrd and email and firstname and lastname and address:
            dao = RegisterDAO()
            pid = dao.insertSupplier(uname, passwrd, email, firstname, lastname, address)
            result = RegisterHandler.build_resources_addSupplier(uname, passwrd, email, firstname, lastname, address)
            return jsonify(Supplier=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400