from flask import request, redirect
from flask.views import View, MethodView
from flask.templating import render_template
from .forms import BookSearchForm


class IndexView(View):

    def dispatch_request(self):
        return redirect('/search/')


class SearchView(MethodView):

    def get(self, search_form=None):
        search_form = search_form or BookSearchForm()
        return render_template('search.html', search_form=search_form)

    def post(self):
        search_form = BookSearchForm(request.form)
        if search_form.validate():
            #TODO: Dispatch search
            return "Searching for {}, results will be sent at {}".format(
                search_form.query.data,
                search_form.email.data)
        else:
            return self.get(search_form)
