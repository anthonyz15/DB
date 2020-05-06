from config.dbconfig import pg_config
import psycopg2
class PurchaseDAO:
    global list,list1
    list=set()
    list1=set()
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    '''def purchase(self,Date,Address,Quantity,Cost):
        print(Date,Address,Quantity,Cost)
        print('Purchase Completed')
        list.add((Date,Address,Quantity,Cost))
        return list

    def reserve(self,Date, Address, Quantity, Cost):
        print(Date, Address, Quantity, Cost)
        print('Reserve Completed')
        list1.add((Date, Address, Quantity, Cost))
        return list1'''

    def getPurchase(self):
        cursor = self.conn.cursor()
        query = "select firstname,lastname,caddress from consumer"
        cursor.execute(query)
        result=[]
        for row in cursor:
            result.append(row)
        return result
    def searchPurchasebyId(self,id):
        cursor = self.conn.cursor()
        query = "select firstname,lastname,caddress from consumer where coid= %s "
        cursor.execute(query,(id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrderPurchase(self):
        cursor = self.conn.cursor()
        query = "select odate,olocation,totalprice from orders where totalprice>0"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchOrderPurchasebyId(self, id):
        cursor = self.conn.cursor()
        query = "select odate,olocation,totalprice from orders where totalprice>0 and oid=%s"
        cursor.execute(query, (id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrderReserve(self):
        cursor = self.conn.cursor()
        query = "select odate,olocation,totalprice from orders where totalprice=0"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchOrderReservebyId(self, id):
        cursor = self.conn.cursor()
        query = "select odate,olocation,totalprice from orders where totalprice=0 and oid=%s"
        cursor.execute(query, (id,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    def getPurchasebyCoid(self, id):
        cursor = self.conn.cursor()
        query = "SELECT  firstname,lastname,totalprice,olocation,odate FROM consumer as c inner join purchases as p on c.coid=p.coid inner join orders as o on o.oid=p.oid where c.coid=%s and totalprice>0"
        cursor.execute(query, (id,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    def getReservebyCoid(self, id):
        cursor = self.conn.cursor()
        query = "SELECT  firstname,lastname,totalprice,olocation,odate FROM consumer as c inner join reserves as rv on c.coid=rv.coid inner join orders as o on o.oid=rv.oid where c.coid=%s and totalprice=0"
        cursor.execute(query, (id,))
        result = []
        for row in cursor:
            result.append(row)
        return result