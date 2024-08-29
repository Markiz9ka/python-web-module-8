import pika
from models import Contact

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='email_queue')

def send_email(contact_id):
    contact = Contact.objects(id=contact_id).first()
    if contact and not contact.message_sent:
        print(f"send email to {contact.email} ({contact.fullname})")
        contact.message_sent = True
        contact.save()

def callback(ch, method, properties, body):
    contact_id = body.decode()
    send_email(contact_id)

channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)

print('Waiting for messages. Press Ctrl+C to end.')
channel.start_consuming()
