#coding: utf-8

import pika
import json
from traceback import format_exc
import logging
import os
from logging.handlers import *

formatter = logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
)

logger = logging.getLogger("crawlerd");
error_log = "logs/error.log";
error_file_handler = RotatingFileHandler(
    error_log, maxBytes=100000, backupCount=10
)    
error_file_handler.setLevel(logging.ERROR)
error_file_handler.setFormatter(formatter)
logger.addHandler(error_file_handler);

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
        logger.error( "Can't imported crawler");
        return;
    c = crawler.__getattribute__(crawler_name).__getattribute__(crawler_name)(url);
    try:
        c.run(*message[2:]);
    except:
        logger.error("Error On %s" % message[0]);
        logger.error(format_exc());
        return

channel.basic_consume(callback,
                        queue='crawler_task_queue',
                        no_ack=True)
 
channel.start_consuming()

if __name__ == '__main__':
    pass

