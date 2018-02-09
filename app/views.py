from flask.views import View
from flask.templating import render_template


class IndexView(View):
    def dispatch_request(self):
        return render_template('index.html')
