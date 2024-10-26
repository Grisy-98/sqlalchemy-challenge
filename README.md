# sqlalchemy-challenge

## Instructions

Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.

### Part 1: Analyze and Explore the Climate Data

In this section, you’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically, you’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib. To do so, complete the following steps:
  1. Note that you’ll use the provided files (climate_starter.ipynb and hawaii.sqlite) to complete your climate analysis and data exploration.
  2. Use the SQLAlchemy create_engine() function to connect to your SQLite database.
  3. Use the SQLAlchemy automap_base() function to reflect your tables into classes, and then save references to the classes named station and measurement.
  4. Link Python to the database by creating a SQLAlchemy session.
  5. Perform a precipitation analysis and then a station analysis by completing the steps in the following two subsections.

##### Precipitation Analysis

The days with the highest precipitation happened in the months of September, April, and February.
Towards the end of the December, that was when there mas the minimum amount of precipitation that occured that year. 
![image](https://github.com/user-attachments/assets/27c2d803-2f17-4ed2-85c9-d928ca6bd5ba)


##### Stations Analysis

There are a total of 9 stations and the most active station is station USC00519281. 
The lowest temperature that was recorded by that station was 54 degrees. 
The highest temperature that was recorded by that station was 85 degrees.
The average temperature that was recorded by that station was about 71.66 degrees.

Based on the created histogram, the majority of the temperatures recorded was around 75 degrees.
![image](https://github.com/user-attachments/assets/63ef160c-9788-4ba6-b5d7-bfab69a870c3)

### Part 2: 

Now that you’ve completed your initial analysis, you’ll design a Flask API based on the queries that you just developed. To do so, use Flask to create your routes as follows:
1. /
   - Start at the homepage
   - List all the available routes
  
2. /api/v1.0/precipitation
   - Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
   - Return the JSON representation of your dictionary.

3. /api/v1.0/stations
   - Return a JSON list of stations from the dataset.

4. /api/v1.0/tobs
   - Query the dates and temperature observations of the most-active station for the previous year of data.
   - Return a JSON list of temperature observations for the previous year.
  
5. /api/v1.0/<start> and /api/v1.0/<start>/<end>
   - Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
   - For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
   - For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
