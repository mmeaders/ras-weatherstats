<API import urllib2
import json
import datetime
import sqlite3
f = urllib2.urlopen('http://api.wunderground.com/api/<WU API Key Here>/geolookup/conditions/q/GA/Kennesaw.json')
json_string = f.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']
conditions = parsed_json['current_observation']['weather']
humidity = parsed_json['current_observation']['relative_humidity']
precipitation = parsed_json['current_observation']['precip_1hr_in']
pressure = parsed_json['current_observation']['pressure_in']
dewpoint = parsed_json['current_observation']['dewpoint_f']
windspeed = parsed_json['current_observation']['wind_mph']
winddir = parsed_json['current_observation']['wind_dir']
visibility = parsed_json['current_observation']['visibility_mi']
stationid = parsed_json['current_observation']['station_id']
latitude = parsed_json['current_observation']['observation_location']['latitude']
longitude = parsed_json['current_observation']['observation_location']['longitude']
timeobserved = parsed_json['current_observation']['observation_time_rfc822']
mytime = datetime.datetime.now()
#mytime = datetime.utcfromtimestamp(datetime.now()) 
#print mytime
#print "Current temperature in %s is: %s" % (location, temp_f)
#print "Location: %s" % (location)
#print "Temperature(F): %s" % (temp_f)
#print "Conditions: %s" % (conditions)
#print "Humidity: %s" % (humidity)
#print "Precipitation: %s" % (precipitation)
#print "Pressure: %s" % (pressure)
#print "Dewpoint: %s" % (dewpoint)
#print "Windspeed: %s" % (windspeed)
#print "Wind Direction: %s" % (winddir)
#print "Station ID: %s" % (stationid)
#print "Latitude: %s" % (latitude)
#print "Longitude: %s" % (longitude)
#print "TimeObserved: %s" % (timeobserved)
f.close()

db=sqlite3.connect('/weather/weather.db')
cursor=db.cursor()

with db:
	cursor.execute("insert into mytable VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(None,location, temp_f, conditions, humidity, precipitation, pressure, dewpoint, windspeed, winddir, stationid, latitude, longitude, timeobserved,mytime))

db.close
