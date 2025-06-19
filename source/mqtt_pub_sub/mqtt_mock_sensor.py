import paho.mqtt.client as mqtt
import time
import json

client = mqtt.Client()
client.connect("test.mosquitto.org", 1883)
client.loop_start()

# Load fake sensor data from file
with open("data/sensor_data.json", "r") as f:
    data = json.load(f)

for entry in data:
    payload = json.dumps(entry)
    print("Publishing:", payload)
    client.publish("test/iot/sensors", payload)
    time.sleep(2)

client.loop_stop()
client.disconnect()
