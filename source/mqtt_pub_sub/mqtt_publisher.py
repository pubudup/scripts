import paho.mqtt.client as mqtt
import time

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "test/iot/demo"

# Called when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    print("Connected with result code:", rc)
    client.subscribe(TOPIC)

# Called when a subscribed message is received
def on_message(client, userdata, msg):
    print(f"[{msg.topic}] {msg.payload.decode()}")

# Create MQTT client
client = mqtt.Client()

# Set callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to public broker
client.connect(BROKER, PORT, keepalive=60)

# Start a background thread to handle network events
client.loop_start()

# 📨 Publish a message every 5 seconds
try:
    count = 1
    while True:
        message = f"Hello MQTT! Message #{count}"
        print(f"Publishing: {message}")
        client.publish(TOPIC, message)
        count += 1
        time.sleep(5)

except KeyboardInterrupt:
    print("Exiting...")
    client.loop_stop()
    client.disconnect()
