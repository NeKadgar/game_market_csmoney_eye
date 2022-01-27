import requests


class Client:
    def __init__(self):
        self._session = requests.Session()

    def get(self, url, **kwargs):
        return self._session.get(url, **kwargs)
