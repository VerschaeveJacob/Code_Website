from flask import Flask, render_template, url_for, request, redirect
import os
from dbClass import dbClass

app = Flask(__name__)

#serienummer = ""

@app.route('/', methods=["GET","POST"])
def index():
    return render_template('index.html')

@app.route('/registreer')
def registreer():
    return render_template('registreren.html')

@app.route('/nieuw_wachtwoord')
def nieuw_wachtwoord():
    return render_template('nieuwwachtwoord.html')

@app.route('/informatie_C02')
def informatie_CO2():
    return render_template('informatie_C02.html')

@app.route('/informatie_Comfortniveau')
def informatie_comfortniveau():
    return render_template('informatie_comfortniveau.html')

@app.route('/dashboard_CO2')
def dashboard_CO2(CO2):
    db = dbClass()
    #print(serienummer)
    #CO2_waarde = db.CO2_dashboard(serienummer)
    #print(CO2_waarde)
    #CO2 = 455
    #print(serienummer)
    return render_template('dashboard_CO2.html', waarde = CO2)

@app.route('/grafiek_CO2')
def grafiek_CO2():
    return render_template('grafiek_CO2.html')

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
    print(email)
    email = request.form['email']
    password = request.form['password']
    print(password)
    password_bevestigen = request.form['password_bevestigen']
    print(password_bevestigen)
    serienummer = request.form['serienummer']
    print(serienummer)
    result_email = db.registreren_emailadres_controleren(email)
    print(result_email[0])

    if result_email[0] != 0 or password != password_bevestigen:
        return render_template("registreren.html")
    else:
        db.registreren(email,password,serienummer)
        print("Gelukt")
        return render_template('index.html')

@app.route('/contactverzenden')
def contactverzenden():
    return render_template("contact_verzenden.html")

@app.route('/inloggen_controleren' , methods=["POST"])
def inloggen_controleren():
    db = dbClass()
    email = request.form['email']
    wachtwoord = request.form['password']

    aantal = db.inloggen_controleren(email, wachtwoord)
    print(aantal)
    #global serienummer
    print("DB_Controleren")
    CO2 = 355
    #serienummer = db.inloggen_serienummer(email)
    #print(serienummer)
    if aantal[0] == 1:
        print("JA")
        return dashboard_CO2(CO2)
    else:
        print("Nee")
        return render_template("inloggen_verkeerd.html")

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
