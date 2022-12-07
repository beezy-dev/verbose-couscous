
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

## running locally 

```bash title="start OpenShift Local"
➜  ~ crc start
```

outputing: 
```
WARN A new version (2.11.0) has been published on https://developers.redhat.com/content-gateway/file/pub/openshift-v4/clients/crc/2.11.0/crc-macos-installer.pkg 
INFO Checking if running as non-root              
INFO Checking if crc-admin-helper executable is cached 
INFO Checking for obsolete admin-helper executable 
INFO Checking if running on a supported CPU architecture 
INFO Checking minimum RAM requirements            
INFO Checking if crc executable symlink exists    
INFO Checking if running emulated on a M1 CPU     
INFO Checking if vfkit is installed               
INFO Checking if old launchd config for tray and/or daemon exists 
INFO Checking if crc daemon plist file is present and loaded 
INFO Loading bundle: crc_vfkit_4.11.7_amd64...    
CRC requires a pull secret to download content from Red Hat.
You can copy it from the Pull Secret section of https://console.redhat.com/openshift/create/local.
? Please enter the pull secret **************************************************************************************************

INFO Creating CRC VM for openshift 4.11.7...      
INFO Generating new SSH key pair...               
INFO Generating new password for the kubeadmin user 
INFO Starting CRC VM for openshift 4.11.7...      
INFO CRC instance is running with IP 127.0.0.1    
INFO CRC VM is running                            
INFO Updating authorized keys...                  
INFO Check internal and public DNS query...       
INFO Check DNS query from host...                 
INFO Verifying validity of the kubelet certificates... 
INFO Starting kubelet service                     
INFO Waiting for kube-apiserver availability... [takes around 2min] 
INFO Adding user's pull secret to the cluster...  
INFO Updating SSH key to machine config resource... 
INFO Waiting for user's pull secret part of instance disk... 
INFO Changing the password for the kubeadmin user 
INFO Updating cluster ID...                       
INFO Updating root CA cert to admin-kubeconfig-client-ca configmap... 
INFO Starting openshift instance... [waiting for the cluster to stabilize] 
INFO 3 operators are progressing: image-registry, openshift-controller-manager, service-ca 
INFO 3 operators are progressing: image-registry, openshift-controller-manager, service-ca 
INFO 3 operators are progressing: image-registry, openshift-controller-manager, service-ca 
INFO 3 operators are progressing: image-registry, openshift-controller-manager, service-ca 
INFO 2 operators are progressing: image-registry, openshift-controller-manager 
INFO 2 operators are progressing: image-registry, openshift-controller-manager 
INFO Operator openshift-controller-manager is progressing 
INFO Operator openshift-controller-manager is progressing 
INFO Operator openshift-controller-manager is progressing 
INFO Operator openshift-controller-manager is progressing 
INFO All operators are available. Ensuring stability... 
INFO Operators are stable (2/3)...                
INFO Operators are stable (3/3)...                
INFO Adding crc-admin and crc-developer contexts to kubeconfig... 
Started the OpenShift cluster.

The server is accessible via web console at:
  https://console-openshift-console.apps-crc.testing

Log in as administrator:
  Username: kubeadmin
  Password: cKiLy-5umju-GnxbP-Lfqpb

Log in as user:
  Username: developer
  Password: developer

Use the 'oc' command line interface:
  $ eval $(crc oc-env)
  $ oc login -u developer https://api.crc.testing:6443
```

### log in as admin 

```bash title="log in as admin"
➜  ~ eval $(crc oc-env)
➜  ~ oc login -u kubeadmin https://api.crc.testing:6443
```

outputing: 
```
Logged into "https://api.crc.testing:6443" as "kubeadmin" using existing credentials.

You have access to 66 projects, the list has been suppressed. You can list all projects with 'oc projects'

Using project "default".
```
