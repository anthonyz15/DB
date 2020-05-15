from config.dbconfig import pg_config
import psycopg2
class RegisterDAO:
    global list,list1
    list=set()
    list1=set()
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def signup(self,username, password, email):
        print(username, password, email)
        list.add((username, password, email))
        return list

    def Admin(self,username, password, email):
        print(username, password, email)
        list1.add((username, password, email))
        return list1
    def getAdmins(self):
        cursor = self.conn.cursor()
        query = "select firstname,lastname from admins"
        cursor.execute(query)
        result=[]
        for row in cursor:
            result.append(row)
        return result

    def searchAdmin(self,admin):
        cursor = self.conn.cursor()
        query = "select firstname,lastname from admins where adminid= %s "
        cursor.execute(query,(admin,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getUsers(self):
        cursor = self.conn.cursor()
        query = "select uname,passwrd,email from users"
        cursor.execute(query)
        result=[]
        for row in cursor:
            result.append(row)
        return result

    def searchUsersbyId(self,id):
        cursor = self.conn.cursor()
        query = "select uname,passwrd,email from users where uid= %s "
        cursor.execute(query,(id,))
        result = []
        for row in cursor:
            result.append(row)
        return result



    def getsupplier(self):
        cursor = self.conn.cursor()
        query = "select firstname,lastname,address from supplier"
        cursor.execute(query)
        result=[]
        for row in cursor:
            result.append(row)
        return result
    def searchsupplierbyId(self,supplier):
        cursor = self.conn.cursor()
        query = "select firstname,lastname,address from supplier where sid= %s "
        cursor.execute(query,(supplier,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getConsumers(self):
        cursor = self.conn.cursor()
        query = "select firstname,lastname,caddress from consumer"
        cursor.execute(query)
        result=[]
        for row in cursor:
            result.append(row)
        return result
    def searchConsumersbyId(self,id):
        cursor = self.conn.cursor()
        query = "select firstname,lastname,caddress from consumer where coid= %s "
        cursor.execute(query,(id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insertAdmin(self, uname,passwrd,email,firstname,lastname):
        cursor = self.conn.cursor()
        query = "insert into admins(uname,passwrd,email,firstname,lastname) values (%s, %s, %s , %s, %s) returning adminid;"
        cursor.execute(query, (uname,passwrd,email,firstname,lastname,))
        pid = cursor.fetchone()[0]
        self.conn.commit()
        return pid

    def insertConsumer(self, uname, passwrd, email, firstname, lastname,caddress):
        cursor = self.conn.cursor()
        query = "insert into consumer(uname,passwrd,email,firstname,lastname,caddress) values (%s, %s, %s , %s, %s, %s) returning coid;"
        cursor.execute(query, (uname, passwrd, email, firstname, lastname,caddress))
        pid = cursor.fetchone()[0]
        self.conn.commit()
        return pid
    def insertPhone(self, coid, phone):
        cursor = self.conn.cursor()
        query = "insert into phone(coid, phone_1) values (%s, %s) returning phid;"
        cursor.execute(query, (coid, phone))
        pid = cursor.fetchone()[0]
        self.conn.commit()
        return pid
    def insertSupplier(self, uname, passwrd, email, firstname, lastname,address):
        cursor = self.conn.cursor()
        query = "insert into supplier(uname,passwrd,email,firstname,lastname,address) values (%s, %s, %s , %s, %s, %s) returning sid;"
        cursor.execute(query, (uname, passwrd, email, firstname, lastname,address))
        pid = cursor.fetchone()[0]
        self.conn.commit()
        return pid