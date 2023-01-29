# Environment Setup
1. Zeus
2. [k3s with `Docker` as the container runtime](https://docs.k3s.io/advanced#using-docker-as-the-container-runtime)
```shell
curl -sfL https://get.k3s.io | sh -s - --docker
```
3. [Kubeflow](https://github.com/kubeflow/manifests#installation)
4. FastAPI
```shell
pip install "fastapi[all]"
```
