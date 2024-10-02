# Azan-Prayer-Docker

This Docker project sets up a containerized environment to fetch prayer times and play audio notifications using `mpg123` with `alsa` for sound output. The container is based on Alpine Linux and uses `cron` for scheduling tasks.

## Overview

- **Fetches prayer times** from a specified API daily.
- **Updates cron jobs** to play Azan audio at the specified prayer times.
- **Uses ALSA** for audio playback in the container.

## Requirements

- **Docker**: Ensure Docker is installed on your system.
- **ALSA**: Audio support using ALSA.

## Installation

### Dockerfile

The Dockerfile sets up the container environment with Python, necessary packages, and cron jobs. It also handles the virtual environment setup and installs required Python libraries.

### docker-compose.yml

The Docker Compose configuration sets up the container, ensuring that the timezone is synchronized with the host and mounts the necessary directories.

### entrypoint.sh

The entrypoint script activates the virtual environment, starts the cron daemon, runs the `fetch_prayer.py` script, and then updates the cron jobs using `read_prayer.py`.

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/9M2PJU/Azan-Prayer-Docker.git
   cd Azan-Prayer-Docker
   ```

2. **Build and run the Docker container:**

   ```bash
   docker compose up -d --build
   ```

3. **Container will:**
   - Fetch prayer times daily at 4 AM.
   - Update cron jobs based on fetched prayer times.
   - Play Azan audio at scheduled prayer times.

## Files

- `Dockerfile`: Defines the container image.
- `docker-compose.yml`: Configuration for Docker Compose.
- `entrypoint.sh`: Script that runs when the container starts.
- `fetch_prayer.py`: Python script to fetch prayer times.
- `read_prayer.py`: Python script to update cron jobs based on fetched times.
- `mp3/`: Directory containing the Azan audio files.
- `crontab`: File defining default cron jobs (if necessary).

## Notes

- **ALSA Audio**: Ensure your host system has the ALSA sound system installed and configured if you are using it for sound playback inside the container.
- **Timezone**: The container uses the host's timezone, which is set to `Asia/Kuala_Lumpur`.

## Troubleshooting

- **Audio Playback Issues**: Check if ALSA is properly configured on your host system.
- **Cron Logs**: If cron jobs are not executing, verify `/var/log/cron.log` inside the container for any errors.



