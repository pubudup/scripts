#Simple GUI to test MQTT pub sub
import tkinter as tk
import paho.mqtt.client as mqtt

def send_message():
    msg = entry.get()
    if msg:
        client.publish("test/iot/gui", msg)
        status_label.config(text=f"Sent: {msg}")
        entry.delete(0, tk.END)

client = mqtt.Client()
client.connect("test.mosquitto.org", 1883)
client.loop_start()

app = tk.Tk()
app.title("MQTT Publisher")

entry = tk.Entry(app, width=40)
entry.pack(pady=10)

send_btn = tk.Button(app, text="Send MQTT Message", command=send_message)
send_btn.pack(pady=5)

status_label = tk.Label(app, text="")
status_label.pack()

app.mainloop()
client.loop_stop()
client.disconnect()
