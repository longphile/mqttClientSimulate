from paho.mqtt import client as mqtt
import time
import ssl
import sys
import threading
import json

device_pre = 'Device_Iot_'
device_id = device_pre + '1'#str(sys.argv[0])
path_folder = 'D:/Python/Mqtts_app/'
path_folder_full = path_folder + device_id + '/'
path_to_root_cert = path_folder + "AmazonRootCA1.pem.txt"
path_to_cert_file = path_folder_full + "cert.pem"#"D:/Python/Cert_Aws/24519cda64-certificate.pem.crt"#
path_to_key_file  = path_folder_full + "private.key"#"D:/Python/Cert_Aws/24519cda64-private.pem.key"#
hostName = "a2ksy3ej3y4vom-ats.iot.ap-southeast-1.amazonaws.com"
portNumber = 8883
#"Ex_Iot_1"
#sas_token = "<generated SAS token>"
#iot_hub_name = "<iot hub name>"

mode = "auto" # auto or manual
temperature = 30
ss_delta = 'off'
ss_desire = "off"


def on_connect(client, userdata, flags, rc):
    print("Device connected with result code: " + str(rc))


def on_disconnect(client, userdata, rc):
    print("Device disconnected with result code: " + str(rc))

def on_message(client, userdata, msg):
    global ss_delta
    global mode
    global temperature
    print("Message Receive " + msg.topic+" "+str(msg.payload))
    s = str(msg.payload.decode("utf-8"))
    json_dict = json.loads(s)
    if str(json_dict['state']['reported']['Temperature']) != temperature :
        temperature = str(json_dict['state']['reported']['Temperature'])
        print( "temperature : " + temperature)
    if str(json_dict['state']['reported']['Sensor']) != ss_delta :
        ss_delta = str(json_dict['state']['reported']['Sensor'])
        print( "Sensor : " + ss_delta)
    
def on_publish(client, userdata, mid):
    print("Device sent message")
    
def on_log(client, userdata, level , buf):
    print("log" + buf)

client = mqtt.Client(client_id='App'+ device_id, protocol=mqtt.MQTTv311)

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish
client.on_message = on_message
client.on_log = on_log 
#client.username_pw_set(username=iot_hub_name+".azure-devices.net/" +
#                       device_id + "/?api-version=2018-06-30", password=sas_token)

client.tls_set(ca_certs=path_to_root_cert, certfile=path_to_cert_file, keyfile=path_to_key_file,
               cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
client.tls_insecure_set(False)

client.connect(hostName , port =portNumber)

def PublicTopic():
    global ss_delta
    global mode
    global device_id
    #print ("$aws/things/"+ ss_delta + "/shadow/update")
    while True : #not client.connected_flag: #wait in loop 
        time.sleep(3)
        print ("nhap mode ( auto or manual )")
        mode_temp = input()
        mode = mode_temp
        if mode == "manual" :
            client.publish(topic = "$aws/things/"+ device_id + "/shadow/update", payload="{\"state\": {\"desired\":{\"mode\":\""+ mode +"\",\"Sensor\":\""+ ss_delta +"\"}}}" ,qos=0) #"$aws/things/Ex_Iot_1/shadow/update" 
        if mode == "manual" :
            print ("nhap sensor (on or off)")
            ss_delta_temp = input()
            if ss_delta_temp != ss_delta :
                ss_delta = ss_delta_temp
                client.publish(topic = "$aws/things/"+ device_id + "/shadow/update", payload="{\"state\": {\"desired\":{\"mode\":\""+ mode +"\",\"Sensor\":\""+ ss_delta +"\"}}}" ,qos=0) #"$aws/things/Ex_Iot_1/shadow/update" 

x = threading.Thread(target=PublicTopic, args=())
x.start()

client.subscribe(topic = "$aws/things/" + device_id +"/shadow/update/accepted",qos=1)
client.loop_forever()
