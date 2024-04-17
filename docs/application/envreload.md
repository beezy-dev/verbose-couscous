# reload, restart or redeploy

## context
Containerized application deployed on Kubernetes, manually or via GitOps, is composed of multiple objects from namespace, deployment, configmaps, secrets, services, and more. Most are static while other will be updated during the application lifecycle. 

Most of these object defintions are static while others will be updated with no to significant impact on the application, e.g.:   

* changing a service impacts the access but not the application.
* changing a data backend secret impacts the application with crashing, providing corrupted and/or outdated response.  
* changing a namespace or a deployment will require a redeployment of the application, meaning full disruption. 

How can we address these use cases?

### the application

The ```hello-path-go``` code mockup a web service with a third-party credential loop validation. If the flag value of ```my-secret``` is:   

* different than 4321 then it fails and retry after 10 secondes.  
* 4321 then it "validates" the credentials and start the webservice.  

Here is the code: 

```Golang
--8<-- "sources/hello-path-go/main.go"
```


## restart

### example

## reload

### example

## redeploy

### example


