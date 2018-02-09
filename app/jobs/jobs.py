from flask_mail import Message
from ..app import mail_instance

def search_books_then_reply(query, email):
    print("{} {}".format(query, email))
    message = Message(query, [email])
    mail_instance.send(message)
