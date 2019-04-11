import os
import requests

url = os.environ.get('GATEWAY_URL')
name = 'fileapi'

requests.post(
  url = '{url}/services'.format(
    url = url
  ),
  data = {
    'name': name,
    'host': os.environ.get('APP_URL'),
    'port': os.environ.get('APP_PORT')
  }
)

requests.post(
  url = '{url}/services/{name}/routes'.format(
    url = url,
    name = name
  ),
  data = {
    'name': 'all-file-api-routes',
    'paths': [
      '/fileapi'
    ]
  }
)
