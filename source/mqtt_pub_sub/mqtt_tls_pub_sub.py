import time

import paho.mqtt.client as mqtt
import ssl

client = mqtt.Client()

client.tls_set(cert_reqs=ssl.CERT_NONE)  # Accept any cert (for testing)
client.tls_insecure_set(True)            # Allow self-signed

client.connect("test.mosquitto.org", 8883)
client.loop_start()

#client.publish("test/iot/secure", "Secure MQTT connection")

# 📨 Publish a message every 5 seconds
BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "test/iot/demo"

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