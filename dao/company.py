from config.dbconfig import pg_config
import psycopg2
class CompanyDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    def getCompany(self):
        cursor = self.conn.cursor()
        query = "select name,location from company"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchCompanybyId(self,id):
        cursor = self.conn.cursor()
        query = "select name, location from company where compid= %s "
        cursor.execute(query,(id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insertcompany(self, name, location):
        cursor = self.conn.cursor()
        query = "insert into company(name,location) values (%s, %s) returning compid;"
        cursor.execute(query, (name,location))
        pid = cursor.fetchone()[0]
        self.conn.commit()
        return pid