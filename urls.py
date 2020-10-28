from django.conf.urls import url

from . import views

app_name = 'modules_installation'

urlpatterns = [
    url(r'^$', views.ModuleInfoView.as_view(), name='info'),
]
