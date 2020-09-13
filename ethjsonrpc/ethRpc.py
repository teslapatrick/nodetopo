"""
Author: maurycyp chenghuazheng
Url: https://github.com/ConsenSys/ethjsonrpc/blob/master/ethjsonrpc/exceptions.py
"""

import json
import warnings

import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError as RequestsConnectionError
# from ethereum import utils
# from ethereum.abi import encode_abi, decode_abi
#
# from ethjsonrpc.constants import BLOCK_TAGS, BLOCK_TAG_LATEST
# from ethjsonrpc.utils import hex_to_dec, clean_hex, validate_block
from ethjsonrpc.exceptions import (ConnectionError, BadStatusCodeError,
                                   BadJsonError, BadResponseError)

GETH_DEFAULT_RPC_PORT = 8545
ETH_DEFAULT_RPC_PORT = 8545
PARITY_DEFAULT_RPC_PORT = 8545
PYETHAPP_DEFAULT_RPC_PORT = 4000
MAX_RETRIES = 3
JSON_MEDIA_TYPE = 'application/json'


class EthJsonRpc(object):
    '''
    Ethereum JSON-RPC client class
    '''

    def __init__(self, host='localhost', port=GETH_DEFAULT_RPC_PORT, tls=False):
        self.host = host
        self.port = port
        self.tls = tls
        self.session = requests.Session()
        self.session.mount(self.host, HTTPAdapter(max_retries=MAX_RETRIES))

    def _call(self, method, params=None, _id=1):

        params = params or []
        data = {
            'jsonrpc': '2.0',
            'method':  method,
            'params':  params,
            'id':      _id,
        }
        scheme = 'http'
        if self.tls:
            scheme += 's'
        url = '{}://{}:{}'.format(scheme, self.host, self.port)
        headers = {'Content-Type': JSON_MEDIA_TYPE}
        try:
            r = self.session.post(url, headers=headers, data=json.dumps(data))
        except RequestsConnectionError:
            raise ConnectionError
        if r.status_code / 100 != 2:
            raise BadStatusCodeError(r.status_code)
        try:
            response = r.json()
        except ValueError:
            raise BadJsonError(r.text)
        try:
            return response['result']
        except KeyError:
            raise BadResponseError(response)

    '''
    @author chenghuazheng
    @pragma enode
    '''

    def admin_add_peer(self, enodes=[]):
        """
        Not Tested
        """
        return self._call(method='admin_addPeer', params=[enodes], _id=64)

    def admin_remove_peer(self, enode=''):
        """
        Tested
        """
        return self._call(method='admin_removePeer', params=[enode], _id=65)

    def admin_peers(self):
        """
        Tested
        """
        return self._call(method='admin_peers', params=[], _id=66)