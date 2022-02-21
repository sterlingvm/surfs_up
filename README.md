# Surfs Up Challenge

## Purpose & Overview
Our client wants to run an surf shop in Oahu, Hawaii but isn't sure whether the business venture will work out. He is particular wary of whether weather conditions in the area will be favorable or lucrative for business before packing his bags and heading to Hawaii to follow this business passion. He has asked us to analyze weather data, run statistical analyses, and present the data to him in formats that he can use to show potential investors and his board of directors. He also particularly wants to see descriptive statistics on weather data for June and December, arguably the hottest and coldest months of the year.

This project's SQL database data is 2017 data

To do so, we utilized an SQLite database that houses Hawaii weather reports from 11 different weather stations using SQLAlchemy. We then extracted and reflected that data using an sqlalchemy engine, performed filtered queries on the data, converted the data into a dataframe, calculated the descriptive statistics for the Data for June, December, and other conditions, then loaded those data reports onto a Flask web app for easy access to the data using a web-developed, locally-hosted site page and interface.

## Results
The results of the June and December queries are as follows:

June 2017 Descriptive Statistics Results
![june_descriptives](Resources/June_Results.jpg?raw=true "Title")
Overall temperature recordings: 1700
Average temperature in June 2017: 74.94˚F
Minimum temperature recorded in June 2017: 64.00˚F
Maximum temperature recorded in June 2017: 85.00˚F


December 2017 Descriptive Statistics Results
![december_descriptives](Resources/Dec_Results.jpg?raw=true "Title")
Overall temperature recordings: 1517
Average temperature in December 2017: 71.04˚F
Minimum temperature recorded in December 2017: 56.00˚F
Maximum temperature recorded in December 2017: 83.00˚F

Flask URLs Per Report Page:
1) Go to/open app.py
2) in command line type "extract FLASK_APP=app.py"
3) in command line type "set FLASK_APP=app.py"
4) in command line type "flask run"
5) Enter any of these URLS to reach your desired analysis/report!:
    -Base: http://127.0.0.1:5000/
    -Precipitation Report: http://127.0.0.1:5000/api/v1.0/precipitation
    -Stations Information: http://127.0.0.1:5000/api/v1.0/stations
    -Temperature Observations: http://127.0.0.1:5000/api/v1.0/tobs
    -Temperature Queries By Date: http://127.0.0.1:5000/api/v1.0/temp/2017-06-01/2017-06-30
    ^ For Temperature Queries By Date, you can change the date filter by changing the start date (first date) and end date (second date) in the URL.


## Summary
In summary, our data tells us that temperatures stay consistantly in the 70s year round, with lows dropping in the winter/colder months. Coupled with precipitation data (not pictured here - go to climate_analysis.ipynb), we can see that precipitation frequency and temperature line up well for a surf shop in Oahu Hawaii! With more information such as precipitation reports based on time of day or surfing frequency/beach occupancy based on date/time we can gather even more pertinent insights that we can deliver to our client to grant assurance for his business venture!





