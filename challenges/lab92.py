#!/usr/bin/env python3

# Import modules
import requests
import datetime

def main():

  # Get JSON obj and pull out lat/lon/timestamp
  response = requests.get("http://api.open-notify.org/iss-now.json").json()
  latitude = response["iss_position"]["latitude"]
  longitute = response["iss_position"]["longitude"]
  timestamp = datetime.datetime.fromtimestamp(response["timestamp"])

  print(f"CURRENT LOCATION OF THE ISS:\nTimestamp: {timestamp}\nLatitude: {latitude}\nLongitude: {longitute}")


# Run main
if __name__ == "__main__":
  main()
