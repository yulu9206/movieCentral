from django.urls import path, include

from django.contrib import admin

from django.conf.urls import url

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    # path('/', hello.views.index, name='index'),
    path('movies/', hello.views.movies),
    path('customers/', hello.views.customers),
    path('login/', hello.views.getlogin),
    path('post-login/', hello.views.login),
    path('logout/', hello.views.logout),
    path('register/', hello.views.register),
    path('customer-detail/', hello.views.customerDetail),
    path('movie-detail/', hello.views.movieDetail),
    path('reports/', hello.views.reports),
    # path('reports/', hello.views.reports),
]
