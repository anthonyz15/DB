from config.dbconfig import pg_config
import psycopg2
class PurchaseDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def purchase(self,Date,Address,Quantity,Cost):
        print(Date,Address,Quantity,Cost)
        print('Purchase Completed')

    def reserve(self,Date, Address, Quantity, Cost):
        print(Date, Address, Quantity, Cost)
        print('Reserve Completed')