# Final Project - cours CS50

import os

from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import func
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from helper import login_required
import requests

app = Flask(__name__)


# Check for environment variable
#if not os.getenv("DATABASE_URL"):
#    raise RuntimeError("DATABASE_URL is not set")

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

    return render_template("index.html")

@app.route("/login")
def login():

    return render_template("index.html")

@app.route("/logout")
@login_required
def logout():

    return render_template("index.html")



@app.route("/aboutus")
def AboutUs():

    return render_template("index.html")
#Login

#Register

#logout

#pagina para agregar fallas como operador

#pagina para aceptar fallas como supervisor

#pagina para visualizar reportes
