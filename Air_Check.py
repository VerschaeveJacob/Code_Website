from flask import Flask, render_template, url_for
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registreer')
def registreer():
    return render_template('registreren.html')

@app.route('/nieuw_wachtwoord')
def nieuw_wachtwoord():
    return render_template('nieuwwachtwoord.html')

@app.route('/informatieC02')
def informatie_CO2():
    return render_template('informatie_C02.html')

@app.route('/informatie_Comfortniveau')
def informatie_comfortniveau():
    return render_template('informatie_comfortniveau.html')

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
    app.run()