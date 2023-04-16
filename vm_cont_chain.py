import paho.mqtt.client as mqtt
import time

user = "mihirsin"

def on_connect(client, userdata, flags, rc):
    client.subscribe(f"{user}/ping")
    client.message_callback_add(f"{user}/ping", on_message_from_ping)

def on_message_from_ping(client, userdata, message):
    num = int(message.payload.decode().split(':')[1].strip())
    time.sleep(1)
    client.publish(f"{user}/pong", f"msg: {num + 1}")
    print(f"msg: {num + 1}")

if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(host="localhost", keepalive=60)
    client.loop_forever()