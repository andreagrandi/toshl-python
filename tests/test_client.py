# -*- coding: utf-8 -*-
from toshl.client import ToshlClient
import mock
from unittest import TestCase


class TestClient(TestCase):
    def setUp(self):
        self.success_mocked_response = mock.Mock()
        self.success_mocked_response.status_code = 200

    def test_client_init(self):
        client = ToshlClient('abcd1234')
        assert client._token == 'abcd1234'

    def test_client_has_base_url(self):
        client = ToshlClient('abcd1234')
        base_api_url = getattr(client, 'BASE_API_URL', None)
        assert base_api_url is not None

    @mock.patch('toshl.client.requests.request')
    def test_client_can_make_request(self, mock_request):
        mock_request.return_value = self.success_mocked_response
        client = ToshlClient('abcd1234')
        client._make_request('/me', 'GET')
        mock_request.assert_called_once_with(
            headers={'Authorization': 'Bearer abcd1234'},
            method='GET', params=None, url='https://api.toshl.com/me')

    @mock.patch('toshl.client.requests.request')
    def test_client_can_make_request_with_params(self, mock_request):
        mock_request.return_value = self.success_mocked_response
        client = ToshlClient('abcd1234')
        client._make_request('/me', 'GET', params={'a': 'foo1', 'b': 'foo2'})
        mock_request.assert_called_once_with(
            headers={'Authorization': 'Bearer abcd1234'},
            method='GET', params={'a': 'foo1', 'b': 'foo2'},
            url='https://api.toshl.com/me')

    @mock.patch('toshl.client.requests.request')
    def test_client_can_make_request_with_utf8_params(self, mock_request):
        mock_request.return_value = self.success_mocked_response
        client = ToshlClient('abcd1234')
        client._make_request(
            '/me', 'GET', params={'a': u'foo1', 'b': u'£123'})
        mock_request.assert_called_once_with(
            headers={'Authorization': 'Bearer abcd1234'},
            method='GET', params={'a': u'foo1', 'b': u'\xa3123'},
            url='https://api.toshl.com/me')

    @mock.patch('toshl.client.requests.request')
    def test_client_set_auth_token_correctly(self, mock_request):
        mock_request.return_value = self.success_mocked_response
        client = ToshlClient('AAABBBCCCDDD')
        client._make_request('/me', 'GET', params={'a': 'foo1', 'b': 'foo2'})
        assert mock_request.call_args[1]['headers']['Authorization'] == \
            'Bearer AAABBBCCCDDD'
