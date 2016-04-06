import mock
from unittest import TestCase
from toshl.client import ToshlClient, Account


class TestAccount(TestCase):
    def test_account_init(self):
        client = ToshlClient('abcd1234')
        account = Account(client)
        assert account.client == client

    @mock.patch('toshl.client.requests.request')
    def test_list_accounts_successful(self, mock_request):
        mock_response = mock.Mock()
        expected_dict = {
            "id": "42",
            "name": "Account Test",
            "balance": 3000,
            "initial_balance": 3000,
            "currency": {
                "code": "USD",
                "rate": 1,
                "fixed": False
            },
            "median": {
                "expenses": 55,
                "incomes": 1300
            },
            "status": "active",
            "order": 0,
            "modified": "2012-09-04T13:55:15Z",
            "goal": {
                "amount": 63570,
                "start": "2013-07-01",
                "end": "2015-07-01"
            }
        }
        mock_response.json.return_value = expected_dict
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        client = ToshlClient('abcd1234')
        account = Account(client)
        response = account.list()

        mock_request.assert_called_once_with(
            headers={'Authorization': 'Bearer abcd1234'},
            method='GET', params=None, url='https://api.toshl.com/accounts')
        assert response == [expected_dict]

    @mock.patch('toshl.client.requests.request')
    def test_search_accounts_successful_multiple_accounts(self, mock_request):
        mock_response = mock.Mock()
        expected_dict = [
            {
                "id": "42",
                "name": "Account Test",
                "balance": 3000
            },
            {
                "id": "123",
                "name": "Test Found",
                "balance": 22000
            }
        ]

        mock_response.json.return_value = expected_dict
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        client = ToshlClient('abcd1234')
        account = Account(client)
        account_found = account.search('Test Found')

        mock_request.assert_called_once_with(
            headers={'Authorization': 'Bearer abcd1234'},
            method='GET', params=None, url='https://api.toshl.com/accounts')
        assert account_found is not None
        assert account_found == '123'

    @mock.patch('toshl.client.requests.request')
    def test_search_accounts_successful_single_account(self, mock_request):
        mock_response = mock.Mock()
        expected_dict = {
            "id": "123",
            "name": "Test Found",
            "balance": 22000
        }

        mock_response.json.return_value = expected_dict
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        client = ToshlClient('abcd1234')
        account = Account(client)
        account_found = account.search('Test Found')

        mock_request.assert_called_once_with(
            headers={'Authorization': 'Bearer abcd1234'},
            method='GET', params=None, url='https://api.toshl.com/accounts')
        assert account_found is not None
        assert account_found == '123'

    @mock.patch('toshl.client.requests.request')
    def test_search_accounts_not_found(self, mock_request):
        mock_response = mock.Mock()
        expected_dict = {
            "id": "123",
            "name": "Test Found",
            "balance": 22000
        }

        mock_response.json.return_value = expected_dict
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        client = ToshlClient('abcd1234')
        account = Account(client)
        account_found = account.search('Not Found')

        mock_request.assert_called_once_with(
            headers={'Authorization': 'Bearer abcd1234'},
            method='GET', params=None, url='https://api.toshl.com/accounts')
        assert account_found is None
