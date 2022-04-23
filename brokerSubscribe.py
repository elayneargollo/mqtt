import paho.mqtt.subscribe as subscribe

msg = subscribe.simple("elayne/data", hostname="127.0.0.1")
print(f"{msg.payload}")