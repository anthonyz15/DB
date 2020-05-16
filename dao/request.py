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

    def getRequestbyCoid(self, request):
        cursor = self.conn.cursor()
        query = "SELECT  firstname,lastname,quantity,rqaddress,rqdate FROM consumer as c inner join makes as mk on c.coid=mk.coid inner join request as req on req.rqid=mk.rqid where c.coid=%s"
        cursor.execute(query, (request,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insertrequest(self, rqaddress,quantity,rqdate):
        cursor = self.conn.cursor()
        query = "insert into request(rqaddress,quantity,rqdate) values (%s, %s, %s) returning rqid;"
        cursor.execute(query, (rqaddress,quantity,rqdate,))
        pid = cursor.fetchone()[0]
        self.conn.commit()
        return pid







    def dailyResourcesinNeed(self,date):
        cursor = self.conn.cursor()
        query = "SELECT resources.rname, sum(request.quantity), request.rqdate FROM public.request, public.requested,public.resources WHERE request.rqid = requested.rqid AND requested.rid = resources.rid and request.rqdate = %s group by resources.rname, request.rqdate;"
        cursor.execute(query, (date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def weeklyResourcesinNeed(self, date):
        cursor = self.conn.cursor()
        query = "SELECT to_char(rqdate, 'IYYY-IW') as 'Year-Week', resources.rname, sum(request.quantity), request.rqdate FROM public.request, public.requested,public.resources WHERE request.rqid = requested.rqid AND requested.rid = resources.rid and request.rqdate = %s group by to_char(rqdate, 'IYYY-IW'), request.rqdate;"
        cursor.execute(query, (date,))
        result = []
        for row in cursor:
            result.append(row)
        return result