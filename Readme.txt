* Simulation mqtt clien using python and paho lib with mosquito

1. Install pyho lib for python
pip install paho-mqtt

2. Install mosquito to simulate broker for mqtt server

3. Run mosquito
+ initial broker
mosquito - v
+ send message to topic
mosquitto_pub -m [message] -t [topic]
+ listen from topic
mosquitto_sub -t [topic]

4. Run 2 script to public message MqttClient_Pub.py and subcribe message  MqttClient_Sub.py from mosquito


* Simulation mqtts with AWS:

1. Install awscli for python : pip install awscli 
and config with you acc to use : ( take keys from your account )
Ex :
$ aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: us-west-2
Default output format [None]: json 

2. Change DeviceNumber in Mqtts_setup.py and run this script to create the things for your AWS account
This script will create things and download certificates to connect with each thing in your AWS account .

3. Change directory of certificates from Mqtts_device.py and Mqtts_app.py to connect from client and app to your AWS account
Run Mqtts_device.py and Mqtts_app.py to simulate divice and app connect with your account via mqtts.
Change temperature ( from device ) , mode ( manual or auto ) , sensor ( on or off ) to simulation operation of sensor.

Note : It simulation app connect with account via AWS, we can connect form app to account via http by using example from request_test.py 


 

