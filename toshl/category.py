class Category(object):
    def __init__(self, client):
        self.client = client

    def list(self):
        response = self.client._make_request('/categories')
        response = response.json()
        return self.client._list_response(response)

    def search(self, category_name):
        categories = self.list()
        for c in categories:
            if c['name'] == category_name:
                return c['id']
