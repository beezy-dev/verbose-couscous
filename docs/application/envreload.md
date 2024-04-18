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

### the code: 

```Golang
--8<-- "sources/hello-path-go/main.go"
```

Output of the code with an incorrect ```my-secret``` value:
```
romdalf@minime ~/dev/opensource/beezy-dev/verbose-couscous (main*) $ go run docs/sources/hello-path-go/main.go --my-secret 1234
[GO] 2024/04/17 20:37:55 Creating a hello path web service with logger
[GO] 2024/04/17 20:37:55 Connection to remote service: nok. Check my-secret parameter.
[GO] 2024/04/17 20:37:55 Note: my-secret value is 1234 while expecting 4321
```

Output of the code with a correct ```my-secret``` value: 
```
romdalf@minime ~/dev/opensource/beezy-dev/verbose-couscous (main*) $ go run docs/sources/hello-path-go/main.go --my-secret 4321
[GO] 2024/04/17 20:38:17 Creating a hello path web service with logger
[GO] 2024/04/17 20:38:17 Connection to remote service: ok
[GO] 2024/04/17 20:38:17 Web service accessible at 0.0.0.0:8080
``` 

### the deployment

The initial image has been built based on the above code which is also available [here](https://github.com/beezy-dev/verbose-couscous/tree/main/docs/sources/hello-path-go). 

## reload, restart, redeploy 

### redeploy

### restart

### reload



