import os
import json
# import requests

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from .models import Greeting

api_key = 'Z1P14W088UZ4E700'

def index(request):
	return render(request, 'homepage.html')

def login(request):
	return render(request, 'login.html')

def movies(request):
	# get-data
	data = [
    {"movieId": 1, "title": "Fantastic Beasts", "trailerUrl": "https://www.youtube.com/watch?v=TiblmGnet2Q",
    "releaseDate": "2018-11-16", "mpaaRatingId": "PG-13", "Length": "2h13m", "country":"US", "Price":2.99,
    "Studio": "Warner Bros. Pictures", "Synopsis": "asdf", "Type": 4,
	"img":"https://imgc.allpostersimages.com/img/print/u-g-F8TKQV0.jpg?w=900&h=900&p=0"},
    {"movieId": 1, "title": "Fantastic Beasts", "trailerUrl": "https://www.youtube.com/watch?v=TiblmGnet2Q",
    "releaseDate": "2018-11-16", "mpaaRatingId": "PG-13", "Length": "2h13m", "country":"US", "Price":2.99,
    "Studio": "Warner Bros. Pictures", "Synopsis": "asdf", "Type": 4,
	"img":"https://imgc.allpostersimages.com/img/print/u-g-F8TKQV0.jpg?w=900&h=900&p=0"},
    {"movieId": 1, "title": "Fantastic Beasts", "trailerUrl": "https://www.youtube.com/watch?v=TiblmGnet2Q",
    "releaseDate": "2018-11-16", "mpaaRatingId": "PG-13", "Length": "2h13m", "country":"US", "Price":2.99,
    "Studio": "Warner Bros. Pictures", "Synopsis": "asdf", "Type": 4,
	"img":"https://imgc.allpostersimages.com/img/print/u-g-F8TKQV0.jpg?w=900&h=900&p=0"},
	{"movieId": 1, "title": "Fantastic Beasts", "trailerUrl": "https://www.youtube.com/watch?v=TiblmGnet2Q",
    "releaseDate": "2018-11-16", "mpaaRatingId": "PG-13", "Length": "2h13m", "country":"US", "Price":2.99,
    "Studio": "Warner Bros. Pictures", "Synopsis": "asdf", "Type": 4,
	"img":"https://imgc.allpostersimages.com/img/print/u-g-F8TKQV0.jpg?w=900&h=900&p=0"},
	{"movieId": 1, "title": "Fantastic Beasts", "trailerUrl": "https://www.youtube.com/watch?v=TiblmGnet2Q",
    "releaseDate": "2018-11-16", "mpaaRatingId": "PG-13", "Length": "2h13m", "country":"US", "Price":2.99,
    "Studio": "Warner Bros. Pictures", "Synopsis": "asdf", "Type": 4,
	"img":"https://imgc.allpostersimages.com/img/print/u-g-F8TKQV0.jpg?w=900&h=900&p=0"},
	{"movieId": 1, "title": "Fantastic Beasts", "trailerUrl": "https://www.youtube.com/watch?v=TiblmGnet2Q",
    "releaseDate": "2018-11-16", "mpaaRatingId": "PG-13", "Length": "2h13m", "country":"US", "Price":2.99,
    "Studio": "Warner Bros. Pictures", "Synopsis": "asdf", "Type": 4,
	"img":"https://imgc.allpostersimages.com/img/print/u-g-F8TKQV0.jpg?w=900&h=900&p=0"},
	{"movieId": 1, "title": "Fantastic Beasts", "trailerUrl": "https://www.youtube.com/watch?v=TiblmGnet2Q",
    "releaseDate": "2018-11-16", "mpaaRatingId": "PG-13", "Length": "2h13m", "country":"US", "Price":2.99,
    "Studio": "Warner Bros. Pictures", "Synopsis": "asdf", "Type": 4,
	"img":"https://imgc.allpostersimages.com/img/print/u-g-F8TKQV0.jpg?w=900&h=900&p=0"},
	{"movieId": 1, "title": "Fantastic Beasts", "trailerUrl": "https://www.youtube.com/watch?v=TiblmGnet2Q",
    "releaseDate": "2018-11-16", "mpaaRatingId": "PG-13", "Length": "2h13m", "country":"US", "Price":2.99,
    "Studio": "Warner Bros. Pictures", "Synopsis": "asdf", "Type": 4,
	"img":"https://imgc.allpostersimages.com/img/print/u-g-F8TKQV0.jpg?w=900&h=900&p=0"},
	{"movieId": 1, "title": "Fantastic Beasts", "trailerUrl": "https://www.youtube.com/watch?v=TiblmGnet2Q",
    "releaseDate": "2018-11-16", "mpaaRatingId": "PG-13", "Length": "2h13m", "country":"US", "Price":2.99,
    "Studio": "Warner Bros. Pictures", "Synopsis": "asdf", "Type": 4,
	"img":"https://imgc.allpostersimages.com/img/print/u-g-F8TKQV0.jpg?w=900&h=900&p=0"},
	{"movieId": 1, "title": "Fantastic Beasts", "trailerUrl": "https://www.youtube.com/watch?v=TiblmGnet2Q",
    "releaseDate": "2018-11-16", "mpaaRatingId": "PG-13", "Length": "2h13m", "country":"US", "Price":2.99,
    "Studio": "Warner Bros. Pictures", "Synopsis": "asdf", "Type": 4,
	"img":"https://imgc.allpostersimages.com/img/print/u-g-F8TKQV0.jpg?w=900&h=900&p=0"}
  ]
	return render(request, 'movies.html', {'data': data})
	# return render(request, 'movies.html')

def movieDetail(request):
	return render(request, 'movieDetail.html')

def customers(request):
	return render(request, 'customers.html')

def customerDetail(request):
	return render(request, 'customerDetail.html')

def reports(request):
	return render(request, 'reports.html')

# def db(request):
# 	greeting = Greeting()
# 	greeting.save()
# 	greetings = Greeting.objects.all()
# 	return render(request, 'db.html', {'greetings': greetings})

# def hw1Web(request):
# 	results = {
# 		'symbol': '',
# 		'proceeds': 0,
# 		'cost': 0,
# 		'net_profit': 0,
# 		'return_on_invest': 0,
# 		'break_even_price': 0
# 	}
# 	return render(request, 'hw1.html', {'results': results})

# def calculate(request):
# 	postData = {
# 	'symbol': request.POST.get('symbol', "default symbol"),
# 	'allotment': request.POST.get('allotment', "default allotment"),
# 	'final_share': request.POST.get('final_share', "default final_share"),
# 	'sell_commission': request.POST.get('sell_commission', "default sell_commission"),
# 	'initial_share': request.POST.get('initial_share', "default initial_share"),
# 	'buy_commission': request.POST.get('buy_commission', "default buy_commission"),
# 	'tax_rate': request.POST.get('tax_rate', "default tax_rate"),
# 	}
# 	results = profitCalculate(postData)
# 	return render(request, 'hw1.html', {'results': results})

# def profitCalculate(postData):
# 	allotment = float(postData['allotment'])
# 	final_share_price = float(postData['final_share'])
# 	sell_commission = float(postData['sell_commission'])
# 	initial_share_price = float(postData['initial_share'])
# 	buy_commission = float(postData['buy_commission'])
# 	tax_rate = float(postData['tax_rate'])

# 	proceeds = allotment * final_share_price
# 	total_purchase_price = allotment * initial_share_price
# 	capital_gain = (final_share_price - initial_share_price) * allotment - buy_commission - sell_commission
# 	tax = capital_gain * tax_rate / 100
# 	cost = total_purchase_price + buy_commission + sell_commission + tax
# 	net_profit = proceeds - cost
# 	return_on_investment = net_profit / cost * 100
# 	break_even_price = (total_purchase_price + buy_commission + sell_commission) / allotment

# 	results = {
# 	'symbol': postData['symbol'],
# 	'proceeds': proceeds,
# 	'cost': cost,
# 	'net_profit': net_profit,
# 	'return_on_investment': return_on_investment,
# 	'break_even_price': break_even_price
# 	}
# 	return results

# def hw2(request):
# 	results = {
# 		'symbol': '',
# 		'proceeds': 0,
# 		'cost': 0,
# 		'net_profit': 0,
# 		'return_on_invest': 0,
# 		'break_even_price': 0
# 	}
# 	return render(request, 'hw2.html', {'results': results})

# def getFinanceInfo(request):
# 	postData = {
# 		'symbol': request.POST.get('symbol', "default symbol"),
# 		'allotment': request.POST.get('allotment', "default allotment"),
# 		'final_share': request.POST.get('final_share', "default final_share"),
# 		'sell_commission': request.POST.get('sell_commission', "default sell_commission"),
# 		'initial_share': request.POST.get('initial_share', "default initial_share"),
# 		'buy_commission': request.POST.get('buy_commission', "default buy_commission"),
# 		'tax_rate': request.POST.get('tax_rate', "default tax_rate"),
# 	}
# 	results = callFinanceService(postData)
# 	return render(request, 'hw2.html', {'results': results})

# def callFinanceService(postData):
# 	data = requests.get('http://alphavantage.co/query?function=apiKey={}'.format(api_key))
# 	results = data.json()
# 	return results
