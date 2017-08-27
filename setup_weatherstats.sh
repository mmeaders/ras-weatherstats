docker build --tag weatherstats .
docker run --name weatherstats -v /home/pi/weathermount:/weather -d --restart=always weatherstats cron -f
