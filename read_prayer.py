import re
from datetime import datetime

def read_prayer_times(file_path):
    prayer_times = []

    with open(file_path, "r") as file:
        for line in file:
            match = re.match(r"Prayer (\d+): \d{4}-\d{2}-\d{2} (\d{2}:\d{2}):\d{2}", line)
            if match:
                prayer_index = int(match.group(1))
                if prayer_index != 1:  # Exclude Prayer 1 (Subuh)
                    prayer_time_str = match.group(2)
                    prayer_times.append((prayer_index, prayer_time_str))

    print("Parsed Prayer Times:", prayer_times)  # Debugging line
    return prayer_times

def add_cron_jobs(prayer_times):
    cron_jobs = []

    # Get the current date and time for comments
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M")

    # Prayer names mapping
    prayer_names = {
        0: "Subuh",
        2: "Zohor",
        3: "Asar",
        4: "Maghrib",
        5: "Isyak"
    }

    # Add cron jobs for prayer times
    for prayer_index, prayer_time_str in prayer_times:
        prayer_hour, prayer_minute = map(int, prayer_time_str.split(':'))
        audio_file = "/app/mp3/azan2.mp3" if prayer_index == 0 else "/app/mp3/azan.mp3"
        command = f"mpg123 {audio_file}"
        prayer_name = prayer_names.get(prayer_index, f"Prayer {prayer_index}")
        cron_job = f"{prayer_minute} {prayer_hour} * * * {command} # {prayer_name} - Fetched on {date_str} at {time_str}\n"
        cron_jobs.append(cron_job)

    # Add cron job for fetching prayer times at 4 AM daily
    fetch_prayer_command = "python3 /app/fetch_prayer.py"
    fetch_prayer_cron_job = f"0 4 * * * {fetch_prayer_command} # Fetch Prayer Times - Fetched on {date_str} at {time_str}\n"
    cron_jobs.append(fetch_prayer_cron_job)

    # Add cron job to read prayer times after fetching them at 4:01 AM
    read_prayer_command = "python3 /app/read_prayer.py"
    read_prayer_cron_job = f"1 4 * * * {read_prayer_command} # Read Prayer Times - Fetched on {date_str} at {time_str}\n"
    cron_jobs.append(read_prayer_cron_job)

    # Write the updated crontab, replacing all previous "Prayer" jobs
    with open('/etc/crontabs/root', 'w') as cron_file:
        for job in cron_jobs:
            cron_file.write(job)

def main():
    file_path = "/app/prayer_data/prayer.txt"  # Adjusted path
    prayer_times = read_prayer_times(file_path)
    add_cron_jobs(prayer_times)

if __name__ == "__main__":
    main()
    
