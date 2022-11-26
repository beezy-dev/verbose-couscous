# Project Pancake 

Project Pancake is demonstrating the concept of Open Hybrid Cloud with a far edge scenario.  

The setup is composed of:  

- a control station 
- an Red Hat OpenShift cluster deployed within a Public Cloud
  - a control service
  - a web service (NGINX + MongoDB) to record sessions
  - Prometheus + Grafana to expose metrics 
- an Red Hat Edge Gateway (optional)
  - a control service 
- an Edge device 

The scenario is as follow:   

- an user controls remotely a device by gesture captured via a webcam on the control station.
- the control station sends the gestures to the control service.
- the control service sends:
  - a entry into Prometheus
  - a feedback to the web service
  - the requests to the device

In far Edge scenario, the connectivity could be a challenge. To mitigate communication failure, an Edge gateway could be deployed closer to the Edge device as a reliable connectivity option.    
Considering this scenario, the Edge gateway could either be:  

- a Red Hat OpenShift remote worker
- a Red Hat Edge Device with Podman or Microshift

This scenario will be explored.   