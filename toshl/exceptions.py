class ToshlException(Exception):
    def __init__(
            self, status_code, error_id, error_description, extra_info=None):
        self.status_code = status_code
        self.error_id = error_id
        self.error_description = error_description
        self.extra_info = extra_info

    def __str__(self):
        return '{0} - {1}: {2}'.format(
            self.status_code, self.error_id, self.error_description)
