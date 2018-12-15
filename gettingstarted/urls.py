from django.urls import path, include

from django.contrib import admin

from django.conf.urls import url

admin.autodiscover()

import hello.views


urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^customer/delete/(?P<userId>\d+)$', hello.views.deleteCustomer),
    url(r'^movie-review/(?P<reviewId>\d+)$', hello.views.deleteReview),
    url(r'^edit-review/(?P<reviewId>\d+)$', hello.views.postEditReview),
    url(r'^customer/detail/(?P<userId>\d+)$', hello.views.customerDetail),
    url(r'^customer/edit/(?P<userId>\d+)$', hello.views.editCustomer),
    path('profile/', hello.views.profile),
    path('movies/', hello.views.movies),
    path('customers/', hello.views.customers),
    path('login/', hello.views.getlogin),
    path('post-login/', hello.views.login),
    path('logout/', hello.views.logout),
    path('register/', hello.views.register),
    path('customer-detail/', hello.views.customerDetail),
    path('addmovie/', hello.views.addMovie),
    path('sub/', hello.views.sub),
    url('movie-detail/(?P<movieId>\d+)$', hello.views.movieDetail),
    url('movie-detail/(?P<movieId>\d+)/(?P<reviewId>\d+)$', hello.views.editReview),
    url('post-review/(?P<movieId>\d+)$', hello.views.postReview),
    path('reports/', hello.views.reports),
    url(r'^activate/(?P<uid>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})$',
        hello.views.activate, name='activate'),
    url(r'^history/(?P<userId>\d+)$', hello.views.customerHistory),
    path('topten/', hello.views.topten),
    path('financial/', hello.views.financial),
    url('edit/(?P<movieId>\d+)$', hello.views.edit),
    path('edit/', hello.views.edit),
    path('toptenwatching/', hello.views.toptenwatching),
    url('delete/(?P<movieId>\d+)$', hello.views.delete),
]
