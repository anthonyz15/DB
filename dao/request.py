from config.dbconfig import pg_config
import psycopg2
class RequestDAO:
    global list
    list = set()
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def addrequest(self,date,quantity,adress):
        print(date,quantity,adress)
        list.add((date,quantity,adress))
        return list

    def searchrequested(self, name):
        cursor = self.conn.cursor()
        query = "SELECT  rname,rtype,quantity,rqaddress,rqdate FROM resources as r inner join requested as rq on r.rid=rq.rid inner join request as req on req.rqid=rq.rqid where rname like %s order by rname"
        cursor.execute(query, (name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getrequest(self):
        cursor = self.conn.cursor()
        query = "select rqaddress,quantity,rqdate from request"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchrequest(self, request):
        cursor = self.conn.cursor()
        query = "select rqaddress,quantity,rqdate from request where rqid= %s "
        cursor.execute(query, (request,))
        result = []
        for row in cursor:
            result.append(row)
        return result