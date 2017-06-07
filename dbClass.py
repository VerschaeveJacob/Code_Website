class dbClass():
    def __init__(self):
        import mysql.connector as connector

        self.__dsn = {"host": "localhost", "user": "jacob", "passwd": "root", "db": "Air_Check"}
        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()

    def insert_comment(self, name, email, comment):
        q = "INSERT INTO tblContact(Naam,Emailadres,Bericht, Tijdstip)" \
            "VALUES('" + name + "','" + email + "','" + comment + "', now())"
        self.__cursor.execute(q)
        self.__connection.commit()
        self.__connection.close()

    def registreren(self, email, passwoord, serienummer):
        q = "INSERT INTO tblGegevens(Emailadres,Wachtwoord,Ingelogd_Blijven, Serienummer)" \
            "VALUES('" + email + "','" + passwoord + "', 0 ,'" + serienummer + "')"
        self.__cursor.execute(q)
        self.__connection.commit()
        self.__connection.close()

    def inloggen_controleren(self, mail, passwoord):
        q = "SELECT COUNT(*) FROM tblGegevens WHERE Emailadres = '" + mail + "' AND Wachtwoord = '" + passwoord + "';"
        self.__cursor.execute(q)
        result = self.__cursor.fetchone()
        self.__connection.close()
        return result