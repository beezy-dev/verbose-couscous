# Standard Application Entry Process (SAEP)

## business requirements
Whatever if applications are bought, built internally or externally, there is a need of defining the golden path, a process to onboard these assets.

This standard process will help fast tracking the time to production as we can guarantee that the target application is compliant with the organization's governance. 

## prerequisites
The following is required to onboard an application through the SAEP: 
* Git repository
* Container image registry 
* An OpenShift target

## workflow overview

is the app
* COTS
* build externally 
* build internally

is the app have all the requirements?
* containerized payload?
    * scan
    * sbom
    * ubi
* deployment method (helm, operator)
* documentation

is containerized
* yes
* no

is there a deploy method
* yes
* no

is there documentation?
* yes 
* no

```mermaid
sequenceDiagram
box Vendors
participant Third-Party
participant Application
end
box CCP Git Runners
participant Cloud Artifactory
participant Cloud Git
participant Cloud Registry
participant Build
end
box CCP OCP
participant Helm Charts
participant OCP
participant CI-CD
participant Testing
end
  Third-Party->>Application: cots or external dev
  alt if cots
    Application->>Cloud Artifactory: push binary
  end
  alt if external development
    Application->>Cloud Git: push source code
  end
  Cloud Git->>Build: triggered pipeline job
  alt if failed built job
    Build->>Cloud Git: push built logs and break
  end
  Build->>Cloud Git: push built logs
  Build->>Cloud Registry: push signed container image
  Build->>Helm Charts: pre-flight checks
  alt if pre-flight checks fail
    Helm Charts->>Cloud Git: push failed logs and break
  end
  Pre-flights->>OCP: add Helm Charts to Catalogue
  OCP->>CI-CD: trigger deploy pipeline job
  alt if deploy fails
    CI-CD->>Git Cloud: push failed logs and break
  end
  CI-CD->>Testing: trigger f and nf testing
```

