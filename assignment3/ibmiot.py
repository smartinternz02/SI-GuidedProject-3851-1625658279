import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "fhmboz",
        "typeId": "PragatiDevice",
        "deviceId":"12312"
    },
    "auth": {
        "token": "njwe9hfaidn1"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    tankLevels=random.randint(0,100)
    lightIntensity=random.randint(0,100)
    myData={'tankLevels':tankLevels, 'lightIntensity':lightIntensity}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: ", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()