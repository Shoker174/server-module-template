from django.conf.urls import url

from . import views

app_name = 'test_module'

urlpatterns = [
    url(r'^$', views.ModuleInfoView.as_view(), name='info'),
    url(r'^create/test/', views.ModuleMenuSubItemView.as_view(), name='create-test'),
]
