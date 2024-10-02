FROM python:3.12-alpine

# Install additional system packages
RUN apk add --no-cache mpg123 alsa-lib alsa-utils curl openrc tzdata

# Set the timezone
ENV TZ=Asia/Kuala_Lumpur

# Create necessary directories
WORKDIR /app
RUN mkdir -p /app/prayer_data /app/mp3 /var/log

# Copy the scripts and other necessary files
COPY fetch_prayer.py /app/
COPY read_prayer.py /app/
COPY mp3/* /app/mp3/
COPY entrypoint.sh /entrypoint.sh

# Install Python dependencies
RUN pip install --no-cache-dir requests pydub

# Ensure the scripts are executable
RUN chmod a+x /app/*.py /entrypoint.sh

# Pre-run Python scripts
RUN python /app/fetch_prayer.py && python /app/read_prayer.py

# Set entrypoint
ENTRYPOINT ["/entrypoint.sh"]
