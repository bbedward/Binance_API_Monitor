import requests

try:
	from urllib import urlencode
except ImportError:
	from urllib.parse import urlencode

class API:

	URL = "https://www.binance.com/api/v1"

	def get_info(self):
        	path = "%s/exchangeInfo" % self.URL
	        return requests.get(path, timeout=30, verify=True).json()
