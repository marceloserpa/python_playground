# Kafka Hello World with Python


## Setup the environment

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt 
```

## Start Kafka and Zookeeper containers
```
docker-compose up -d
```

## Create the test topic
```
docker-compose exec kafka bash
```
```
kafka-topics --create --topic hello-kafka-2 --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092
```