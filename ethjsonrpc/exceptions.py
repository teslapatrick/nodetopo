"""
Author: maurycyp
Url: https://github.com/ConsenSys/ethjsonrpc/blob/master/ethjsonrpc/exceptions.py
"""

class EthJsonRpcError(Exception):
    pass


class ConnectionError(EthJsonRpcError):
    pass


class BadStatusCodeError(EthJsonRpcError):
    pass


class BadJsonError(EthJsonRpcError):
    pass


class BadResponseError(EthJsonRpcError):
    pass