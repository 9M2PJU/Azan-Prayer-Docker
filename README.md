
## 🌐 Socials:
[![Facebook](https://img.shields.io/badge/Facebook-%231877F2.svg?logo=Facebook&logoColor=white)](https://facebook.com/https://www.facebook.com/faizul.9m2pju) [![TikTok](https://img.shields.io/badge/TikTok-%23000000.svg?logo=TikTok&logoColor=white)](https://tiktok.com/@9m2pju) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?logo=YouTube&logoColor=white)](https://youtube.com/@http://www.youtube.com/@9m2pju) 

# 💻 Tech Stack:
![Raspberry Pi](https://img.shields.io/badge/-RaspberryPi-C51A4A?style=for-the-badge&logo=Raspberry-Pi) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white) ![Windows Terminal](https://img.shields.io/badge/Windows%20Terminal-%234D4D4D.svg?style=for-the-badge&logo=windows-terminal&logoColor=white) ![YAML](https://img.shields.io/badge/yaml-%23ffffff.svg?style=for-the-badge&logo=yaml&logoColor=151515) ![Cloudflare](https://img.shields.io/badge/Cloudflare-F38020?style=for-the-badge&logo=Cloudflare&logoColor=white) ![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)
# 📊 GitHub Stats:
![](https://github-readme-stats.vercel.app/api?username=9M2PJU&theme=dark&hide_border=false&include_all_commits=false&count_private=false)<br/>
![](https://github-readme-streak-stats.herokuapp.com/?user=9M2PJU&theme=dark&hide_border=false)<br/>
![](https://github-readme-stats.vercel.app/api/top-langs/?username=9M2PJU&theme=dark&hide_border=false&include_all_commits=false&count_private=false&layout=compact)

## 🏆 GitHub Trophies
![](https://github-profile-trophy.vercel.app/?username=9M2PJU&theme=radical&no-frame=false&no-bg=true&margin-w=4)

---
[![](https://visitcount.itsvg.in/api?id=9M2PJU&icon=0&color=0)](https://visitcount.itsvg.in)

  ## 💰 You can help me by Donating
  [![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/9m2pju) 

  
<!-- Proudly created with GPRM ( https://gprm.itsvg.in ) -->

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
- `crontab`: File defining default cron jobs.

## Notes

- **ALSA Audio**: Ensure your host system has the ALSA sound system installed and configured if you are using it for sound playback inside the container.
- **Timezone**: The container uses the host's timezone, which is set to `Asia/Kuala_Lumpur`.

## Troubleshooting

- **Audio Playback Issues**: Check if ALSA is properly configured on your host system.
- **Cron Logs**: If cron jobs are not executing, verify `/var/log/cron.log` inside the container for any errors.



