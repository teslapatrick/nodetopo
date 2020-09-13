from functools import wraps
from web3 import Web3, HTTPProvider
from ethjsonrpc.ethRpc import EthJsonRpc


def is_connected(func):
    '''
    @dev check connection
    TESTED
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        client = Web3(HTTPProvider('http://127.0.0.1:8545'))
        if not client.isConnected():
            raise ConnectionError("Node not connected.")
        return func(*args, **kwargs)
    return wrapper


def all_node_connected(need_peers, now_peers):
    for peer in need_peers:
        _enode = peer.get('enode')
        if _enode not in now_peers:
            print("Node {} not connected.".format(_enode))

# @is_connected
# def all_node_connected(func, need_peers, now_peers):
#     '''
#     @dev ensure all nodes connected
#     '''
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         for peer in need_peers:
#             _enode = peer.get('id')
#             if _enode not in now_peers:
#                 print("Node {} not connected.".format(_enode))
#         return func(*args, **kwargs)
#     return wrapper


