## Inroduction
This UI repo starts from a barebones Django app, which can easily be deployed to Heroku.
Deployed at:https://sleepy-shore-81319.herokuapp.com/

## Running Locally

Make sure you have Python 3.7 [installed locally](http://install.python-guide.org). 

```sh
$ git clone https://github.com/yulu9206/movieCentralUI.git
$ cd python-getting-started

$ source mc-env/bin/activate
or
$ pip install -r requirements.txt

$ python manage.py runserver
```
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
