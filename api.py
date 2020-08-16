import requests
import json
from keys import API_KEY

# zipCode = "10001"
#
# url = "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={}&distance=50&API_KEY={}".format(zipCode, API_KEY)
#
# api_request = requests.get(url)
# data = json.loads(api_request.content)
# city = data[0]['ReportingArea']
# quality = data[0]['AQI']
# category = data[0]['Category']['Name']
#
# print(city, quality, category)
# print(data)


# coding: utf-8
import requests


params = {
    'access_key': 'b473c6937a0660adf948dce436521ef8',
    'query': 'New York'
}

api_result = requests.get('http://api.weatherstack.com/current', params)

api_response = json.loads(api_result.content)
print(api_response)

print(u'Current temperature in %s is %d℃' % (api_response['location']['name'], api_response['current']['temperature']))
print(api_response['current']['weather_descriptions'][0])