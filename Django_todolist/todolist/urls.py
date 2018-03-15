from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'todolist.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.todo_list),
    url(r'^delete/(?P<pk>\d+)/',views.delete),
    url(r'^complete/(?P<id>\d+)/', views.complete),

]