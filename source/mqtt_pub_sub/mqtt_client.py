import paho.mqtt.client as mqtt

# Callback when connected
def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    client.subscribe("test/iot/demo")

# Callback when a message is received
def on_message(client, userdata, msg):
    print(f"[{msg.topic}] {msg.payload.decode()}")

def on_publish(client, userdata, mid):
    print("mid: " + str(mid))
    client.publish("test/iot/demo", mid, payload=str(mid))

# Create client and connect
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()


