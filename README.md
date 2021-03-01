url shortener microservices and monitoring with prometheus and grafana 

#### Prerequisite
* Docker
* Docker-Compose 
* git 

#### Steps

##### Clone source code from git
```
$  git clone https://github.com/veligorer/shortlink-api.git
```

##### Change directory
```
$  cd shortlink-api
```
##### Build and run with docker-compose 

```
$ docker-compose up -d 
```

##### Test application with curl command

```
curl -X GET "http://localhost:8000/shorturl/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"url\":\"https://fastapi.tiangolo.com\"}"
```

the respone should be:
```
{"shorturl":"https://cleanuri.com/8Nk1Bg"}
```

##### Stop docker containers

```
docker-compose down
```

#### Monitoring application with prometheus and grafana

* [Prometheus](http://localhost:9090/) 
* [Grafana](http://localhost:3000/)  




