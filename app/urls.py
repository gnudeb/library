from . import views

urlpatterns = {
    '/': views.IndexView.as_view('index'),
    '/search/': views.SearchView.as_view('search'),
    '/upload/': views.BookUploadView.as_view('upload'),
}
