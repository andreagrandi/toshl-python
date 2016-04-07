import mock
from unittest import TestCase
from toshl.client import ToshlClient, Category


class TestCategory(TestCase):
    def test_category_init(self):
        client = ToshlClient('abcd1234')
        category = Category(client)
        assert category.client == client

    @mock.patch('toshl.client.requests.request')
    def test_list_categories_successful(self, mock_request):
        mock_response = mock.Mock()
        expected_dict = [
            {
                "id": "42",
                "name": "Entertainment",
                "modified": "2012-09-04T13:55:15Z",
                "type": "expense",
                "deleted": False,
                "counts": {
                    "entries": 21,
                    "tags": 5
                }
            },
            {
                "id": "58",
                "name": "Sport",
                "modified": "2012-09-04T13:55:15Z",
                "type": "expense",
                "deleted": False,
                "counts": {
                    "entries": 21,
                    "tags": 5
                }
            }
        ]

        mock_response.json.return_value = expected_dict
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        client = ToshlClient('abcd1234')
        category = Category(client)
        response = category.list()

        mock_request.assert_called_once_with(
            headers={'Authorization': 'Bearer abcd1234'},
            method='GET', params=None, url='https://api.toshl.com/categories')
        assert response == expected_dict
