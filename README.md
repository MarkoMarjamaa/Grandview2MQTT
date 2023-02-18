# Grandview2MQTT
Control Grandview motorized screen with serial and control it as cover in Home Assistant

Create /home/pi/grandview2mqtt dir and place files there. 

Might have to install Paho. 
```
pip3 install paho-mqtt
```

Update grandview2mqtt.py with your environment
```
# Address of your MQTT broker server
broker_address="homeautomation"

# Homeassistant discovery topic (normally no need to change ) 
discovery_topic="homeassistant"

# This scripts own topic. No need to change. 
my_topic="Grandview2MQTT"

# Serial port for your Grandview. I use udev to name ports
port="/dev/grandview"

# Name of the screen. Can run several screens in same environment
object_name="Living Room Screen"
object_id="living_room_screen"
```


Can run directly 
```
python3 grandview2mqtt.py
```
Or start as service
```
sudo cp grandview2mqtt.service /etc/systemd/system
systemctl enable grandview2mqtt
systemctl restart grandview2mqtt
systemctl status grandview2mqtt
```
