# reload, restart or redeploy

## context
Containerized application deployed on Kubernetes, manually or via GitOps, is composed of multiple objects from namespace, deployment, configmaps, secrets, services, and more. Most are static while other will be updated during the application lifecycle.   

Most of these object defintions are static while others will be updated with no to significant impact on the application, e.g.:   

* changing a service impacts the access but not the application.
* changing a data backend secret impacts the application with crashing, providing corrupted and/or outdated response.  
* changing a namespace or a deployment will require a redeployment of the application, meaning full disruption. 

How can we address these use cases?

## the application

The ```hello-path-go``` code mockup a web service with a third-party credential loop validation. If the flag value of ```my-secret``` is:   

* different than 4321 then it fails and retry after 10 secondes.  
* 4321 then it "validates" the credentials and start the webservice.  

### the code 

The sources are available [here](https://github.com/beezy-dev/verbose-couscous/tree/main/docs/sources/hello-path-go).
```Golang
--8<-- "sources/hello-path-go/main.go"
```

Output of the code with no parameters results in an incorrect ```mysecret``` value: 
```
romdalf@minime ~/dev/opensource/beezy-dev/verbose-couscous (main) $ go run docs/sources/hello-path-go/main.go                             
[hello-path-go-main] 2024/04/18 11:16:44 ------------------------------------------------------------
[hello-path-go-main] 2024/04/18 11:16:44 hello-path-go - a simple web service returning the URL path.
[hello-path-go-main] 2024/04/18 11:16:44 ------------------------------------------------------------
[hello-path-go-main] 2024/04/18 11:16:44 Web service initialization...
[hello-path-go-main] 2024/04/18 11:16:44 Note: mysecret value is 1234 while expected value is 4321.
[hello-path-go-main] 2024/04/18 11:16:44 FATAL: connection to remote service failed. Check mysecret parameter.
exit status 1
```

Output of the code with the correct value set for ```my-secret``` results in a working web service **with a security exposure**: 
```
romdalf@minime ~/dev/opensource/beezy-dev/verbose-couscous (main*) $ go run docs/sources/hello-path-go/main.go --mysecret 4321
[hello-path-go-main] 2024/04/18 11:17:59 ------------------------------------------------------------
[hello-path-go-main] 2024/04/18 11:17:59 hello-path-go - a simple web service returning the URL path.
[hello-path-go-main] 2024/04/18 11:17:59 ------------------------------------------------------------
[hello-path-go-main] 2024/04/18 11:17:59 Web service initialization...
[hello-path-go-main] 2024/04/18 11:17:59 Connection to remote service: ok.
[hello-path-go-main] 2024/04/18 11:17:59 Web service accessible at 0.0.0.0:8080
``` 

### the build

The initial image has been built using ```podman``` with the following ```Containerfile```:
```INI
--8<-- "sources/hello-path-go/Containerfile"
```

The image is hosted here ```https://github.com/beezy-dev/verbose-couscous/pkgs/container/hello-path-go```
The image tag is ```ghcr.io/beezy-dev/hello-path-go:v0.1``` for any deployment type.

### the deployment




## reload, restart, redeploy 

### redeploy

### restart

### reload



