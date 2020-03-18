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

