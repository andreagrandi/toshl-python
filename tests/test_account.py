from toshl.client import ToshlClient, Account
from unittest import TestCase


class TestAccount(TestCase):
    def test_account_init(self):
        client = ToshlClient('abcd1234')
        account = Account(client)
        assert account.client == client
