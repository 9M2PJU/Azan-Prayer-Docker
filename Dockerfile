FROM alpine:latest

# Install required packages
RUN apk update && \
    apk add --no-cache python3 py3-pip mpg123 alsa-lib alsa-utils curl openrc tzdata && \
    apk add --no-cache --virtual .build-deps gcc musl-dev

# Create a virtual environment
RUN python3 -m venv /app/venv

# Install Python packages inside the virtual environment
RUN /app/venv/bin/pip install --no-cache-dir requests pydub

# Remove build dependencies
RUN apk del .build-deps

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
RUN chmod +x /entrypoint.sh

# Copy the crontab file
COPY crontab /etc/crontabs/root

# Set entrypoint
ENTRYPOINT ["/entrypoint.sh"]

