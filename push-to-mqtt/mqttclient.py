import paho.mqtt.client as paho
mqttc = paho.Client()
 
# Settings for connection
host = "mqtt.netpie.io"
topic= "mbed-sample/#"
port = 1883
 
# Callbacks
def on_connect(mosq, obj, rc):
    print("connect rc: "+str(rc))
    mqttc.publish("mbed-sample","Python Script Test Message.");
 
def on_message(mosq, obj, msg):
    print( "Received on topic: " + msg.topic + " Message: "+str(msg.payload) + "\n");
 
def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed OK")
 
# Set callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
 
# Connect and subscribe
print("Connecting to " +host +"/" +topic)
mqttc.connect(host, port, 60)
mqttc.subscribe(topic, 0)
 
# Wait forever, receiving messages
rc = 0
while rc == 0:
    rc = mqttc.loop()
 
print("rc: "+str(rc))
 
