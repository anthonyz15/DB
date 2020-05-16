from config.dbconfig import pg_config
import psycopg2
class ResourcesDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getreAvailability(self):
        cursor = self.conn.cursor()
        query = "SELECT  rname,rquantity,rprice,rlocation FROM resources WHERE rid NOT IN (SELECT rid FROM contains)"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return  result

    def getreAnnounceAvailability(self):
        cursor = self.conn.cursor()
        query = "SELECT distinct rname FROM resources WHERE rid NOT IN (SELECT rid FROM contains)"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return  result

    def getresourcesRequested(self):
        cursor = self.conn.cursor()
        query = "select * from resources where rquantity>0"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getresourcesInRequest(self,id):
        cursor = self.conn.cursor()
        query = "SELECT  rname,rtype FROM resources as r inner join requested as rq on r.rid=rq.rid where rqid=%s order by rname"
        cursor.execute(query,(id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getresourcesAvailable(self):
        cursor = self.conn.cursor()
        query = "select rname,rprice,rquantity,rlocation from resources"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchresourcesAvailable(self,name):
        cursor = self.conn.cursor()
        query = "SELECT  rname,rtype,rquantity,rprice,rlocation FROM resources WHERE rid NOT IN (SELECT rid FROM requested) and rname like %s order by rtype"
        cursor.execute(query, (name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getresourcesDetails(self):
        cursor = self.conn.cursor()
        query = "select rname, rquantity,rprice, rlocation from resources"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchResourcesbyId(self,id):
        cursor = self.conn.cursor()
        query = "select rname, rquantity,rprice, rlocation from resources where rid=%s"
        cursor.execute(query,(id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insertresources(self, rname, rquantity, rprice, type, rlocation):
        cursor = self.conn.cursor()
        query = "insert into resources(rname,rquantity,rprice,rtype,rlocation) values (%s, %s, %s, %s, %s) returning rid;"
        cursor.execute(query, (rname, rquantity, rprice, type, rlocation))
        pid = cursor.fetchone()[0]
        self.conn.commit()
        return pid

    def dailyResourcesAvailable(self):
        cursor = self.conn.cursor()
        query = "SELECT resources.rname, resources.rlocation, sum(resources.rquantity) as Available FROM resources WHERE resources.rid NOT IN ( Select rid from contains) Group by resources.rname, resources.rlocation;"
        cursor.execute(query,)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def locationMatching(self):
        cursor = self.conn.cursor()
        query = "SELECT resources.rname,  sum(resources.rquantity) as Available,   sum(request.quantity) as Needed,  request.rqaddress FROM public.resources, public.request,   public.requested WHERE   request.rqid = requested.rqid AND  request.rqaddress = resources.rlocation AND  requested.rid = resources.rid and resources.rid NOT IN (Select rid from contains) Group by resources.rname, request.rqaddress;"
        cursor.execute(query, )
        result = []
        for row in cursor:
            result.append(row)
        return result

    def locationAvailable(self):
        cursor = self.conn.cursor()
        query = " SELECT resources.rname, resources.rlocation, sum(resources.rquantity) as Available FROM public.resources WHERE resources.rid NOT IN (Select rid from contains)  Group by resources.rname,  resources.rlocation order by rlocation;"
        cursor.execute(query, )
        result = []
        for row in cursor:
            result.append(row)
        return result

    def locationNeeded(self):
        cursor = self.conn.cursor()
        query = "SELECT resources.rname, sum(request.quantity) as Needed, request.rqaddress FROM public.request, public.requested, public.resources WHERE requested.rqid = request.rqid AND resources.rid = requested.rid Group By resources.rname, request.rqaddress order by rqaddress;"
        cursor.execute(query, )
        result = []
        for row in cursor:
            result.append(row)
        return result