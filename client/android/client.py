#-*- coding:utf-8 -*-

from kivy.network.urlrequest import UrlRequest


class RestClient(object):
    url = None
    callback = None
    errback = None

    @staticmethod
    def get(query=''):
        url = RestClient.url + query
        RestClient._send_request('GET', url)

    @staticmethod
    def post(data):
        url = RestClient.url
        RestClient._send_request('POST', url, data)

    @staticmethod
    def patch(data, query=''):
        url = RestClient.url + query
        RestClient._send_request('PATCH', url, data)

    @staticmethod
    def delete(query=''):
        url = RestClient.url + query
        RestClient._send_request('DELETE', url)

    @staticmethod
    def _send_request(method, url, data=None):
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        if data:
            headers['Content-Length'] = str(len(data))
        UrlRequest(url, req_body=data, req_headers=headers,
                   method=method,
                   debug=True,
                   decode=False,
                   on_success=RestClient.callback,
                   on_failure=RestClient.errback,
                   on_error=RestClient.errback)
