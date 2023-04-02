# Project Pancake 

## Overview 
The scope of project *Pancake* is to demonstrate an iterative design approach from both a software and hardware perspective while discovering the flaws at each iterations.   

During this process, we will be demonstrating:

- the Internet of Things (IoT) objects 
- the usage of of a microcontroller and basic electronic
- the Python programming language; and the more specific MicroPython flavor 
- containerizing applications
- refactoring in phases a monolithic application into microservices 
- deploying containers on a Kubernetes container platform

## Phase 0 
Discover the Internet of Things (IoT) objects and the basics of electronic to build the robot.

The hardware is composed of:   
- a Raspberry Pico Wireless 
- a breakout board for easy prototyping (optional)
- a L298N motor controller with 2 DC engines
- a 4-battery holder pack
- a NC522 NFC interface (optional)

## Phase 1
Discover the basics of software architecture on a microcontroller compared to a single-board computer or standard computer.  
This phase will introduce a first software iteration to remotely control the robot from a simple web page.  

The code provides the following features:   
- connection to a pre-defined wireless network
- serve a web page to drive the rover (forward, backward, left, right, stop)
- detecting minerals of interests (optional)

This first phase will provide an usable robot and exposing a series of flaws.

## Phase 2
Discover the basics of edge gateway from a hardware and software perspective.  

Phase 2 is addressing these 2 key elements by:   
- refactoring the application into microservices
- containerizing the microservices
- leveraging the concept of Edge gateway

## Phase 3
Discover the basics of IoT fleet management and Edge-as-Service. 

Phase 3 is addressing the followings:  
- securing the Edge connectivity using cloud native solutions
- applying GitOps principle to deploy and maintain the rover solution
- leveraging a hybrid cloud deployment for increased resilience 

## Bill of Material (BoM)

### Software
- a computer with [Thonny](https://thonny.org/) installed 
- a text editor like [Sublime](https://www.sublimetext.com/) or [vscodium](https://vscodium.com/) 
- Internet 

### Hardware
The below table shows a set of required and optional components. The optional components are to extend the learning and experience of the robot.  

| QTY | Article                                   | Price |
|-----|------------------------------------------ |-------|
| 1   | Rapsberry Pi PICO Wireless with header    | $10   | 
| 1   | KeeYees L298N Motor Kit with Jump Wires   | $4    | 
| 1   | HiLetGo 4xAA or 9V Battery Clip           | $2    | 
| 1   | USB to micro USB cable 1-meter            | $3    | 
|     | TOTAL                                     | $19   |

| QTY | Optional Article                          | Price |
|-----|------------------------------------------ |-------|
| 1   | Freenove Breakout board Raspberry Pi Pico | $13   | 
| 1   | HiLetGo Mifare RC522 RF + S50 Blank Card  | $6    | 
|     | TOTAL                                     | $62   | 
 
???+ note
    When working in a workshop style, some of the above items are available in bulk with a interesting discount.


