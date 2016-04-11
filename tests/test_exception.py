from unittest import TestCase
from toshl.exceptions import ToshlException


class TestToshlException(TestCase):
    def test_str_toshlexception(self):
        te = ToshlException(
            status_code=404,
            error_id='exception.not_found',
            error_description='Exception Not Found')
        self.assertEqual(
            str(te),
            '404 - exception.not_found: Exception Not Found')
