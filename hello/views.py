import os
import json
import requests
import logging, logging.config
import sys

from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage

from .models import Greeting, TempUser

api_key = 'Z1P14W088UZ4E700'
mc_url = 'http://ec2-18-219-67-50.us-east-2.compute.amazonaws.com:8080/dos/api'
json_headers = dict()
json_headers['Content-Type'] = 'application/json;charset=UTF-8'

# messages.debug(request, '%s SQL statements were executed.' % count)
# messages.info(request, 'Three credits remain in your account.')
# messages.success(request, 'Profile details updated.')
# messages.warning(request, 'Your account expires in three days.')
# messages.error(request, 'Document deleted.')

def register(request):
	if request.method == 'POST':
		data = {
			"email": request.POST.get("email", "yulu9206@gmail.com"),
			"firstName": request.POST.get("firstName", "defaultFirstName"),
			"lastName": request.POST.get("lastName", "defaultLastName"),
			"password": request.POST.get("password", "defaultPassword"),
			"username": request.POST.get("username", "defaultUsername"),
			"role": request.POST.get("role", 1),
		}
		tempUser = TempUser(email=data['email'], firstName=data['firstName'], lastName=data['lastName'], password=data['password'], username=data['username'], role=data['role'])
		tempUser.save()
		current_site = get_current_site(request)
		mail_subject = 'Activate your movieCentral account.'
		message = render_to_string('acc_active_email.html', {
			'user': tempUser,
			'domain': current_site.domain,
			'uid':tempUser.pk,
			'token':account_activation_token.make_token(tempUser),
		})
		to_email = request.POST.get('email')
		email = EmailMessage(
					mail_subject, message, to=[to_email]
		)
		email.send()
		return HttpResponse('Please confirm your email address to complete the registration')
	else:
		form = SignupForm()
	return render(request, 'signup.html', {'form': form})

def activate(request, uid, token):
	try:
		uid = uid
		user = TempUser.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.isActivate = True
		user.save()
		req_body = {
			"email": user.email,
			"firstName": user.firstName,
			"lastName": user.lastName,
			"password": user.password,
			"username": user.username,
			"role": user.role
		}
		url = mc_url + '/user'
		req_body = json.dumps(req_body)
		res = requests.post(url, data=req_body, headers=json_headers)
		res_body = json.loads(res.content.decode('utf-8'))
		if res.status_code == 201:
			messages.success(request, 'Thank you for your email confirmation. Now you can log in your account.')
		else:
			messages.error(request, res_body['error'])
	else:
		messages.error(request, 'Activation link is invalid!')
	return redirect('/login')

def index(request):
    try:
        this_user = request.session['user']
        data = {
        'user': this_user
        }
    except:
        data = {}
    return render(request, 'homepage.html', data)

def profile(request):
    try:
        this_user = request.session['user']
        data = {
        'user': this_user
        }
    except:
        data = {}
    return render(request, 'profile.html', data)

def editCustomer(request, userId):
	req_body = {
		"email": request.POST.get("email", "yulu9206@gmail.com"),
		"firstName": request.POST.get("firstName", "defaultFirstName"),
		"lastName": request.POST.get("lastName", "defaultLastName"),
		"password": request.POST.get("password", "defaultPassword"),
		"username": request.POST.get("username", "defaultUsername"),
		"city": request.POST.get("city", "defaultcity"),
		"phone": request.POST.get("phone", "defaultphone"),
		"state": request.POST.get("state", "defaultstate"),
		"street": request.POST.get("street", "defaultstreet"),
		"zipcode": request.POST.get("zipcode", "defaultzipcode")
	}

	url = mc_url + '/user/' + userId
	req_body = json.dumps(req_body)
	res = requests.put(url, data=req_body, headers=json_headers)
	res_body = json.loads(res.content.decode('utf-8'))
	if res.status_code == 200:
		messages.success(request, 'Updated')
		request.session['user'] = res_body['user']
	else:
		messages.error(request, res_body['error'])
	return redirect('/profile')

def getlogin(request):
	return render(request, 'login.html')

def login(request):
	req_body = {
		"password": request.POST.get("password", "defaultPassword"),
		"username": request.POST.get("username", "defaultUsername")
	}
	url = mc_url + '/login'
	req_body = json.dumps(req_body)
	res = requests.post(url, data=req_body, headers=json_headers)
	res_body = json.loads(res.content.decode('utf-8'))
	if res.status_code == 200:
		request.session['user'] = res_body['user']
		return redirect('/')
	else:
		messages.error(request, res_body['error'])
		return redirect('/login')

def logout(request):
	request.session['user'] = None
	return redirect('/')

def customers(request):
	url = mc_url + '/user'
	res = requests.get(url)
	if res.status_code == 200:
		res_body = json.loads(res.content.decode('utf-8'))
		customers = res_body['content']
	else:
		customers = {'defaul': 'default'}
	return render(request, 'customers.html', {'customers': customers})

def deleteCustomer(request, userId):
	url = mc_url + '/user/' + userId
	res = requests.delete(url, headers=json_headers)
	res_body = json.loads(res.content.decode('utf-8'))
	if res.status_code == 200:
		messages.success(request, res_body['user'])
	else:
		messages.error(request, res_body['error'])
	return redirect('/customers')

def customerDetail(request, userId):
	url = mc_url + '/user/' + userId
	res = requests.get(url)
	if res.status_code == 200:
		res_body = json.loads(res.content.decode('utf-8'))
		userDetail = res_body['user']
	else:
		userDetail = {'defaul': 'default'}
		messages.error(request, res_body['error'])
	return render(request, 'customerDetail.html', {'userDetail':userDetail})

def movies(request):
	# get-data
	url1 = mc_url + '/movies'
	url2 = mc_url + '/movie-genre/'
	res1 = requests.get(url1).json()
	data = res1['content']
	for i in range(len(data)):
		res2 = requests.get(url2 + str(data[i]['movieId'])).json()
		temp = res2['genres']
		if len(temp) >= 1:
			data[i]['genre'] = temp[0]['genreName']
		else:
			data[i]['genre'] = ""
	return render(request, 'movies.html', {"data": data})

def movieDetail(request):
	return render(request, 'movieDetail.html')

def reports(request):
	return render(request, 'reports.html')

# def db(request):
# 	greeting = Greeting()
# 	greeting.save()
# 	greetings = Greeting.objects.all()
# 	return render(request, 'db.html', {'greetings': greetings})
