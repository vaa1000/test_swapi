import requests


class CustomRequest:
    @staticmethod
    def custom_request(method: str, url: str, **kwargs):
        return requests.request(method, url, **kwargs)