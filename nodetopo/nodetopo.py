"""Main module."""

import web3
from ethjsonrpc.ethRpc import EthJsonRpc

class NodeClient:

    def __init__(self, address='http://127.0.0.1', port='8545'):
        self.url = address + port
        self.status = dict()
        self.client = web3.Web3(web3.Web3.HTTPProvider(self.url))
        self.ethRpc = EthJsonRpc()

    def status(self, enode=''):
        return self.status.get(enode)

    def add(self, enode=''):
        # check connection
        if not self.client.isConnected():
            return "Local node is not connected."

        # try add
        try:
            self.client.geth.admin.add_peer(enode)
        except:
            return "some errors."

    def Drop(self, enode='', all_nodes=False):
        if all_nodes:
            # drop all nodes
            '''
            @dev get from node
            @pragma peers
            '''

            # peers = self.client.geth.admin.peers
            peers = self.ethRpc.admin_peers()
            print(peers)
            # for peer in peers:
            #     print(peer)

        return True

        # drop enode
        pass


if __name__ == '__main__':
    nc = NodeClient()
    nc.Drop(all_nodes=True)
