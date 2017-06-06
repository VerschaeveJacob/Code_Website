class dbClass():
    def __init__(self):
        import mysql.connector as connector

        self.__dsn = {"host": "localhost", "user": "jacob", "passwd": "root", "db": "db_products"}
        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()

