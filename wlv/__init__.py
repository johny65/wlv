import os
from flask import Flask, session, redirect, url_for, escape, request, render_template
from .logcollect import GlassfishFormatter

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        #hardcoded login for now:
        if username == "admin" and password == "wlv":
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        else:
            logout()
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

def check_logged():
    return "username" in session

@app.route("/")
@app.route("/log")
def index():
    if not check_logged():
        return redirect(url_for('login'))
        
    log_path = os.getenv("WLV_LOG_PATH")
    if not log_path:
        return "Ningún log configurado."
    
    parser = GlassfishFormatter()
    try:
        with open(log_path) as log_file:
            log_content = parser.parse(log_file)
        return render_template("log.html", log_content=log_content)
    except FileNotFoundError:
        return "No se encontró el archivo de log ({}).".format(log_path)
    except IOError:
        return "Ocurrió un error abriendo el archivo de log ({}).".format(log_path)
