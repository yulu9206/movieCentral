# Python: Getting Started


## Running Locally

Make sure you have Python 3.7 [installed locally](http://install.python-guide.org). 

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


## URL Documentation
### Customer & Admin
    /login/, login and registration page
    /logout/, logout
    /profile/, view account detail
    /customer/edit/userId, update customerprofile
    
    /movies/, view all movies
    /movie-detail/movieId, view movieDetail and review
    /movie-detail/movieId/reviewId, edit movie review
    
    /toptenwatching/, views top ten watched movies
    /toptenrating/, views top ten rated movies   
    
    /sub/, subscription page
    
  ### Admin Only
    /reports/, view movie watching history
    /financial/, view financial report
    
    /customers/, view all customers info
    /customer/detail/userId, view customerDetail
    /topten/, views top ten active users
    /history/userId, customer watching history
    
    /delete/movieId, delete movie
    /edit/, movie management page 
    /edit/movieId, edit movie
