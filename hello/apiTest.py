import requests
import json

mc_url = 'http://ec2-18-219-67-50.us-east-2.compute.amazonaws.com:8080/dos/api'

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

getCustomers()