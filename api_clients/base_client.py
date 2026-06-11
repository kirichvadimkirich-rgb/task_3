
import requests
from config.settings import BASE_URL

class BaseClient:
    def __init__(self):
        self.base_url = BASE_URL

    def _send_request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        return requests.request(method, url, **kwargs)

    def _post(self, endpoint, json=None, headers=None):
        return self._send_request("POST", endpoint, json=json, headers=headers)

    def _delete(self, endpoint, headers=None):
        return self._send_request("DELETE", endpoint, headers=headers)
    
    def _get(self, endpoint, params=None, headers=None):
        return self._send_request("GET", endpoint, params=params, headers=headers)