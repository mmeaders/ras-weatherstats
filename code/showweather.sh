sqlite3 /home/pi/python/wu/weather.db "select * from (SELECT strftime('%Y-%m-%d %H:%M:%S',Timestamp)as timestamp,temp, conditions from mytable order by timestamp desc LIMIT 55)order by timestamp asc;
"
