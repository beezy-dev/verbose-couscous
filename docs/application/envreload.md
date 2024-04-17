# reload, restart or redeploy

## context
Containerized application deployment, handled manually or via a GitOps practice, is composed of multiple Kubernetes objects like namespace, pods, configmaps, secrets, services, and more. Most of these are static, immutable, and other can be updated during the application lifecycle. 

These object defintion update, manually applied or via a GitOps resync, can have a direct impact on the application behavior while other don't. Examples:
- changing a service or route for a pod will not impact the application but its access from external sources.
- changing a secret to access a data backend will impact the application from functioning up to potential crash, or worst providing outdated outpus when leveraging caching mechanism.  

How can we address this?

## redeploy
This is the easiest path. When ever an object definition is change, a redeployment of the application happens. However this is a slow and delicate process with high dependencies on cross-functional teams to execute the appropriate change management to reduce business disruption. 

In other words, such approach is the **legacy approach** with limited benefits for a cloud-native pattern. 

### example

The code from ```hello-path-go``` will be illustrated on how to handle a secret at the application start, reload, redeploy when there is a change at the object level. 

Here is the code: 

```Golang
--8<-- "sources/hello-path-go/main.go"
```


## restart

### example

## reload

### example






