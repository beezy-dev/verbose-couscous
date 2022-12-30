
# Keep your Secrets secret!

## Security Overview
The journey to secure a container platform could be overwheelming. Building a layer based or mindmap diagram can help to define the different components requiring attention. Here is an example of such mindmap, work in progress and not a definite/static diagram:

![](../images/mermaid-diagram-2022-12-28-131205.svg)

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

The etcd key value store is the most critical piece of a Kubernetes cluster as it servers as a sort of distributed CMDB for every components; from nodes, to configmap, to services, ... If etcd fails, the entire cluster will collapse, if it is hacked, the entire workloads and components are compromised. The key value store does not provide any encryption capabilities. 

Then secret. As everything else, secrets are stored within the cluster etcd. Secret payloads are not encrypted but encoded in base64. This is by default a mechanism to protect the data field payload going through software that might chok on special characters.  

Considering the above, the attach surface is similar to an open door policy. Let's digg into the Kubernetes Secret Management and then see how to mitigate from an end-to-end perspective this unwanted ```open door policy```.

## Create a Kubernetes Secret

### from Ops view
Let's consider that an application needs to connect to an endpoint requesting basic credentials, respectively ```admin``` and ```p@ssw0rd$```. As defined earlier, these value needs to be encoded in based64 to avoid being truncated. This can be done with:

```bash title="credential base64 encoding"
echo 'admin' | base64
echo 'p@ssw0rd$' | base64
```

Then the encoded credentials can be used within an YAML manifest like:  

!!! warning inline end  
    While convenient from a GitOps perspective, the YAML manifest is optional as secrets can be create using the ```kubectl create secret``` command.  
    However, the manifest is **unsafe**; the data field values can be then decoded on any system giving back the original values.

``` title="mysecret.yml"
--8<-- "files/mysecret.yml"
```

Finally, to actually create the secret within the Kubernetes cluster, run the following:

```bash title="create a secret based on a YAML manifest" 
kubectl apply -f mysecret.yml
```

### from an architecture view
While the above is trivial as they are commons to any Kubernetes API objects CURD operations, let's have a sequence diagram to understand the components in action: 

!!! info inline end  
    For this diagram, the data field flows through a series of component, usually TLS encupsulated. However, the origin and end points are considered unsafe during since there is any data encryption.
 
```mermaid
sequenceDiagram
participant User or App
participant etcd
participant API Server
autonumber
  User or App->>API Server: create Secret mysecret
  Note right of User or App: base64 encoded data field
  API Server->>etcd: store Secret
```

## Iterative Mitigation Path 

Let's zoom in on the mindmap focusing on Kubernetes CRUD operations to elaborate an iterative mitigation path.

![](../images/mermaid-diagram-2022-12-29-104705.svg)

<!-- 
This is the mermaid.js manifest for the mindmap diagram
 ```mermaid
mindmap
  id)kubernetes secrets(
    etcd
      Auth
      File System
      Patching Life Cycle
      Pod Access
      TLS  
    API
      Auth
      Config Hardening
      Patch Life Cycle
      RBAC
      TLS
    CLI or Manifest
      Data Field
      GitOps
``` -->

### etcd
By design, etcd provides a TLS for transport and authentication but no [encryption capabilities](https://etcd.io/docs/v3.5/op-guide/security/#does-etcd-encrypt-data-stored-on-disk-drives). The project's mitigations offered are:  
 
- Let client applications encrypt and decrypt the data
- Use a feature of underlying storage systems for encrypting stored data like [dm-crypt](https://en.wikipedia.org/wiki/Dm-crypt)

In other words, these two options refer to:

- from a Kubernetes perspective, clients are the CLI toolings via the API server;
  - tools like ```kubectl``` or others would have encryption capabilities to secure the data field.  
    However, within the context of Kubernetes and its workload, it would require both the API server and the applications to somehow know that the data field is encrypted and how to decrypt for CRUD operations.   
  - the Kubernetes API server has an encryption at rest configuration API object  ```EncryptionConfiguration``` to configure [encryption providers](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/). This approach streamlines the process as every CRUD operations depends on the API server which will handle the encryption/decryption requests.  

!!! warning
    While the CLI tooling approach might address the unsecure manifest and ease GitOps practice, it would be a rather significant implementation. Reducing the implementation complexity by using the existing ```EncryptionConfiguration``` would ease the consumption of secrets but leave the Ops with an unsecure manifest.

- from a deployment perspective, etcd will consume available storage from the master node(s), storage that could be encrypted using different options, one being dm-crypt.  
  
!!! warning  
    Encrypting the data at the disk/file system level will protect any CRUD operations on the etcd content being written on disk. However, this does not protect against unauthorized etcd client access. 

### Manifest

### API

The address the relative high concern, the [Kubernetes Project](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/) advises to leverage the ```EncryptionConfiguration``` API objects to perform encryption at rest for Secrets at creation time. 

