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

    def insertmakes(self, pid,coid):
        cursor = self.conn.cursor()
        query = "insert into makes(rqid,coid) values (%s, %s) returning mkid;"
        cursor.execute(query, (pid,coid))
        pid = cursor.fetchone()[0]
        self.conn.commit()
        return pid


    def insertrequested(self, pid,rid,quantity):
        cursor = self.conn.cursor()
        query = "insert into requested(rid,rqid,quantity) values (%s, %s,%s) returning rqdid;"
        cursor.execute(query, (rid,pid,quantity))
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
        date1 = date.split("-")
        year = int(date1[0])
        month = int(date1[1])
        day = int(date1[2])
        print(year + month + day)
        if month == 1 or month == 3  or month == 5  or month == 7 or month == 8  or month == 10  or month == 12:
            if day+7 > 31:
                if month+1 >12:
                    year = year+1
                    month = "01"
                else:
                    month = month+1
            else:
                day = int(date1[2]) + 7
        else:
            if month == 4 or month == 6 or month == 9 or month == 11:
                if day + 7 > 30:
                    if month + 1 > 12:
                        year = year + 1
                        month = "01"
                    else:
                        month = month + 1
                else:
                    day = int(date1[2]) + 7
            else:
                if month == 2:
                    if day + 7 > 28:
                        if month + 1 > 12:
                            year = year + 1
                            month = "01"
                        else:
                            month = month + 1
                    else:
                        day = int(date1[2]) + 7

            year = str(year)
            if month < 10:
                month = "0" + str(month)
            else:
                month = str(month)

            if day < 10:
                day = "0" + str(day)
            else:
                day = str(day)

        date2 = year + "-" + month + "-" + day
        print(year +"-" +month+"-" + day)

        query = "SELECT rqdate as Week1stDate, resources.rname, sum(request.quantity) FROM public.request, public.requested,public.resources WHERE request.rqid = requested.rqid AND requested.rid = resources.rid and request.rqdate between %s and %s group by  request.rqdate, resources.rname;"
        cursor.execute(query, (date,date2,))
        result = []
        for row in cursor:
            result.append(row)
        return result