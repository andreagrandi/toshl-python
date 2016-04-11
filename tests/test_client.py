# -*- coding: utf-8 -*-
import mock
from unittest import TestCase
from toshl.client import ToshlClient
from toshl.exceptions import ToshlException


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

    @mock.patch('toshl.client.requests.request')
    def test_client_request_raises_exception_on_400(self, mock_request):
        mock_response = mock.Mock()
        expected_dict = {
            'error_id': 'exception_id',
            'description': 'Exception description'
        }
        mock_response.json.return_value = expected_dict
        mock_response.status_code = 400
        mock_request.return_value = mock_response

        client = ToshlClient('abcd1234')

        with self.assertRaises(ToshlException) as ex:
            client._make_request('/me', 'GET')

        assert ex.exception.status_code == 400
        assert ex.exception.error_id == 'exception_id'
        assert ex.exception.error_description == 'Exception description'
        assert ex.exception.extra_info is None

    @mock.patch('toshl.client.requests.request')
    def test_client_request_raises_exception_with_extra_info(
            self, mock_request):
        mock_response = mock.Mock()
        expected_dict = {
            'error_id': 'exception_id',
            'description': 'Exception description',
            "fields": [
                {
                    "field": "amount",
                    "error": "Amount cannot be zero."
                },
                {
                    "field": "category",
                    "error": "Please select at least one category."
                }
            ]
        }
        mock_response.json.return_value = expected_dict
        mock_response.status_code = 400
        mock_request.return_value = mock_response

        client = ToshlClient('abcd1234')

        with self.assertRaises(ToshlException) as ex:
            client._make_request('/me', 'GET')

        assert ex.exception.status_code == 400
        assert ex.exception.error_id == 'exception_id'
        assert ex.exception.error_description == 'Exception description'
        assert ex.exception.extra_info == [
            {
                "field": "amount",
                "error": "Amount cannot be zero."
            },
            {
                "field": "category",
                "error": "Please select at least one category."
            }
        ]
