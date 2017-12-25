from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^$', views.book, name='book'),
url(r'^$', views.book_user, name='book_user')
]