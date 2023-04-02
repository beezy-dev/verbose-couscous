# Phase 1
Discover the basics of software architecture on a microcontroller compared to a single-board computer or standard computer.  
This phase will introduce a first software iteration to remotely control the robot from a simple web page.  

The code provides the following features:   
- connection to a pre-defined wireless network
- serve a web page to drive the rover (forward, backward, left, right, stop)
- detecting minerals of interests (optional)

This first phase will provide an usable robot and exposing a series of flaws.

## Workspace 


## Architecture 
The below table shows the hardware difference between:  

- a microcontroller like the Raspberry Pico Wireless
- a single board computer like the Raspberry Pi 4B 
- a standard computer specification overview 

| Summary |  Pico W    | Raspberry Pi 4B               | Computer           |
|---------|------------|-------------------------------|--------------------|
| CPU     |  2x133Mhz  | 4x1.8Ghz ARMv8                | up 5Ghz / 24+ core |
| RAM     |  256KB     | from 1GB to 8GB               | up 64 GB           |
| Disk    |  2MB       | SD card (up to 2TB)           | HDD (multi TB)     |
| Power   |  from 90 (no wifi) up to 260-370mA (wifi) | 540 to 1280mA | from 1400 to +4500mA |
| Autonomy on 4AA | between 20 to 50 hours | max 2 hours | n/a |
| Operating System | none | Linux or Windows for ARM | Linux, BSD, Windows |

Each solution has its own target:

- a microcontroller is perfect for embedded systems on battery 
- a single board controller targets kiosk or edge computer solutions 
- a standard computer provides the horse power for multitasking with productivity or even gaming

Last is the operating system consideration. While a SBC or a computer would have an operating system and compatible software to address the user needs, a microcontroller doesn't have per say an operating system. The Raspberry Pico has the following options:

- a MicroPython firmware capable of interpreting Python code (See [Pico Getting Started](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/0))
- a Pico SDK to develop in C/C++/ASM and build the firmware (See [Pico SDK](https://github.com/raspberrypi/pico-sdk))

While this is the two official ways of developing on a Raspberry Pico, other compiled languages like Rust could also be leverage to build a firmware. Check the video from [Low Level Learning](https://www.youtube.com/watch?v=Yi0WRF5WPFw).

## Software

The phase 1 source code is available [here](https://github.com/beezy-dev/project-pancake/blob/main/code/phase01/main.py).

By loading the below code, the microcontroller will connect to a local wireless network (to be configured) and provide a web server and basic HTML page to control the robot' s movement (forward, backward, left and right). 

```python
# Copyright 2022 Rom Adams (https://github.com/romdalf) at Red Hat Inc. 
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import utime  
import ujson
import network
import ubinascii
import machine
from machine import Pin
import socket

# getting a ISO8601 timestamp format
def timestamp():
    current_time = utime.localtime()
    time = '{:04d}-{:02d}-{:02d}T{:02d}:{:02d}:{:02d}Z'.format(
        current_time[0], current_time[1], current_time[2],
        current_time[3], current_time[4], current_time[5])
    return time

# print device and software info
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
print(f"{timestamp()} - WRCR: {mac} v0.1 DEV RELEASE")

# network connection ####################################################
networkName = ''
networkPassword= ''

# connecting to network 
def connecting():
    if not wlan.isconnected():
        print(f"{timestamp()} - WLAN connecting to network...")
        wlan.connect(networkName, networkPassword)
        print(f"{timestamp()} - WLAN waiting for connection...")
        while not wlan.isconnected():
            pass 
    ip = wlan.ifconfig()[0]
    print(f"{timestamp()} - WLAN connected on {networkName} with IP {ip}")
    return ip

# motor setup
motorOneFW = Pin(18, Pin.OUT)
motorOneBW = Pin(19, Pin.OUT)
motorTwoFW = Pin(20, Pin.OUT)
motorTwoBW = Pin(21, Pin.OUT)

# define movements
def moveStop():
    motorOneFW.value(0)
    motorOneBW.value(0)
    motorTwoFW.value(0)
    motorTwoBW.value(0)

def moveForward():
    motorOneFW.value(0)
    motorOneBW.value(1)
    motorTwoFW.value(0)
    motorTwoBW.value(1)
    utime.sleep_ms(250)
    moveStop()

def moveBackward():
    motorOneFW.value(1)
    motorOneBW.value(0)
    motorTwoFW.value(1)
    motorTwoBW.value(0)
    utime.sleep_ms(250)
    moveStop()

def moveLeft():
    motorOneFW.value(1)
    motorOneBW.value(0)
    motorTwoFW.value(0)
    motorTwoBW.value(1)
    utime.sleep_ms(250)
    moveStop()

def moveRight():
    motorOneFW.value(0)
    motorOneBW.value(1)
    motorTwoFW.value(1)
    motorTwoBW.value(0)
    utime.sleep_ms(250)
    moveStop()

# create a network socket
socketPort = 80
def networkSocket(ip):
    address = (ip, socketPort)
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print(f"{timestamp()} - Try to start a Network Socket...")
        connection.bind(address)
    except OSError:
        old = connection.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
        print(f"{timestamp()} - Socket state {old} already in use!")
        connection.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
        new = connection.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
        print(f"{timestamp()} -Socket state {new}")
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.bind(address)
    print(f"{timestamp()} - Socket started on {ip} on port {socketPort}")
    connection.listen(1)
    return connection

def webControl():
    html = f"""
            <!DOCTYPE html>
            <html>
            <head>
            <title>WRCR</title>
            </head>
            <center><b>
            <form action="./forward">
            <input type="submit" value="Forward" style="height:120px; width:120px" />
            </form>
            <table><tr>
            <td><form action="./left">
            <input type="submit" value="Left" style="height:120px; width:120px" />
            </form></td>
            <td><form action="./stop">
            <input type="submit" value="Stop" style="height:120px; width:120px" />
            </form></td>
            <td><form action="./right">
            <input type="submit" value="Right" style="height:120px; width:120px" />
            </form></td>
            </tr></table>
            <form action="./backward">
            <input type="submit" value="Backward" style="height:120px; width:120px" />
            </form>
            </body>
            </html>
            """
    return str(html)

def webServer(connection):
    print(f"{timestamp()} - webServer started with webControl as Index")
    while True:
        status = Pin("LED", Pin.OUT)
        status.toggle()
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        try:
            request = request.split()[1]
        except IndexError:
            print(f"{timestamp()} - webServer failed due to IndexError!")
            pass
        if request == '/forward?':
            print(f"{timestamp()} - webControl called for moveForward")
            moveForward()
        elif request == '/backward?':
            print(f"{timestamp()} - webControl called for moveBackward")
            moveBackward()
        elif request == '/right?':
            print(f"{timestamp()} - webControl called for moveRight")
            moveRight()
        elif request == '/left?':
            print(f"{timestamp()} - webControl called for moveLeft")
            moveLeft()
        elif request == '/stop?':
            print(f"{timestamp()} - webControl called for moveStop")
            moveStop()
        html = webControl()
        client.send(html)
        client.close()

try:
    ip = connecting()
    connection = networkSocket(ip)
    webServer(connection)
except KeyboardInterrupt:
    machine.reset()
``` 

## Limitations


