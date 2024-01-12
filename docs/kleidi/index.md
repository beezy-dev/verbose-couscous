# kleidi 

From the Greek ```κλειδί``` or key, this project aims to:  
* provide an universal Key Management Services (KMS) provider plugin for Kubernetes
* learn how to develop a containerized software interacting with the Kubernetes API server 

![kleidi](../images/DALL-E-kleidi_comic_strip.png)

## context
Secrets objects in Kubernetes stored in ```etcd``` with their data field encoded in base64 which is readable by everyone. While applications could see their Secrets being stored externally, the ones used by the platform itself can not be offloaded to avoid a collapse of the platform in case of network partitioning. 

Also, most of the third party solutions attempting to address the Secrets management have a fallback mechanism to the standard Kubernetes Secrets objects. This means that the security exposure is sooner or later to be addressed The Kubernetes project offers options to [encrypt data at rest](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/) mitigating to some degrees this security exposure.   

For more details about the security exposure, mitigation path, and production-grade solutions, this handbook I co-authored is a perfect referrence: [Kubernetes Secrets Handbook](https://www.packtpub.com/product/kubernetes-secrets-handbook/).

The only viable option for a productio-grade environment is through the usage of the KMS provider plugin. With the releave of Kubernetes ```1.29```, the KMSv2 is marked stable and documented in the article [KMS provider for data encryption](https://kubernetes.io/docs/tasks/administer-cluster/kms-provider/). 

The ```kleidi``` project will based its efforts on the Kubernetes KMSv2 architecture. 

## KMSv2 architecture 

Like with networking, storage, cloud providers, and more, Kubernetes provides a high level abstraction to simplify the integration with third party components, and the KMSv2 provider plugin follows the same principle.   

The Kubernetes API Server has been improved to include the 

## kleidi business requirements

* Go
* rootless; might be difficult considering the GRPC nature
* modular to ease the onboarding of new KMS 3rd party
    * a dummy encryption module using GPG or similar encryption technique
    * leverage a (virtual) Trust Platform Module as a first module
* metrics 
* audit logs 
* Helm Charts and Operator deployment model

## kleidi architecture 


## repository


