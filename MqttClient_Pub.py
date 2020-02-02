#!python3
import paho.mqtt.client as mqtt  #import the client1
import time

def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)

def on_message(client, userdata, msg):
    print("Message Receive" + msg.topic+" "+str(msg.payload))
    
mqtt.Client.connected_flag=False#create flag in class
broker="192.168.0.104"
client = mqtt.Client("mqtt_pub")             #create new instance 
client.on_connect=on_connect  #bind call back function
client.on_message=on_message  #bind call back function

print("Connecting to broker ",broker)
client.connect(broker)      #connect to broker
client.loop_start()
#print("Connecting to broker ","mqtt.eclipse.org")
#client.connect("mqtt.eclipse.org", 1883, 60)
while True : #not client.connected_flag: #wait in loop
    print("In wait loop")
    time.sleep(1)
    client.publish(topic="helloTopic",payload="Message from mqtt_pub",qos=0,retain=False)
    time.sleep(1)
print("in Main Loop")
client.loop_stop()    #Stop loop 
client.disconnect() # disconnect