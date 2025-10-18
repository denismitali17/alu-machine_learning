#!/usr/bin/env python3
import requests
import sys
import time

def main(url):
    response = requests.get(url)

    if response.status_code == 404:
        print("Not found")
    elif response.status_code == 403:
        reset_time = response.headers.get("X-RateLimit-Reset")
        if reset_time:
            reset_timestamp = int(reset_time)
            minutes_left = (reset_timestamp - int(time.time())) // 60
            print(f"Reset in {minutes_left} min")
        else:
            print("Reset in unknown time")
    elif response.status_code == 200:
        data = response.json()
        location = data.get("location")
        print(location if location else "Not found")
    else:
        print("Error: Unexpected response")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python 2-user_location.py https://api.github.com/users/holbertonschool")
    else:
        main(sys.argv[1])
