class dbClass():
    def __init__(self):
        import mysql.connector as connector

        self.__dsn = {"host": "localhost", "user": "jacob", "passwd": "root", "db": "AIR_CHECK"}
        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()

    def insert_comment(self, name, email, comment):
        q = "INSERT INTO tblContact(Naam,Emailadres,Bericht, Tijdstip)" \
            "VALUES('" + name + "','" + email + "','" + comment + "', now())"
        print(q)
        self.__cursor.execute(q)
        self.__connection.commit()
        self.__connection.close()

    def registreren(self, email, passwoord, serienummer):
        q = "INSERT INTO tblGegevens(Emailadres,Wachtwoord,Ingelogd_Blijven, Serienummer)" \
            "VALUES('" + email + "','" + passwoord + "', 0 ,'" + serienummer + "')"
        self.__cursor.execute(q)
        self.__connection.commit()
        self.__connection.close()

    def inloggen_controleren(self, mail):
        q = "SELECT wachtwoord FROM tblGegevens WHERE Emailadres = '" + mail + "';"
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

    def Temperatuur_dashboard(self, serienummer):
        q = "SELECT M.Temperatuur FROM tblGegevens as G JOIN tblMetingLTC as M ON M.Serienummer = G.Serienummer " \
            "WHERE M.Serienummer LIKE '" + serienummer +  "' ORDER BY Tijdstip DESC LIMIT 1;"
        self.__cursor.execute(q)
        result = self.__cursor.fetchone()
        self.__connection.close()
        return result

    def Luchtvochtigheid_dashboard(self, serienummer):
        q = "SELECT M.Luchtvochtigheid FROM tblGegevens as G JOIN tblMetingLTC as M ON M.Serienummer = G.Serienummer " \
            "WHERE M.Serienummer LIKE '" + serienummer +  "' ORDER BY Tijdstip DESC LIMIT 1;"
        self.__cursor.execute(q)
        result = self.__cursor.fetchone()
        self.__connection.close()
        return result

    def Comfortniveau_dashboard(self, serienummer):
        q = "SELECT M.Comfortniveau FROM tblGegevens as G JOIN tblMetingLTC as M ON M.Serienummer = G.Serienummer " \
            "WHERE M.Serienummer LIKE '" + serienummer +  "' ORDER BY Tijdstip DESC LIMIT 1;"
        self.__cursor.execute(q)
        result = self.__cursor.fetchone()
        self.__connection.close()
        return result

    def CO2_grafiek(self, serienummer):
        q = "SELECT CO2, Tijdstip FROM tblMetingCO2 WHERE Serienummer = '" + serienummer + "' ORDER BY Tijdstip DESC LIMIT 5;"
        self.__cursor.execute(q)
        result = self.__cursor.fetchall()
        self.__connection.close()
        return result


    def Temperatuur_grafiek(self, serienummer):
        q = "SELECT Temperatuur, Tijdstip FROM tblMetingLTC WHERE Serienummer = '" + serienummer + "' ORDER BY Tijdstip DESC LIMIT 5;"
        self.__cursor.execute(q)
        result = self.__cursor.fetchall()
        self.__connection.close()
        return result

    def Luchtvochtigheid_grafiek(self, serienummer):
        q = "SELECT Luchtvochtigheid, Tijdstip FROM tblMetingLTC WHERE Serienummer = '" + serienummer + "' ORDER BY Tijdstip DESC LIMIT 5;"
        self.__cursor.execute(q)
        result = self.__cursor.fetchall()
        self.__connection.close()
        return result

    def Comfortniveau_grafiek(self, serienummer):
        q = "SELECT Comfortniveau, Tijdstip FROM tblMetingLTC WHERE Serienummer = '" + serienummer + "' ORDER BY Tijdstip DESC LIMIT 5;"
        self.__cursor.execute(q)
        result = self.__cursor.fetchall()
        self.__connection.close()
        return result

    def metingsinterval_CO2(self, serienummer):
        q = "SELECT Metingsinterval FROM tblMetingsintervalCO2 WHERE Serienummer = '" + serienummer + "';"
        self.__cursor.execute(q)
        result = self.__cursor.fetchone()
        self.__connection.close()
        return result

    def metingsinterval_LTC(self, serienummer):
        q = "SELECT Metingsinterval FROM tblMetingsintervalLTC WHERE Serienummer = '" + serienummer + "';"
        self.__cursor.execute(q)
        result = self.__cursor.fetchone()
        self.__connection.close()
        return result

    def update_metingsinterval_CO2(self, serienummer, waarde):
        q = "UPDATE tblMetingsintervalCO2 SET Metingsinterval = " + waarde + " WHERE Serienummer = '" + serienummer + "'"
        self.__cursor.execute(q)
        self.__connection.commit()
        self.__connection.close()

    def update_metingsinterval_LTC(self, serienummer, waarde):
        q = "UPDATE tblMetingsintervalLTC SET Metingsinterval = " + waarde + " WHERE Serienummer = '" + serienummer + "'"
        self.__cursor.execute(q)
        self.__connection.commit()
        self.__connection.close()