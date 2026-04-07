import random
import time

def generate_vehicle_data():
    return {
        "speed": random.randint(0, 120),
        "engine_temp": random.randint(70, 120),
        "fuel_level": random.randint(0, 100)
    }

while True:
    data = generate_vehicle_data()
    print(data)
    time.sleep(2)