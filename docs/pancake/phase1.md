## Phase 1
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
| Power   |  90mA (no wifi) up to 260-370mA (wifi) | 540mA (2.7W) to 1280mA (6.4W) | 
| Autonomy on 4AA | between 20 to 50 hours | max 2 hours | n/a |


## Software
The phase 1 source code is available [here](https://github.com/beezy-dev/project-pancake/blob/main/code/phase01/main.py).



