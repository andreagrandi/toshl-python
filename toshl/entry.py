class Entry(object):
    def __init__(self, client):
        self.client = client

    def create(self, json_payload):
        response = self.client._make_request(
            '/entries', 'POST', json=json_payload)
        if response.status_code == 201:
            return self.client._parse_location_header(response)
