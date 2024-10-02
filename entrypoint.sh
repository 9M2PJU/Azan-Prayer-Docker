#!/bin/sh

# Run the fetch_prayer.py script to get initial prayer times
python3 /app/fetch_prayer.py

# Run the read_prayer.py script to set up prayer time cron jobs
python3 /app/read_prayer.py

# Start cron in the foreground with logging enabled
crond -f -l 8 -L /var/log/cron.log
