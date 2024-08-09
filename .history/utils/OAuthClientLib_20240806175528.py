# utils/OAuthClientLib.py

import requests
import json

class OAuthClient:
    def __init__(self, client_id, client_secret, token_url, refresh_url, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_url = token_url
        self.refresh_url = refresh_url
        self.redirect_uri = redirect_uri
        self.access_token = None
        self.refresh_token = None

    def get_token(self, authorization_code):
        payload = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'authorization_code',
            'code': authorization_code,
            'redirect_uri': self.redirect_uri
        }
        response = requests.post(self.token_url, data=payload)
        if response.status_code == 200:
            tokens = response.json()
            self.access_token = tokens['access_token']
            self.refresh_token = tokens['refresh_token']
            return tokens
        else:
            response.raise_for_status()

    def refresh_token(self):
        payload = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'refresh_token',
            'refresh_token': self.refresh_token
        }
        response = requests.post(self.refresh_url, data=payload)
        if response.status_code == 200:
            tokens = response.json()
            self.access_token = tokens['access_token']
            self.refresh_token = tokens['refresh_token']
            return tokens
        else:
            response.raise_for_status()

    def make_authenticated_request(self, url, method='GET', headers=None, data=None):
        if headers is None:
            headers = {}
        headers['Authorization'] = f'Bearer {self.access_token}'
        if method.upper() == 'GET':
            response = requests.get(url, headers=headers)
        elif method.upper() == 'POST':
            response = requests.post(url, headers=headers, data=data)
        else:
            raise ValueError('Unsupported HTTP method')
        return response.json()
