from flask import Flask, render_template, url_for, request, redirect
import os
from dbClass import dbClass
import uuid
import hashlib

app = Flask(__name__)

#GLOBALE VARIABELE SERIENUMMER
serienummer = ""


#INLOGGEN, REGISTREREN, NIEUW WACHTWOORD
@app.route('/', methods=["GET","POST"])
def index():
    return render_template('index.html')

@app.route('/registreer')
def registreer():
    return render_template('registreren.html')

@app.route('/nieuw_wachtwoord')
def nieuw_wachtwoord():
    return render_template('nieuwwachtwoord.html')




#DASHBOARD PAGINA'S
@app.route('/dashboard_CO2')
def dashboard_CO2():
    db = dbClass()
    global serienummer
    print("serienummer dashboard %s" % serienummer)
    CO2_waarde = db.CO2_dashboard(str(serienummer[0]))
    print(CO2_waarde)
    return render_template('dashboard_CO2.html', waarde = round(int(CO2_waarde[0]),0))

@app.route('/dashboard_temperatuur')
def dashboard_temperatuur():
    db = dbClass()
    global serienummer
    Temp_waarde = db.Temperatuur_dashboard(str(serienummer[0]))
    print(Temp_waarde)
    return render_template('dashboard_temperatuur.html', waarde = round(int(Temp_waarde[0]),0))

@app.route('/dashboard_luchtvochtigheid')
def dashboard_luchtvochtigheid():
    db = dbClass()
    global serienummer
    Luchtvochtigheids_waarde = db.Luchtvochtigheid_dashboard(str(serienummer[0]))
    print(Luchtvochtigheids_waarde)
    return render_template('dashboard_luchtvochtigheid.html', waarde = round(int(Luchtvochtigheids_waarde[0]),0))

@app.route('/dashboard_comfortniveau')
def dashboard_comfortniveau():
    db = dbClass()
    global serienummer
    Comfortniveau_waarde = db.Comfortniveau_dashboard(str(serienummer[0]))
    print(Comfortniveau_waarde)
    return render_template('dashboard_comfortniveau.html', waarde = round(int(Comfortniveau_waarde[0]),0))



#GRAFIEK PAGINA'S
@app.route('/grafiek_CO2')
def grafiek_CO2():
    return render_template('grafiek_CO2.html')




#INFORMATIE PAGINA'S
@app.route('/informatie_C02')
def informatie_CO2():
    return render_template('informatie_C02.html')

@app.route('/informatie_Comfortniveau')
def informatie_comfortniveau():
    return render_template('informatie_comfortniveau.html')




#FORMULIEREN
@app.route('/sentContact', methods=["POST"])
def sentContact():
    db = dbClass()
    naam = request.form['naam']
    print(naam)
    email = request.form['email']
    print(email)
    comment = request.form['commentaar']
    print(comment)
    db.insert_comment(naam,email,comment)

    return render_template('contact_verzenden.html')

@app.route('/sentRegistreer', methods=["POST"])
def sentRegistreer():
    db = dbClass()
    email = request.form['email']
    password = request.form['password']
    hashed_password = hash_password(password)
    password_bevestigen = request.form['password_bevestigen']
    serienummer = request.form['serienummer']

    #controleren of de 2 paswoorden gelijk zijn, zoja, dan mag je registreren, zo nee, mag je opnieuw proberen
    if check_password(hashed_password, password_bevestigen):
        db.registreren(email, hashed_password, serienummer)
        return render_template("index.html")
    else:
        return render_template("registreren.html")
    #if result_email[0] != 0 or password != password_bevestigen:
    #return render_template("index.html")
    # else:
    #     db.registreren(email,hashed_password,serienummer)
    #     print("Gelukt")
    #     return render_template('index.html')

@app.route('/contactverzenden')
def contactverzenden():
    return render_template("contact_verzenden.html")

@app.route('/inloggen_controleren' , methods=["POST"])
def inloggen_controleren():
    dbemail = dbClass()
    dbserienummer = dbClass()
    email = request.form['email']
    wachtwoord = request.form['password']

    hashed_password = dbemail.inloggen_controleren(email)
    print(hashed_password)
    print("DB_Controleren")
    if check_password(hashed_password[0], wachtwoord):
        global serienummer
        serienummer = dbserienummer.inloggen_serienummer(email)
        print("serienummer inloggen %s" % serienummer)
        return dashboard_CO2()
        #return dashboard_CO2(str(serienummer[0]))
    else:
        return render_template("inloggen_verkeerd.html")

    #
    #
    #     #CO2 = 355
    # serienummer = db.inloggen_serienummer(email)
    # #print(serienummer)
    # if aantal[0] == 1:
    #     print("JA")
    # else:
    #     print("Nee")



#PASSWORD HASHING AND DEHASHING
def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

if __name__ == '__main__':
    app.run(debug=True)
