from mongoengine import Document, StringField, ReferenceField, ListField, BooleanField, connect

connect(host='mongodb+srv://markelloff777:lFuT06h24CTd6dEz@cluster0.jv53z.mongodb.net/')

class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()

class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author, required=True)
    quote = StringField()

class Contact(Document):
    fullname = StringField(required=True)
    email = StringField(required=True)
    message_sent = BooleanField(default=False)
