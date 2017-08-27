FROM mmeaders/mm-pibase

 
# Add crontab file in the cron directory
ADD crontab /etc/cron.d/weather-cron
ADD code /home/pi/
 
# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/weather-cron
#RUN chmod 0644 /home/pi/showweather.sh 

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Set the timezone.
RUN echo "America/New_York" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

# Run the command on container startup
CMD /etc/init.d/cron -f


