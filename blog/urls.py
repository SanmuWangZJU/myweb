from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index),#要把url分配到相应的方法中去
    url(r'^article/(?P<article_id>\d+)$', views.article_page,name='article_page'),
    url(r'^edit/(?P<article_id>\d+)$',views.edit_page,name='edit_page'),
    url(r'^edit/action/$',views.edit_action,name='edit_action'),
]