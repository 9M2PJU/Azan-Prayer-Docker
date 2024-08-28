import re

def read_prayer_times(file_path):
    prayer_times = []

    with open(file_path, "r") as file:
        for line in file:
            match = re.match(r"Prayer (\d+): \d{4}-\d{2}-\d{2} (\d{2}:\d{2}):\d{2}", line)
            if match:
                prayer_index = int(match.group(1))
                if prayer_index != 1:  # Exclude Prayer 1
                    prayer_time_str = match.group(2)
                    prayer_times.append((prayer_index, prayer_time_str))

    print("Parsed Prayer Times:", prayer_times)  # Debugging line
    return prayer_times

def add_cron_jobs(prayer_times):
    cron_jobs = []

    for prayer_index, prayer_time_str in prayer_times:
        prayer_hour, prayer_minute = map(int, prayer_time_str.split(':'))
        if prayer_index == 0:
            audio_file = "/app/mp3/azan2.mp3"
        else:
            audio_file = "/app/mp3/azan.mp3"
        command = f"mpg123 {audio_file}"
        cron_job = f"{prayer_minute} {prayer_hour} * * * {command} # Prayer Time\n"
        cron_jobs.append(cron_job)

    # Read existing crontab entries
    try:
        with open('/etc/crontabs/root', 'r') as cron_file:
            existing_cron_jobs = cron_file.readlines()
    except FileNotFoundError:
        existing_cron_jobs = []

    # Append new cron jobs, avoiding duplicates
    with open('/etc/crontabs/root', 'w') as cron_file:
        # Write existing jobs first
        cron_file.writelines(existing_cron_jobs)
        # Write new jobs
        for job in cron_jobs:
            if job not in existing_cron_jobs:
                cron_file.write(job)

def main():
    file_path = "/app/prayer_data/prayer.txt"  # Adjusted path
    prayer_times = read_prayer_times(file_path)
    add_cron_jobs(prayer_times)

if __name__ == "__main__":
    main()

