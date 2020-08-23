from django.shortcuts import render

# Create your views here.
def home(request):
	import json
	import requests

	api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=504CB3FD-B442-47D4-A1E0-BC30B0F3CCED")
	api_request_nepal = requests.get("https://nepal-weather-api.herokuapp.com/api/?place=all")

	try:
		api = json.loads(api_request.content)
		api_nepal = json.loads(api_request_nepal.content)

	except Exception as e:
		api = "Error in calling API...."

	return render(request, 'home.html', {'api':api, 'api_nepal':api_nepal})

def about_us(request):
	return render(request, 'about_us.html', {})

# def api_request_for_nepal():
# 	import json
# 	import requests
# 	api_request_nepal = requests.get("https://nepal-weather-api.herokuapp.com/api/?place=all")

# 	try:
# 		api_nepal = json.loads(api_request_nepal.content)

# 	except Exception as e:
# 		api_nepal = "Error in calling API...."

# 	return render(request, 'home.html', {'api_nepal':api_nepal})