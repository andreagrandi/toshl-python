import requests
from .exceptions import ToshlException


class ToshlClient(object):
    BASE_API_URL = 'https://api.toshl.com'

    def __init__(self, token):
        self._token = token

    def _make_request(
            self, api_resource, method='GET', params=None, *args, **kwargs):
        """
        Shortcut for a generic request to the Toshl API
        :param url: The URL resource part
        :param method: REST method
        :param parameters: Querystring parameters
        :return: requests.Response
        """
        response = requests.request(
            method=method,
            url='{0}{1}'.format(self.BASE_API_URL, api_resource),
            headers={
                'Authorization': 'Bearer {}'.format(self._token)
            },
            params=params,
            **kwargs
        )

        if response.status_code >= 400:
            error_response = response.json()

            raise(ToshlException(
                status_code=response.status_code,
                error_id=error_response['id'],
                error_description=error_response['description'],
                extra_info=error_response.get('fields')))

        return response

    def _list_response(self, response):
        """
        This method check if the response is a dict and wrap it into a list.
        If the response is already a list, it returns the response directly.
        This workaround is necessary because the API doesn't return a list
        if only one item is found.
        """
        if type(response) is list:
            return response
        if type(response) is dict:
            return [response]


class Account(object):
    def __init__(self, client):
        self.client = client

    def list(self):
        response = self.client._make_request('/accounts')
        response = response.json()
        return self.client._list_response(response)

    def search(self, account_name):
        accounts = self.list()
        for a in accounts:
            if a['name'] == account_name:
                return a['id']
