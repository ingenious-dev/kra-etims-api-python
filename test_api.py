""" API Tests """
import unittest
import kra_etims
from httmock import all_requests, HTTMock


class KRAeTIMSTestCase(unittest.TestCase):
    """Test case for the client methods."""

    def setUp(self):
        self.pin = "A123456789Z"
        self.api = kra_etims.API(
            url="http://localhost:8088",
            pin=self.pin,
        )

    def test_with_timeout(self):
        """ Test timeout """
        api = kra_etims.API(
            url="https://localhost:8088",
            pin=self.pin,
            timeout=10,
        )
        self.assertEqual(api.timeout, 10)

        @all_requests
        def etims_test_mock(*args, **kwargs):
            """ URL Mock """
            return {'status_code': 200,
                    'content': 'OK'}

        with HTTMock(etims_test_mock):
            # call requests
            status = api.post("/items/selectItems", {
                "bhfId":"00",
                "lastReqDt":"20160523000000"
            }).status_code
        self.assertEqual(status, 200)

    def test_post(self):
        """ Test POST requests """
        @all_requests
        def etims_test_mock(*args, **kwargs):
            """ URL Mock """
            return {'status_code': 200,
                    'content': 'OK'}

        with HTTMock(etims_test_mock):
            # call requests
            status = self.api.post("/items/selectItems", {
                "bhfId":"00",
                "lastReqDt":"20160523000000"
            }).status_code
        self.assertEqual(status, 200)