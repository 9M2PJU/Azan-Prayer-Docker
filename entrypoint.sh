#!/bin/sh

# Activate the virtual environment
. /app/venv/bin/activate

# Add a cron job to fetch prayer times every day at 4 AM
echo "0 4 * * * /app/venv/bin/python /app/fetch_prayer.py >> /var/log/cron_fetch_prayer.log 2>&1" >> /etc/crontabs/root

# Run the fetch_prayer.py script to get initial prayer times
python /app/fetch_prayer.py

# Run the read_prayer.py script to set up prayer time cron jobs
python /app/read_prayer.py

# Start cron in the foreground with logging enabled
crond -f -l 8 -L /var/log/cron.log

