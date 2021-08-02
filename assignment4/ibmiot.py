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
    t = cmd.data['text']
    print("printing: - - - ", t)
    print()


client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    temp=random.randint(-20,125)
    hum=random.randint(0,100)
    myData={'temperature':temp, 'humidity':hum}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: ", myData)
    client.commandCallback = myCommandCallback
    time.sleep(1)
client.disconnect()