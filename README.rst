KRA eTIMS API - Python Client
===============================

A Python wrapper for the KRA eTIMS REST API. Easily interact with the KRA eTIMS REST API using this library.

Installation
------------

.. code-block:: bash

    pip install kra-etims

Setup
-----

.. code-block:: python

    from kra_etims import API

    etimsapi = API(
        url="http://localhost:8088",
        pin="A123456789Z",
    )

Options
~~~~~~~

+-----------------------+-------------+----------+-------------------------------------------------------------------------------------------------------+
|         Option        |     Type    | Required |                                              Description                                              |
+=======================+=============+==========+=======================================================================================================+
| ``url``               | ``string``  | yes      | Your Server URL, example: http://localhost:8088/                                                      |
+-----------------------+-------------+----------+-------------------------------------------------------------------------------------------------------+
| ``pin``               | ``string``  | yes      | Your PIN                                                                                              |
+-----------------------+-------------+----------+-------------------------------------------------------------------------------------------------------+
| ``timeout``           | ``integer`` | no       | Connection timeout, default is ``5``                                                                  |
+-----------------------+-------------+----------+-------------------------------------------------------------------------------------------------------+
| ``verify_ssl``        | ``bool``    | no       | Verify SSL when connect, use this option as ``False`` when need to test with self-signed certificates |
+-----------------------+-------------+----------+-------------------------------------------------------------------------------------------------------+
| ``user_agent``        | ``string``  | no       | Set a custom User-Agent, default is ``KRA-eTIMS-Python-REST-API/1.0.1``                               |
+-----------------------+-------------+----------+-------------------------------------------------------------------------------------------------------+

Methods
-------

+--------------+----------------+------------------------------------------------------------------+
|    Params    |      Type      |                           Description                            |
+==============+================+==================================================================+
| ``endpoint`` | ``string``     | KRA eTIMS API endpoint, example: ``customers`` or ``order/12``   |
+--------------+----------------+------------------------------------------------------------------+
| ``data``     | ``dictionary`` | Data that will be converted to JSON                              |
+--------------+----------------+------------------------------------------------------------------+
| ``**kwargs`` | ``dictionary`` | Accepts ``params``, also other Requests arguments                |
+--------------+----------------+------------------------------------------------------------------+

POST
~~~~

- ``.post(endpoint, data, **kwargs)``

Response
--------

All methods will return `Response <http://docs.python-requests.org/en/latest/api/#requests.Response>`_ object.

Example of returned data:

.. code-block:: bash

    >>> r = etimsapi.post("/items/selectItems", {
            "bhfId":"00",
            "lastReqDt":"20160523000000"
        })
    >>> r.status_code
    200
    >>> r.headers['content-type']
    'application/json; charset=UTF-8'
    >>> r.encoding
    'UTF-8'
    >>> r.text
    u'{"resultCd": "000","resultMsg": "Successful","resultDt": "20240816201351","data": {"itemList": [{"tin": "P052350422M",...' // Json text
    >>> r.json()
    {u'resultCd': u'000',u'resultMsg': u'Successful',u'resultDt': u'20240816201351',u'data': {u'itemList': [{u'tin': u'P052350422M',... // Dictionary data

Changelog
---------

See `CHANGELOG.md <https://github.com/ingenious-dev/kra-etims-api-python/blob/trunk/CHANGELOG.md>`_.
