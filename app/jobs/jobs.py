from flask_mail import Message
import lxml.etree
from ..app import mail_instance, db_instance

def search_books_then_reply(query, email):
    print("{} {}".format(query, email))
    message = Message(query, [email])
    mail_instance.send(message)


def parse_book(file):
    tree = lxml.etree.parse(file)
    root = tree.getroot()
    body = root.find('{*}body')

    sections = parse(body)

    db_instance.books.insert_one(sections)


def parse(element):
    d = {}
    title = element.find('{*}title').find('{*}p').text
    d[title] = []

    for paragraph in element.iterfind('{*}p'):
        d[title].append(paragraph.text)

    for section in element.iterfind('{*}section'):
        d[title].append(parse(section))

    return d

