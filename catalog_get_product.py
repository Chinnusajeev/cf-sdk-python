#-----------------------------------------------------------------------------
# Get product from a catalog.  
# GET /v1/catalog/{catalog_name}/products/{id}
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

# catalog name
catalog_name = props['catalog_name']

# product id
id = 'SKLTS16AMCWSH8SH20'

# API end point
api_endpoint = '/v1/catalog/%s/products/%s'%(catalog_name,id)

url = urljoin(api_gateway_url,api_endpoint)

response = requests.get(url,headers=headers)

print response.status_code
pprint(response.json())

# The local copy of the catalog image can be accessed as
image_url = response.json()['data']['images']['1']['image_url']
image_filename = response.json()['data']['images']['1']['image_filename']

print urljoin(api_gateway_url,
              '/v1/catalog/%s/images/%s'%(catalog_name,image_filename))
              