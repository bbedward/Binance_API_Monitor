import requests

class API:

	URL = "https://www.binance.com/api/v1"

	def get_info(self):
        	path = "%s/exchangeInfo" % self.URL
	        return requests.get(path, timeout=30, verify=True).json()
