from config.dbconfig import pg_config
import psycopg2
class RequestDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def addrequest(self,date,quantity,adress):
        print(date,quantity,adress)
        print('added')

    def searchrequested(self, name):
        cursor = self.conn.cursor()
        query = "select rname, rtype, rquantity, rlocation from requested where rname = %s and rquantity > 0 order by rtype desc;"
        cursor.execute(query, (name,))
        result = []
        for row in cursor:
            result.append(row)
        return result