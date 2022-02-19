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
        'Welcome to the Climate Analysis API! <br>'
        '<br>'
        'Available Routes:<br>'
        '/api/v1.0/precipitation <br>'
        '/api/v1.0/stations <br>'
        '/api/v1.0/tobs <br>'
        '/api/v1.0/temp/start/end <br>'
        )
# ^ ACCESS THIS ROUTE BY GOING TO http://127.0.0.1:5000/

@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)
# ^ ACCESS THIS ROUTE BY GOING TO http://127.0.0.1:5000/api/v1.0/precipitation

@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)
# ^ ACCESS THIS ROUTE BY GOING TO http://127.0.0.1:5000/api/v1.0/stations

@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
# ^ ACCESS THIS ROUTE BY GOING TO http://127.0.0.1:5000/api/v1.0/tobs

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)
# ^ TO ACCESS DATA IN THIS ROUTE YOU HAVE TO IUNPUT A START AND END DATE
# DO THIS BY INPUTTING YOUR DATES INTO THE LOCALHOST URL
# EXAMPLE: http://127.0.0.1:5000/api/v1.0/temp/2017-06-01/2017-06-30

