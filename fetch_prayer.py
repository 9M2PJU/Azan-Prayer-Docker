import requests
from datetime import datetime
import os

def fetch_prayer_times(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        prayer_times = data['response']['times']
        return prayer_times
    except requests.exceptions.RequestException as e:
        print("An error occurred while fetching prayer times:", e)
        return []

def write_to_file(prayer_times):
    file_path = "/app/prayer_data/prayer.txt"  # Adjusted path
    with open(file_path, "w") as file:
        for idx, prayer_time in enumerate(prayer_times):
            prayer_datetime = datetime.fromtimestamp(prayer_time)
            formatted_time = prayer_datetime.strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"Prayer {idx}: {formatted_time}\n")

def main():
    fetch_url = "https://mpt.i906.my/mpt.json?code=wlp-0&filter=1"
    prayer_times = fetch_prayer_times(fetch_url)

    if not prayer_times:
        print("No prayer times fetched.")
        return

    write_to_file(prayer_times)

if __name__ == "__main__":
    main()

