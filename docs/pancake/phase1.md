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

| Summary | Microcontroller          | Single Board Computer   | Computer           |
|---------|--------------------------|=======================--|--------------------|
| CPU     | 1 to 150 Mhz 1 or 2 core | up to 1Ghz / multi core | up 5Ghz / 24+ core |
| RAM     | 256 KB                   | up to 8GB               | up 64 GB           |
| Disk    | 2 MB                     | SD card (up to 2TB)     | HDD (multi TB)     |


## Software
The phase 1 source code is available [here](https://github.com/beezy-dev/project-pancake/blob/main/code/phase01/main.py).



