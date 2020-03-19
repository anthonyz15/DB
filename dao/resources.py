from config.dbconfig import pg_config
import psycopg2
class ResourcesDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getreQuantity(self):
        """cursor = self.conn.cursor()
        query = "select * from resources where rquantity>0"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        print(result)"""

        list={(1,'lol',10,4,'mayaguez') , (2,'medic',5,20,'ponce'), (4,'planta',1,200,'San juan')}
        return list

    def getresourcesRequested(self):
        """cursor = self.conn.cursor()
        query = "select * from resources where rquantity>0"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        print(result)"""

        list = {('water', 5, 4, '3/17/20'), ('panadol', 1, 10, '3/12/20')}
        return list

    def getresourcesAvailable(self):
        """cursor = self.conn.cursor()
        query = "select * from resources where rquantity>0"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        print(result)"""

        list = {('water', 'nikini', 80, 'Mayaguez'), \
                ('batteries', 'AA', 89, 'San Juan'), \
                ('medicine', 'acetaminophen', 45, 'Ponce'), \
                ('water', 'dasani', 100, 'Caguas'), \
                ('batteries', 'AAA', 89, 'San Juan'), \
                ('medicine', 'tylenol', 45, 'Carolina')}
        return list

    def searchresourcesAvailable(self,name):
        cursor = self.conn.cursor()
        query = "select rname, rtype, rquantity, rlocation from resources where rname = %s and rquantity > 0 order by rtype desc;"
        cursor.execute(query, (name,))
        result = []
        for row in cursor:
            result.append(row)
        return result
