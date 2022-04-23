import paho.mqtt.client as mqtt

mqttc = mqtt.Client()
mqttc.connect("127.0.0.1", 1883)
mqttc.publish("elayne/data", "{umidade: 26, temperatura: 32}")
mqttc.loop(2)