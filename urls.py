from django.conf.urls import url

from . import views

app_name = 'modules_installation'

urlpatterns = [
    url(r'^$', views.ModuleInfoView.as_view(), name='info'),
    url(r'^dashboard/subitem/$', views.ModuleMenuSubItemView.as_view(), name='dashboard-subitem'),
    url(r'^users/subitem/$', views.ModuleMenuSubItemView.as_view(), name='users-subitem'),
    url(r'^create/test/', views.ModuleMenuSubItemView.as_view(), name='create-test'),
]
