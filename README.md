# Azan-Prayer-Docker

# Azan Prayer Time Announcer

This project sets up a Docker container to fetch daily prayer times, configure cron jobs for automatic announcements, and play Azan audio files at the appropriate times.

## Overview

The container does the following:
1. **Fetches Prayer Times**: Uses `fetch_prayer.py` to fetch prayer times from a public API and writes them to a file.
2. **Sets Up Cron Jobs**: Uses `read_prayer.py` to read the fetched prayer times and set up cron jobs to play Azan audio files at the right times.
3. **Timezone**: The container is configured to use the host's timezone (`Asia/Kuala_Lumpur`).

## Setup

### Prerequisites

- Docker and Docker Compose installed on your machine.

### Directory Structure

Make sure your project directory structure looks like this:

```
azan/
│
├── Dockerfile
├── docker-compose.yml
├── entrypoint.sh
├── fetch_prayer.py
├── read_prayer.py
├── crontab
├── prayer_data/
│   └── prayer.txt
└── mp3/
    ├── azan.mp3
    └── azan2.mp3
```

### Dockerfile

Builds the Docker image with Python, necessary packages, and cron configuration. Includes a virtual environment for Python dependencies.

### docker-compose.yml

Defines the Docker service, specifying build context, volumes, and environment settings.

### entrypoint.sh

The entrypoint script sets up the timezone, adds the cron job for fetching prayer times if it doesn’t already exist, runs the necessary Python scripts, and starts the cron daemon.

## Usage

1. **Build and Start the Container**

   Run the following command to build the Docker image and start the container:

   ```sh
   docker-compose up -d --build
   ```

2. **Fetch Prayer Times**

   The `fetch_prayer.py` script will run every day at 4 AM, fetching new prayer times.

3. **Set Up Cron Jobs**

   The `read_prayer.py` script will set up or update cron jobs to play Azan audio files according to the fetched prayer times.

4. **Check Logs**

   To view logs for debugging or verification, use:

   ```sh
   docker logs audio_player
   ```

## Notes

- Ensure that the `mp3/` directory contains the Azan audio files.
- Adjust the `crontab` file if additional cron jobs are needed.

## Troubleshooting

- **Container Exits Unexpectedly**: Check the logs for errors using `docker logs audio_player` and ensure that all paths and file permissions are correct.
- **Timezone Issues**: Confirm that the `TZ` environment variable is correctly set in both `Dockerfile` and `entrypoint.sh`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize or add more details specific to your setup or requirements.
