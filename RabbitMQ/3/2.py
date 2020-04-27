import pika
import time

def callback(ch, method, properties, body):
    print('[x] received %r' % body)
    time.sleep(body.count(b'.'))
    print('[x] done')
    ch.basic_ack(delivery_tag = method.delivery_tag)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange = 'logs', exchange_type = 'fanout')

result = channel.queue_declare(queue = '', exclusive = True)
queue_name = result.method.queue

channel.queue_bind(exchange = 'logs',
                   queue = queue_name)

channel.basic_consume(queue = queue_name,
                      on_message_callback = callback)

channel.start_consuming()