# Import the dependencies.
import numpy as np
import pandas as pd
import datetime as dt
import re

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################

# Create engine using the `hawaii.sqlite` database file
engine = create_engine("Starter_Code/Resources/hawaii.sqlite")
# Declare a Base using `automap_base()`
Base = automap_base()
# Use the Base class to reflect the database tables
Base.prepare(autoload_with=engine)

# Assign the measurement class to a variable called `Measurement` and
# the station class to a variable called `Station`
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create a session
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Flask Routes
#################################################

# 1 /
# Start at the homepage 
# List all the available routes

@app.route("/")
def home():
    return(
        f"Welcome to the Hawaii Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start (enter as YYYY-MM-DD)<br/>"
        f"/api/v1.0/start/end (enter as YYYY-MM-DD)<br/>"


    )

# 2. /api/v1.0/precipitation
# Convert the query results from your precipitation analysis (i.e. retrieve only
# the last 12 montths of data) to a dictionary using date as the key and prcp as the value.
# Return the JSON representation of your dictionary

@app.route("/api/v1.0/presicpitation")
def precipitaion():
    session = Session(engine)

    one_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    prev_last_date = dt.date(one_year.year, one_year.month, one_year.day)
    
    query_results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_last_date).order_by(Measurement.date).all()
    
    precipitaion_dict = dict(query_results)

    print(f"Results for Precipitaion - {precipitaion_dict}")
    print("Out of Precipitation Section.")
    return jsonify(precipitaion_dict)

# 3. /api/v1.0/stations
# Return a JSON list of stations from the dataset.

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    st = [Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation]
    query_result = session.query(*st).all()
    session.close()

    stations = []
    for station, name, lat, lon, el in query_result:
        station_dict = {}
        station_dict["Station"] = station
        station_dict["Name"] = name
        station_dict["Latitude"] = lat
        station_dict["Longitude"] = lon
        station_dict["Elevation"] = el
        stations.append(station_dict)

    return jsonify(stations)

# 4. /api/v1.0/tobs
# Query the dates and temperature observations of the most active station
# for the previous year data
# Return a JSON list of teemperature observations for the previous year

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    query_results = session.query(Measurement.tobs).filter(Measurement.station=="USC00519281").filter(Measurement.date>='2016-08-23').all()

    temp_obs = []
    for date, tobs in query_results:
        tobs_dict = {}
        tobs_dict["Date"] = date
        tobs_dict["Tobs"] = tobs
        temp_obs.append(tobs_dict)

    return jsonify(temp_obs)

# 5. api/v1.0/<start> and /api.v1.0/<end>
# Return a JSON list of the minimum temperature, the average temperature, and the 
# maximum temperature for a specified strat or start-end range
# For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater
# than or equal to the start dates.
# For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates
# from the start date to end date, inclusive.

@app.route("/api/v1.0/<start>")
def start(start):
    session = Session(engine)
    query_results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tons)).filter(Measurement.date >= start).all()
    session.close()

    temps = []
    for min_temp, avg_temp, max_temp in query_results:
        temps_dict = {}
        temps_dict["Minimum Temperature"] = min_temp
        temps_dict["Average Temperature"] = avg_temp
        temps_dict["Maximum Temperature"] = max_temp
        temps.append(temps_dict)

    return jsonify(temps)


@app.route("/api/v1.0/<start>/<end>")
def start_and_end(start, end):
    session = Session(engine)
    query_results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tons)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    session.close()

    temps = []
    for min_temp, avg_temp, max_temp in query_results:
        temps_dict = {}
        temps_dict["Minimum Temperature"] = min_temp
        temps_dict["Average Temperature"] = avg_temp
        temps_dict["Maximum Temperature"] = max_temp
        temps.append(temps_dict)

    return jsonify(temps)


if __name__ == '__main__':
    app.run(debug=True)
