#------------------------------------------------------------------------------
# Get all catalog names. 
# GET /v1/catalog_names
#------------------------------------------------------------------------------

import os
import json
import requests
from urlparse import urljoin
from pprint import pprint

from props import *

# Replace this with the custom url generated for you.
api_gateway_url = props['api_gateway_url']

# Pass the api key into the header
# Replace 'your_api_key' with your API key.
headers = {'X-Api-Key': props['X-Api-Key']}

# API end point.
api_endpoint = '/v1/catalog_names'

url = urljoin(api_gateway_url,api_endpoint)

response = requests.get(url,headers=headers)

print response.status_code
pprint(response.json())

