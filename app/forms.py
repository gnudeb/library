from wtforms import Form, StringField, validators


class BookSearchForm(Form):
    query = StringField('query', [validators.Length(min=3, max=64)])
    email = StringField('email', [validators.email(message="Invalid email")])
