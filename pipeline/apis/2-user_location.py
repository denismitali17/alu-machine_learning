#!/usr/bin/env python3
"""
Script that prints the location of a specific GitHub user
"""

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
            current_timestamp = int(time.time())
            minutes_left = (reset_timestamp - current_timestamp) // 60
            print(f"Reset in {minutes_left} min")
        else:
            print("Reset in unknown time")
    elif response.status_code == 200:
        data = response.json()
        location = data.get("location")
        # Handle None or missing location
        if location:
            print(location)
        else:
            print("Not found")
    else:
        print("Error: Unexpected response")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./2-user_location.py <GitHub API user URL>")
    else:
        main(sys.argv[1])
