class Account(object):
    def __init__(self, client):
        self.client = client

    def list(self):
        """
        Return a list of Accounts from Toshl for the current user
        """
        response = self.client._make_request('/accounts')
        response = response.json()
        return self.client._list_response(response)

    def search(self, account_name):
        """
        Get a list of all the Accounts for the current user and return the ID
        of the one with the specified name.
        """
        accounts = self.list()
        for a in accounts:
            if a['name'] == account_name:
                return a['id']

    def get(self, account_id):
        """
        Return a specific account given its ID
        """
        response = self.client._make_request('/accounts/{0}'.format(account_id))
        return response.json()

    def create(self, json_payload):
        response = self.client._make_request(
            '/accounts', 'POST', json=json_payload)
        if response.status_code == 201:
            return self.client._parse_location_header(response)

    def update(self, account_id, json_payload):
        response = self.client._make_request(
            '/accounts/{0}'.format(account_id), 'PUT', json=json_payload)
        if response.status_code == 200:
            return response.json()

    def delete(self, account_id):
        return self.client._make_request(
            '/accounts/{0}'.format(account_id), 'DELETE')
