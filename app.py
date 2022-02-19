# Import Dependencies
import datetime as dt
import numpy as np
import pandas as pd


# IMPORT SQLite Database-Necessary Dependencies
import sqlalchemy 
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


# IMPORT Flask - import these right after SQLAlchemy dependencies
from flask import Flask, jsonify


# CREATE THE ENGINE
engine = create_engine("sqlite:///hawaii.sqlite")


# REFLECT THE DATABASE & CREATING CLASSES/COLUMNS
    # 1.) DEVELOP THE BASE
Base = automap_base()
    # 2.) REFLECT THE DATABASE ONTO THE BASE USING Base.prepare()
Base.prepare(engine, reflect=True)
    # 3.) DEVELOP YOUR COLUMN/CLASS VARIABLES FOR REFERRAL
Measurement = Base.classes.measurement
Station = Base.classes.station
    # 4.) QUEUE UP A DATABASE SESSION LINK
session = Session(engine)


# SET UP Flask
app = Flask(__name__)


# ESTABLISH Flask ROUTES AFTER APP SET UP
# ESTABLISH A HOME PAGE WHICH WILL FUNCTION AS 
# THE CENTRAL TERMINAL FOR OUR DATA ANALYSIS RESULTS
@app.route('/')
def welcome():
    return(
        '''
        Welcome to the Climate ANalysis API!
        Available Routes:
        /api/v1.0/precipitation
        /api/v1.0/stations
        /api/v1.0/tobs
        /api/v1.0/temp/start/end       
        ''')