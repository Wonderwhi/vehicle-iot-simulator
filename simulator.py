import random
import time
import requests

URL = "http://127.0.0.1:5000/data"

def generate_vehicle_data():
    return {
        "speed": random.randint(0, 120),
        "engine_temp": random.randint(70, 120),
        "fuel_level": random.randint(0, 100)
    }

while True:
    data = generate_vehicle_data()
    print("Sending:", data)

    try:
        requests.post(URL, json=data)
    except:
        print("Server not running")

    time.sleep(2)