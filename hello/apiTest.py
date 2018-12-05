import requests
import json

mc_url = 'http://ec2-18-219-67-50.us-east-2.compute.amazonaws.com:8080/dos/api'

json_headers = dict()
json_headers['Content-Type'] = 'application/json;charset=UTF-8'


def getCustomers():
	url = mc_url + '/user'
	res = requests.get(url)
	customers = {}
	if res.status_code == 200:
		res_body = json.loads(res.content.decode('utf-8')) 
		customers = res_body
	else:
		customers = {'key': 'value'}
	print (customers)
	return 

def register(data):
	# print (data)
	try:
		req_body = {
			"email": data.email,
			"firstName": data.firstName,
			"lastName": data.lastName,
			"password": data.password,
			"username": data.username
		}
	except:
		req_body = {
			"email": "yulu9206@gmail.com",
			"firstName": "defaultFirstName",
			"lastName": "defaultLastName",
			"password": "defaultPassword",
			"username": "defaultUsername"
		}
	url = mc_url + '/user'
	req_body = json.dumps(req_body)
	res = requests.post(url, data=req_body, headers=json_headers)
	res_body = json.loads(res.content.decode('utf-8'))
	print (res_body)
	return

def login(data):
	url = mc_url + '/user'
	req_body = json.dumps(req_body)
	res = requests.post(url, data=req_body, headers=json_headers)
	if res.status_code == 200:
		messages.success(request, 'success')
		res_body = json.loads(res.content.decode('utf-8')) 
		request.session['userId'] = res_body['user']['userId'] 
		return redirect('/') 
	else:
		messages.error(request, 'error')
		return redirect('/login')

def addMovie(req_body):
    # req_body = {
    #     "country": request.POST.get('country', 'defaultCountry'),
    #     "coverImageUrl": request.POST.get('coverImageUrl', 'defaultUrl'),
    #     "length": request.POST.get('length', 'defaultLength'),
    #     "movieDesc": request.POST.get('movieDesc', 'defaultDesc'),
    #     "movieTitle": request.POST.get('movieTitle', 'defaultTitle'),
    #     "movie_type": request.POST.get('movie_type', 1),
    #     "mpaaId": request.POST.get('movieDesc', 1),
    #     "releaseDate": request.POST.get('releaseDate', '2018-12-05'),
    #     "studio": request.POST.get('studio', 'defaultStudio'),
    #     "trailerUrl": request.POST.get('trailerUrl', 'defaultUrl'), 
    # }
    url = mc_url + '/movie'
    req_body = json.dumps(req_body)
    res = requests.post(url, data=req_body, headers=json_headers)
    res_body = json.loads(res.content.decode('utf-8'))
    if res.status_code == 201:
        print('The Movie is created!')
    else:
        print('error')
    return 

# getCustomers()
# registerData = {
#   "email": "test@email",
#   "firstName": "testF",
#   "lastName": "testL",
#   "password": "testP",
#   "username": "testU"
# }
# register(registerData)

# loginData = {
#   "password": "1111",
#   "username": "testu7"
# }

# login(loginData)

newMovie = {
  "country": "string",
  "coverImageUrl": "string",
  "length": 0,
  "movieDesc": "string",
  "movieTitle": "string",
  "movie_type": 1,
  "mpaaId": 1,
  "releaseDate": "2018-12-05",
  "studio": "string",
  "trailerUrl": "string"
}

addMovie(newMovie)