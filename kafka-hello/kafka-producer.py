from kafka import KafkaProducer

bootstrap_servers = ['localhost:9092'] 

producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers
)

producer.send('hello-kafka', b'hello 1000')

producer.flush()