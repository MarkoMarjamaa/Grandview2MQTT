# Grandview2MQTT
Control Grandview motorized screen with serial and control it as cover in Home Assistant

create /home/pi/grandview2mqtt dir and place files there. 

update grandview2mqtt.py with your environment

# Adddress of your MQTT broker
broker_address="homeautomation"

# Should be normally this. 
discovery_topic="homeassistant"

my_topic="Grandview2MQTT"
# Serial port for your Grandview. I use udev to name ports
port="/dev/grandview"

# Name of the screen. Can run several screens in same environment
object_name="Living Room Screen"
object_id="living_room_screen"



# can run directly 
python3 grandview2mqtt.py

# or Start as service
sudo cp grandview2mqtt.service /etc/systemd/system
systemctl enable grandview2mqtt
systemctl restart grandview2mqtt
systemctl status grandview2mqtt
