# Python: Getting Started


## Running Locally

Make sure you have Python 3.7 [installed locally](http://install.python-guide.org). To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), as well as [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone https://github.com/heroku/python-getting-started.git
$ cd python-getting-started

$ python3 -m venv getting-started
$ pip install -r requirements.txt

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## URL Documentation
    /customer/delete/userId, deleteCustomer 
    /movie-review/reviewId, deleteReview
    /customer/detail/userId, view customerDetail
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
    path('toptenrating/', hello.views.topTenRating),
