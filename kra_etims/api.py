# -*- coding: utf-8 -*-

"""
KRA eTIMS API Class
"""

__title__ = "kra-etims-api"
__version__ = "1.0.1"
__author__ = "Joseph Suhudu @ ingenious.or.ke"
__license__ = "MIT"

from requests import request
from json import dumps as jsonencode


class API(object):
    """ API Class """

    def __init__(self, url, pin, **kwargs):
        self.url = url
        self.pin = pin
        self.wp_api = kwargs.get("wp_api", True)
        self.version = kwargs.get("version", "")
        self.timeout = kwargs.get("timeout", 5)
        self.verify_ssl = kwargs.get("verify_ssl", True)
        self.user_agent = kwargs.get("user_agent", f"KRA-eTIMS-Python-REST-API/{__version__}")

    def __get_url(self, endpoint):
        """ Get URL for requests """
        url = self.url

        if url.endswith("/") is False:
            url = f"{url}/"

        # This is anticipation of the KRA using this convention when versioning
        if self.version:
            return f"{url}{self.version}/{endpoint}"
        
        return f"{url}{endpoint}"

    def __request(self, method, endpoint, data, params=None, **kwargs):
        """ Do requests """
        if params is None:
            params = {}
        url = self.__get_url(endpoint)
        headers = {
            "user-agent": f"{self.user_agent}",
            "accept": "application/json"
        }

        if data is not None:
            data['tin'] = self.pin
            data = jsonencode(data, ensure_ascii=False).encode('utf-8')
            headers["content-type"] = "application/json;charset=utf-8"

        return request(
            method=method,
            url=url,
            verify=self.verify_ssl,
            params=params,
            data=data,
            timeout=self.timeout,
            headers=headers,
            **kwargs
        )

    def get(self, endpoint, **kwargs):
        """ Get requests """
        return self.__request("GET", endpoint, None, **kwargs)

    def post(self, endpoint, data, **kwargs):
        """ POST requests """
        return self.__request("POST", endpoint, data, **kwargs)

    def put(self, endpoint, data, **kwargs):
        """ PUT requests """
        return self.__request("PUT", endpoint, data, **kwargs)

    def delete(self, endpoint, **kwargs):
        """ DELETE requests """
        return self.__request("DELETE", endpoint, None, **kwargs)

    def options(self, endpoint, **kwargs):
        """ OPTIONS requests """
        return self.__request("OPTIONS", endpoint, None, **kwargs)
