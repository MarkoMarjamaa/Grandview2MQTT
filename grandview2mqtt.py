import paho.mqtt.client as mqtt
import json
import serial

broker_address="homeautomation"
discovery_topic="homeassistant"
my_topic="Grandview2MQTT"
port="/dev/grandview"
object_name="Living Room Screen"
object_id="living_room_screen"

############
def on_message(client, userdata, message):
    command = str(message.payload.decode("utf-8"))
    if command == "OPEN":
#            print("Opening")
            ser = serial.Serial(port=port,baudrate=2400,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)
            ser.write(b'\xFF\xEE\xEE\xEE\xDD')
            ser.close()
            client.publish(my_topic+"/cover/"+object_id+"/state","opening", retain=True)
    elif command == "CLOSE":
#            print("Closing")
            ser = serial.Serial(port=port,baudrate=2400,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)
            ser.write(b'\xFF\xEE\xEE\xEE\xEE')
            ser.close()
            client.publish(my_topic+"/cover/"+object_id+"/state","closing", retain=True)
    elif command == "STOP":
#            print("Stopping")
            ser = serial.Serial(port=port,baudrate=2400,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)
            ser.write(b'\xFF\xEE\xEE\xEE\xCC')
            ser.close()
            client.publish(my_topic+"/cover/"+object_id+"/state","stopped", retain=True)
    else:
# Step Up
# Serial.Write(u'\\xFF\\xEE\\xEE\\xEE\\xC9')
# Step Down
# Serial.Write(u'\\xFF\\xEE\\xEE\\xEE\\xE9')
            print("WTF")

########################################

print("creating new instance")
client = mqtt.Client(my_topic+"_"+ object_id)
client.on_message=on_message #attach function to callback

print("connecting to broker")
client.connect(broker_address)

print("Subscribing to topic",my_topic+"/cover/"+object_id+"/set")
client.subscribe(my_topic+"/cover/"+object_id+"/set")

print("Publishing discovery message to topic",discovery_topic+"/cover/"+object_id+"/config")
config_data = {
    "~": my_topic+"/cover/"+object_id, 
    "name": object_name, 
    "cmd_t": "~/set", 
    "stat_t": "~/state",
    "device": {
        "name": "Grandview Motorized Screen",
        "manufacturer": "Grandview",
        "model": "LF-M106", 
        "identifiers":["Grandview2MQTT_"+port]
#	"connections": [ "port", port ]
        }
    }
print (json.dumps(config_data))
client.publish(discovery_topic+"/cover/"+object_id+"/config",json.dumps(config_data), retain=True)

#print("Publishing message to topic",my_topic+"/cover/"+object_id+"/set")
#client.publish(my_topic+"/cover/"+object_id+"/set","OPEN")
#client.publish(my_topic+"/cover/"+object_id+"/set","STOP")
#client.publish(my_topic+"/cover/"+object_id+"/set","CLOSE")

client.loop_forever()
