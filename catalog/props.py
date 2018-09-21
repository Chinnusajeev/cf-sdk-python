""" Make changes to this file.
"""

props = {}

# Replace this with the custom url generated for you.
props['api_gateway_url'] = 'http://localhost:9080/'

# Replace 'your_api_key' with your API key.
props['X-Api-Key'] = 'cognitive_fAshIon_developer'

# To prevent the service from accessing your data for further API improvements,
# set the X-Data-Collection-Opt-Out header parameter to true.
props['X-Data-Collection-Opt-Out'] = 'false'

# You need to give a name to your catalog.
props['catalog_name'] = 'sample_catalog'

# The sample scripts read the json files from this folder.
props['catalog_folder'] = '/cognitive_fashion/code/cf/sample_catalog'

