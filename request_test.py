import requests

response = requests.get("https://a2ksy3ej3y4vom-ats.iot.ap-southeast-1.amazonaws.com:8443/things/Device_Iot_1/shadow", cert=("Mqtts_app/Device_Iot_1/cert.pem", "Mqtts_app/Device_Iot_1/private.key"), verify="Mqtts_app/AmazonRootCA1.pem.txt")

# Inspect some attributes of the `requests` repository
#json_response = response.json()
print ( "response :" + str(response) )
print ( "body :" + str(response.json()))

mode = "auto"
ss_delta = "off"

response = requests.post("https://a2ksy3ej3y4vom-ats.iot.ap-southeast-1.amazonaws.com:8443/things/Device_Iot_1/shadow", cert=("Mqtts_app/Device_Iot_1/cert.pem", "Mqtts_app/Device_Iot_1/private.key")
, verify="Mqtts_app/AmazonRootCA1.pem.txt" , data = "{\"state\": {\"desired\":{\"mode\":\""+ mode +"\",\"Sensor\":\""+ ss_delta +"\"}}}")

print ( "response :" + str(response) )
print ( "body :" + str(response.json()))