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



