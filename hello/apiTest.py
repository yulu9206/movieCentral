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
# getCustomers()
# registerData = {
#   "email": "test@email",
#   "firstName": "testF",
#   "lastName": "testL",
#   "password": "testP",
#   "username": "testU"
# }
# register(registerData)

loginData = {
  "password": "1111",
  "username": "testu7"
}

login(loginData)