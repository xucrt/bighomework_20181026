"""bighomework_20181026 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from BH_blog.views import get_article,get_index,get_posts,post_post,post_article,put_article, index_login,index_register

# from BH_blog.views import home

urlpatterns = [
    #url(r'^$', home, name='home'),
    url(r'^admin/$', admin.site.urls),
    url(r'^login/$', index_login, name="login"),
    url(r'^register/$', index_register, name="register"),
    url(r'^index/$', get_index, name="index"),

    #url(r'^plate/$', get_posts, name='plate'), #Test
    #url(r'^article/$', get_article, name='article'), #Test

    url(r'^plate/(?P<id>\d+)/$', get_posts, name='plate'),
    url(r'^plate/(?P<id>\d+)/post/$', post_post),
    url(r'^article/(?P<id>\d+)/$', get_article, name='article'),
    url(r'^article/(?P<id>\d+)/comment/$', post_article),
    url(r'^article/(?P<id>\d+)/put/$', put_article),

    # url(r'^article/(?P<id>\d+)/delete/$',delete_article),
    # url(r'^article/(?P<id>\d+)/comment/delete/$',delete_comment),
]
