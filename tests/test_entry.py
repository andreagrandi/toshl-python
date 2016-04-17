import mock
from unittest import TestCase
from toshl.client import ToshlClient
from toshl.entry import Entry


class TestEntry(TestCase):
    def test_entry_init(self):
        client = ToshlClient('abcd1234')
        entry = Entry(client)
        assert entry.client == client

    @mock.patch('toshl.client.requests.request')
    def test_create_entry_successful(self, mock_request):
        mock_response = mock.Mock()
        mock_response.status_code = 201
        mock_response.headers = {'Location': '/entries/1'}
        mock_request.return_value = mock_response

        client = ToshlClient('abcd1234')
        entry = Entry(client)

        json_payload = {
            'amount': -123.68,
            'currency': {
                'code': 'GBP'
            },
            'date': '2016-04-07',
            'account': 'abcd1234',
            'category': 'category-001'
        }

        response = entry.create(json_payload)

        mock_request.assert_called_once_with(
            headers={
                'Authorization': 'Bearer abcd1234',
                'Content-Type': 'application/json'
            },
            method='POST', params=None, url='https://api.toshl.com/entries',
            json=json_payload)
        assert response == '1'
