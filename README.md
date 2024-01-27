# Simple-Kubernetes-Clustering
## Project Description
In this Distributed Systems course project focusing on Clustering, students will engage in a practical Kubernetes exercise. The task involves setting up a local Kubernetes cluster, preferably using virtual machines like VirtualBox. Students will develop and deploy a web service, which includes a ‘GET /instance-id‘ API, managing at least two service instances/pods. The service should implement round-robin load balancing, with Nginx as the recommended choice. A key challenge is ensuring each service instance uniquely identifies itself upon each API call. This project aims to deepen practical skills in Kubernetes, containerization, and cluster management, bridging theoretical concepts with hands-on experience.Following figure illustrates a high level architecture of the system.


![descripton](https://github.com/amir-rze/Simple-Kubernetes-Clustering/assets/37247427/645811cd-a5c4-4f7c-b595-c0eb8814a20e)

## Requirements
Kubernetes Cluster Creation: Establish a local Kubernetes cluster. Utilize virtual machines (like VirtualBox) to add nodes. Cloud managed services are not to be used. Use Google/Youtube to find out how to create a cluster.

Web Service Development and Deployment: Create, containerize, and deploy a web service with a ‘GET /instance-id‘ API.

Service Instances: Ensure a minimum of two web service instances/pods are operational at all times.

Load Balancing: Implement round-robin load balancing, ideally with Nginx. However, any other load balancer is acceptable.

Unique Instance Identification: Each API call to ‘/instance-id‘ endpoint must return a unique identifier (e.g., unique Pod ID) from the handling instance/pod. The ID should not be hard coded.
