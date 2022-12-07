
## a hybrid cloud story

This demo is leveraging the [skupper example hello world](https://github.com/skupperproject/skupper-example-hello-world) demo to showcase the journey from a development enviroment to a hybrid-cloud deployment. During the walkthrough, the following concepts will be explored:

- how to build a secure container image? or how to include security at the early stage for a frictionless production-grade deployment
- how to deploy applications in a PaaS or even CaaS approach? or how to release in full "gated" autonomy
- how to support split front-end/back-end architecture? or how to leverage the cloud to deploy applications within data sovereignty environment

## requirements

This demo has been prepared for a Red Hat customers and partners using:
- [Red Hat OpenShift Local](https://developers.redhat.com/products/openshift-local/overview) running on a laptop and defined as the on-prem instance
- [Azure Red Hat OpenShift](https://azure.microsoft.com/nl-nl/products/openshift/#overview) - a Microsoft/Red Hat managed OpenShift cluster
- [Skupper](https://skupper.io/) - a multi cloud communication framework for Kubernetes  

???+ note

    Skupper has been selected in this context to provide a granular connectivity between the front-end and back-end across a secure network. Another solution using Submariner could be considered if unifying two cluster at a network level is required.  

