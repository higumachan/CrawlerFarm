#coding: utf-8

import pika
import json
from traceback import format_exc

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
 
channel.queue_declare(queue='crawler_task_queue')

def callback(ch, method, properties, body):
    print "Received: " ,body
    message = json.loads(body);
    crawler_name = message[0];
    url = message[1];
    try:
        crawler = __import__("crawlers." + crawler_name);
    except:
        print "Can't imported crawler";
        return;
    c = crawler.__getattribute__(crawler_name).__getattribute__(crawler_name)(url);
    try:
        c.run();
    except:
        print "Error On Crawler";
        print format_exc()
        return

channel.basic_consume(callback,
                        queue='crawler_task_queue',
                        no_ack=True)
 
channel.start_consuming()

if __name__ == '__main__':
    pass

