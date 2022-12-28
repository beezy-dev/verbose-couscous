
# Keep your Secrets secret!

## Security Overview
The journey to secure a container platform could be overwheelming. Building a layer based or mindmap diagram can help to define the different components requiring attention. Here is an example of such mindmap, work in progress and not a definite/static diagram:

<img src="https://beezy.dev/images/mermaid-diagram-2022-12-28-131205.svg" width="75%" height="75%" >

<!--
This is the mermaid.js manifest for the mindmap diagram
 ```mermaid
mindmap
  kubernetes security
    Governance
      Everything as Code
      Regulations
      Business Continuity Plan 
      Security Posture Management
    Identity Access Entiltement Management
    Infrastructure 
      Operating System 
      Hardening 
      Patching Life Cycle
      Network
      Storage 
    Orchestrator 
      API
      etcd
      Scheduler 
      Network
      Registry
      Secrets
    Container
      Base Image
      Patching Life Cycle
      Code
      Mutation
      Secrets 
``` -->

This contribution is focusing on the etcd and secrets components listed within the above diagram. 

## Why etcd & secrets?