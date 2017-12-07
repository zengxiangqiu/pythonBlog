from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
   url(r'^$',views.indexView.as_view(),name = 'index'),
   url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
   url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.archivesView.as_view(),name = 'archives'),
   url(r'^category/(?P<pk>[0-9]+)/$',views.categoryView.as_view(), name= 'category'),
   url(r'^tag/(?P<pk>[0-9]+)/$',views.tagView.as_view(), name= 'tag'),
   url(r'^about/$',views.aboutView,name = 'about'),
   url(r'^search/$', views.search, name = 'search')
]