from django.conf.urls import url
from apps.profile import views

urlpatterns = [
    url(r'^$', views.MainPage.as_view(), name="main"),
    url(r'^profile/(?P<id>[\d-]+)/$', views.profile, name="user_profile"),
]