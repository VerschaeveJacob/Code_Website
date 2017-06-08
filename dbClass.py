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

    def inloggen_serienummer(self,mail):
        q = "SELECT Serienummer FROM tblGegevens WHERE Emailadres LIKE '" + mail + "';"
        self.__cursor.execute(q)
        result = self.__cursor.fetchone()
        self.__connection.close()
        return result

    def registreren_emailadres_controleren(self, mail):
        q = "SELECT COUNT(*) FROM tblGegevens WHERE Emailadres = '" + mail + "';"
        self.__cursor.execute(q)
        result = self.__cursor.fetchone()
        self.__connection.close()
        return result

    def CO2_dashboard(self, serienummer):
        q = "SELECT M.CO2 FROM tblGegevens as G JOIN tblMetingCO2 as M ON M.Serienummer = G.Serienummer " \
            "WHERE M.Serienummer LIKE '" + serienummer +  "' ORDER BY Tijdstip DESC LIMIT 1;"
        self.__cursor.execute(q)
        result = self.__cursor.fetchone()
        self.__connection.close()
        return result