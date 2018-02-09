from flask.views import View, MethodView
from flask.templating import render_template
from .forms import BookSearchForm

class IndexView(View):
    def dispatch_request(self):
        search_form = BookSearchForm()
        return render_template('search.html', search_form=search_form)

class SearchView(MethodView):

    def get(self):
        search_form = BookSearchForm()
        return render_template('search.html', search_form=search_form)
