from .views import IndexView, SearchView

urlpatterns = {
    '/': IndexView.as_view('index'),
    '/search/': SearchView.as_view('search'),
}
