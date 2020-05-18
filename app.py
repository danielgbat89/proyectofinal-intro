# Final Project - cours CS50

# Antes de "flask run" activar modo virtual y setear variables de entorno
#1) solo si no aparece ya el (VENV) en la linea de comandos ->  & C:\Users\guillermo\Desktop\Repo\ProyectoFinal_Intro\venv\Scripts\Activate.ps1
#2) $env:FLASK_DEBUG="1"
#3) $env:FLASK_APP="application.py"
#4) $env:DATABASE_URL="postgres://nunuoqncaamyww:e218c3bed1bbb7805ee76d521156e6a01d2078f49edf9870e681356ee826d626@ec2-35-174-88-65.compute-1.amazonaws.com:5432/d8uj98kvm7rfrl"
#5) flask run



import os

#modules Flask
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
#modules for SQL
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import func
#Security
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from helper import login_required

import requests

#plot modules
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
import numpy as np
import base64
from io import BytesIO



app = Flask(__name__)

# Seteo la base de datos
engine = create_engine('postgres://nunuoqncaamyww:e218c3bed1bbb7805ee76d521156e6a01d2078f49edf9870e681356ee826d626@ec2-35-174-88-65.compute-1.amazonaws.com:5432/d8uj98kvm7rfrl')
db = scoped_session(sessionmaker(bind=engine))

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#index
@app.route("/")
def index():

    return render_template("index.html", logued = False)

#Login
@app.route("/login")
def login():

    """Log user in"""
    
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return render_template("login.html", invalidpassword=True)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return render_template("login.html", invalidpassword=True)

        # Query database for username
        username=request.form.get("username")
        rows = db.execute("SELECT * FROM staff WHERE username = :username", {"username": username}).fetchall()
        db.commit()

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return render_template("login.html", invalidpassword=True)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])

def register():
    """Register user"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return render_template("register.html", setname=True)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return render_template("register.html", invalidpassword=True)

        # Ensure password was submitted
        elif request.form.get("password2") != request.form.get("password"):
            return render_template("register.html", passwordnotmatch=True)

        # Ensure job was submitted
        elif not request.form.get("job"):
            return render_template("register.html", noJob=True)

        username = request.form.get("username")
        password = request.form.get("password")
        job = request.form.get("job")
        hashpass =  generate_password_hash(password)
        
        # Insert info in staff Table      
        db.execute("INSERT INTO staff (username , hash) VALUES (:username, :hash)", {"username": username, "hash": hashpass})
        db.commit()
        
        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username", {"username": username}).fetchall()
        db.commit()

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return render_template("register.html", invalidpassword=True)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

      # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


#Logout a
@app.route("/logout")
def logout():

    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")



@app.route("/aboutus")
def AboutUs():
    #TODO
    return render_template("index.html")

@app.route("/plot")
def plot():

    fig = plt.figure()
    
    #plot sth
    # Data for plotting
    t = np.arange(0.0, 2.0, 0.01)
    s = np.sin(2 * np.pi * t)

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
           title='About as simple as it gets, folks')
    
    ax.grid()
    tmpfile = BytesIO()
    fig.savefig(tmpfile, format='png')  #guarda la figura en un espacio temporal
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8') #l decodeutf-8 es para que funcione con jinja
   
    #otro dibujo tipo histograma
    histogram = plt.figure()
    canvas = FigureCanvasAgg(histogram)
    x = np.random.rand(10000)
    ax = histogram.add_subplot(111)
    ax.hist(x, 100)
    ax.set_title("Histograma")
    ax.grid()
    temp2 = BytesIO()
    histogram.savefig(temp2, format='png')
    encoded2 = base64.b64encode(temp2.getvalue()).decode('utf-8')
    
    return render_template("plot.html", data = encoded, data2 = encoded2)
    

@app.route("/wind")
def wind():

    return render_template("wind.html")
#pagina para agregar fallas como operador

#pagina para aceptar fallas como supervisor

#pagina para visualizar reportes
