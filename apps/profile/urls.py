from django.conf.urls import url
from apps.profile import views

urlpatterns = [
    url(r'^$', views.landing, name="main"),
]