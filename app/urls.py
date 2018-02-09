from .views import IndexView

urlpatterns = {
    '/': IndexView.as_view('index'),
}