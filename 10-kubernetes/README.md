## 10. Kubernetes and TensorFlow Serving 

[Study materials](https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/master/10-kubernetes)

[Lesson's code](https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/master/10-kubernetes/code)

[Homework task](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/cohorts/2023/10-kubernetes/homework.md)

---
## Homework solution

In this homework, we'll deploy the credit scoring model from the homework 5. We already have a docker image for this model - we'll use it for deploying the model to `Kubernetes`.

## Prerequisites  

The following need to be installed:  

- Docker

- [kubectl](https://kubernetes.io/docs/tasks/tools/)
(you might already have it - check before installing)  
> The Kubernetes command-line tool, `kubectl`, allows you to run commands against Kubernetes clusters. You can use `kubectl` to deploy applications, inspect and manage cluster resources, and view logs. 
>> [kubectl cheatsheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)

- [kind](https://kind.sigs.k8s.io/docs/user/quick-start/), installation guide:
```bash
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.14.0/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
```
> `kind` lets you run Kubernetes on your local computer. This tool requires that you have either Docker or Podman installed.

## Setup

1. Clone the repository and go to `ML_zoomcamp/10-kubernetes`:
    ```bash
    git clone https://github.com/larin92/ML_zoomcamp.git
    ```

2. Build the Docker image:
   ```bash
   docker build -t zoomcamp-model:hw10 .  
   ```

3. Setup Python environment:
   ```bash
   pipenv install
   ```

## Deployment

1. Create a cluster with `kind`:
   ```bash
   kind create cluster
   ```

   to check that it was successfully created:
   ```bash
   kubectl cluster-info
   ```

2. Load the image into `kind`:
   ```bash 
   kind load docker-image zoomcamp-model:hw10
   ``` 

3. Create a `Kubernetes` deployment based on the deployment manifest file (`deployment.yaml`):
   ```bash
   kubectl apply -f deployment.yaml
   ```

   to check it (get the list of running pods):
   ```bash
   kubectl get deploy
   ```

4. Create the `LoadBalancer` service:
   ```bash
   kubectl apply -f service.yaml
   ```

   to check it (get the list of running services):
   ```bash
   kubectl get service
   ```
  
5. Forward the port:
   ```bash   
   kubectl port-forward service/credit-loadbalancer 9696:80
   ```

## Testing

The `q6_test.py` script sends a request to the model's endpoint and prints the prediction response:
```bash
python q6_test.py
```

----
TBD: Autoscaling
