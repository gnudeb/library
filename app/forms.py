from wtforms import Form, StringField, validators


class BookSearchForm(Form):
    query = StringField('Search query', [validators.Length(min=3, max=64)])
    email = StringField('Email', [validators.email(message="Invalid email")])
