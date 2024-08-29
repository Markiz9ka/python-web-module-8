import pika
from faker import Faker
from models import Contact

fake = Faker()

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='email_queue')

def generate_contacts(n):
    for _ in range(n):
        contact = Contact(
            fullname=fake.name(),
            email=fake.email()
        )
        contact.save()
        channel.basic_publish(exchange='', routing_key='email_queue', body=str(contact.id))
        print(f"generate contact: {contact.fullname}, {contact.email}")

if __name__ == '__main__':
    generate_contacts(10)
    connection.close()
