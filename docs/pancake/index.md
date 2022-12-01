# Project Pancake 

## Overview 
The scope of project *Pancake* is to demonstrating:

- the usage of of a microcontroller and basic electronic
- the Python programming language 
- containerizing applications
- refactoring in phases a monolithic application into microservices 
- deploying containers on a Kubernetes container platform

## Phase 1
Leveraging the *Raspberry Pico Wireless*, we will build a small rover controlled remotely by a simple web based application.
The hardware is composed of:  

- a Raspberry Pico Wireless 
- a L298N motor controller with 2 DC engines
- a NC522 NFC interface
- a 4-battery holder pack

The code, written in Python and deployed on the Raspberry Pico Wireless, provides the following features:
- connection capabilities to a wireless network
- access to a web application to drive the rover
- driving capabilities via left, right, forward, backward and stop functions
- detecting minerals of interests 

## Phase 2
The phase 1 outcome is a first prototype. Considering an edge scenario, this prototype would require to have a closed proximity to the rover per the wireless connection requirement but also due to the code being a monolithic software fully loaded on the rover itself.  
Considering these 2 elements, many constraints can be unveiled when using the rover limiting the flexibility and the remote capabilities for such a device.  

Phase 2 is addressing these 2 key elements by:

- refactoring the application into microservices
- containerizing the microservices
- leveraging the concept of Edge gateway

## Phase 3
While phase 2 was to address constraints, the phase 3 is about productizing the solution using a container platform, either on-prem, in the cloud or a hybrid cloud solution. 

Phase 3 is addressing the followings:

- securing the Edge connectivity using cloud native solutions
- applying GitOps principle to deploy and maintain the rover solution
- leveraging a hybrid cloud deployment for increased resilience 

