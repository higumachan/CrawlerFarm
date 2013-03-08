
import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
 
channel.queue_declare(queue='crawler_task_queue')

def send(crawler_name, url):
    channel.basic_publish(exchange='',
            routing_key='crawler_task_queue',
            body=json.dumps((crawler_name, url)))

if __name__ == '__main__':
    send("SampleCrawler", "http://google.com");
    send("TestCrawler", "http://google.com");

