################################################### Connecting to AWS
import boto3
import os
import json
################################################### Create random name for things
import random
import string

################################################### Parameters for Thing
thingArn = ''
thingId = ''
thingNamePre = "Device_Iot_"
DeviceNumber = 2
thingName = ""#''.join([random.choice(string.ascii_letters + string.digits) for n in range(15)])
defaultPolicyName = 'Ex-Iot-Policy'
###################################################

def createThing():
    global thingClient
    thingResponse = thingClient.create_thing(
        thingName = thingName
    )
    data = json.loads(json.dumps(thingResponse, sort_keys=False, indent=4))
    for element in data: 
        if element == 'thingArn':
            thingArn = data['thingArn']
        elif element == 'thingId':
            thingId = data['thingId']
        createCertificate()

def createCertificate():
	global thingClient
	certResponse = thingClient.create_keys_and_certificate(
			setAsActive = True
	)
	data = json.loads(json.dumps(certResponse, sort_keys=False, indent=4))
	for element in data: 
			if element == 'certificateArn':
					certificateArn = data['certificateArn']
			elif element == 'keyPair':
					PublicKey = data['keyPair']['PublicKey']
					PrivateKey = data['keyPair']['PrivateKey']
			elif element == 'certificatePem':
					certificatePem = data['certificatePem']
			elif element == 'certificateId':
					certificateId = data['certificateId']
    					
	with open(thingName +'/public.key', 'w') as outfile:
			outfile.write(PublicKey)
	with open(thingName +'/private.key', 'w') as outfile:
			outfile.write(PrivateKey)
	with open(thingName +'/cert.pem', 'w') as outfile:
			outfile.write(certificatePem)

	response = thingClient.attach_policy(
			policyName = defaultPolicyName,
			target = certificateArn
	)
	response = thingClient.attach_thing_principal(
			thingName = thingName,
			principal = certificateArn
	)
    
for deviceID in range(DeviceNumber) :
    thingName = thingNamePre + str(deviceID)
    os.mkdir(thingName)	
    thingClient = boto3.client('iot')
    createThing()