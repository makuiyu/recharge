
# 系统结构
recharge/
├── frontend/
│   ├── index.html
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── app.js
│   ├── Dockerfile
├── user/
│   ├── app.py
│   ├── routes.py
│   ├── models.py
│   ├── config.py
│   ├── requirements.txt
│   └── Dockerfile
├── order/
│   ├── app.py
│   ├── routes.py
│   ├── models.py
│   ├── config.py
│   ├── requirements.txt
│   └── Dockerfile
├── inventory/
│   ├── app.py
│   ├── routes.py
│   ├── models.py
│   ├── config.py
│   ├── requirements.txt
│   └── Dockerfile
├── payment/
│   ├── app.py
│   ├── routes.py
│   ├── models.py
│   ├── config.py
│   ├── requirements.txt
│   └── Dockerfile
├── gateway/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
└── deployment/
    ├── mysql_deployment.yaml
    ├── user_deployment.yaml
    ├── order_deployment.yaml
    ├── inventory_deployment.yaml
    ├── payment_deployment.yaml
    ├── gateway_deployment.yaml
    └── frontend_deployment.yaml


# 安装依赖
pip freeze > requirements.txt
pip install -r requirements.txt -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple


# 系统部署

## 拉取依赖镜像
docker pull python:3.9-slim
docker pull nginx:alpine
docker pull mysql:5.7


## 使用Docker构建各个服务镜像
docker build -t makuiyu/user-service:latest user/
docker build -t makuiyu/order-service:latest order/
docker build -t makuiyu/inventory-service:latest inventory/
docker build -t makuiyu/payment-service:latest payment/
docker build -t makuiyu/gateway-service:latest gateway/
docker build -t makuiyu/frontend-web:latest frontend/


## 在Kubernetes上部署每个服务
kubectl apply -f deployment/mysql_deployment.yaml
kubectl apply -f deployment/user_deployment.yaml
kubectl apply -f deployment/order_deployment.yaml
kubectl apply -f deployment/inventory_deployment.yaml
kubectl apply -f deployment/payment_deployment.yaml
kubectl apply -f deployment/gateway_deployment.yaml
kubectl apply -f deployment/frontend_deployment.yaml

kubectl apply -f deployment/


## 检查所有服务是否成功启动
kubectl get pods
kubectl get services
kubectl logs <pod_name>
kubectl logs -f <pod_name>
kubectl logs -f -l app=<app_name>


## 清理环境
kubectl delete -f deployment/mysql_deployment.yaml
kubectl delete -f deployment/user_deployment.yaml
kubectl delete -f deployment/order_deployment.yaml
kubectl delete -f deployment/inventory_deployment.yaml
kubectl delete -f deployment/payment_deployment.yaml
kubectl delete -f deployment/gateway_deployment.yaml
kubectl delete -f deployment/frontend_deployment.yaml

kubectl delete -f deployment/


## 删除镜像
docker rmi makuiyu/user-service:latest
docker rmi makuiyu/order-service:latest
docker rmi makuiyu/inventory-service:latest
docker rmi makuiyu/payment-service:latest
docker rmi makuiyu/gateway-service:latest
docker rmi makuiyu/frontend-web:latest


# 逐个模块

## frontend
kubectl delete -f deployment/frontend_deployment.yaml
sleep 3
docker rmi makuiyu/frontend-web:latest
docker build -t makuiyu/frontend-web:latest frontend/
kubectl apply -f deployment/frontend_deployment.yaml
sleep 3
kubectl get services
kubectl get pods

## gateway
kubectl delete -f deployment/gateway_deployment.yaml
sleep 3
docker rmi makuiyu/gateway-service:latest
docker build -t makuiyu/gateway-service:latest gateway/
kubectl apply -f deployment/gateway_deployment.yaml
sleep 3
kubectl get services
kubectl get pods
