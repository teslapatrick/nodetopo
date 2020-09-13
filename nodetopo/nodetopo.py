"""
@dev Main module.
@dev support python version >= 3.6
@author cheng_hua_zheng
"""
import json
import time

import web3
from ethjsonrpc.ethRpc import EthJsonRpc
from check import is_connected


class NodeClient:

    def __init__(self, address='http://127.0.0.1', port='8545', enodes=[]):
        self.url = address + port
        self.enodes_status = dict()
        self.enodes = list
        self.client = web3.Web3(web3.Web3.HTTPProvider(self.url))
        self.ethRpc = EthJsonRpc()
        self._init_enodes(enodes)

    def status(self, enode=''):
        if enode is not '':
            return self.enodes_status.get(enode)
        else:
            res = list()
            for enode, status in self.enodes_status.items():
                res.append({enode: status})
            return res

    @is_connected
    def _init_enodes(self, enodes: list):
        self.enodes = enodes

    @is_connected
    def check_all_nodes(self):
        """
        @dev get all nodes in node.
        @dev for threading use
        @dev TESTED
        """
        _all_linking_peers_enode = [peer.get('enode') for peer in self.ethRpc.admin_peers()]
        # check all nodes status
        for enode in self.enodes:
            _status = "not connected"
            if enode in _all_linking_peers_enode:
                _status = "connected"
            self.enodes_status.update({
                enode: _status
            })
        return

    @is_connected
    def try_to_connect_within_enodes(self, enode=''):
        # check already
        _current_peers = self.ethRpc.admin_peers()
        # try add
        try:
            if enode is not '':
                # res = self.client.geth.admin.add_peer(enode)
                self.ethRpc.admin_add_peer(enodes=enode)
                self.enodes.append(enode)
                return
            for enode in self.enodes:
                # _peer_enode = peer.get('enode')
                # self.self.client.geth.admin.add_peer(_peer_enode)
                self.ethRpc.admin_add_peer(enodes=enode)
            return
        except:
            return "some errors."

    @is_connected
    def drop(self, enode=''):
        if enode is '':
            # drop all nodes
            '''
            @dev get from node
            @pragma peers
            '''
            # peers = self.client.geth.admin.peers
            peers = self.ethRpc.admin_peers()
            for peer in peers:
                _peer_enode = peer.get('enode')
                self.ethRpc.admin_remove_peer(enode=_peer_enode)
            return
        # drop enode
        self.ethRpc.admin_remove_peer(enode=enode)
        return

if __name__ == '__main__':
    nc = NodeClient(enodes=['enode://556707f7f596d3696ca16cea7d2b0e10a62f12b373e84a78317047b8f859e7e892fff9fd7705dab4457df96f879e67ff88b89bd00f5986c62d13e5d32a08a5cc@139.186.69.17:30303'])
    # nc.add()
    nc.check_all_nodes()
    print(nc.status())
    # nc.drop()
    nc.try_to_connect_within_enodes()
    # time.sleep(5)
    nc.check_all_nodes()
    print(nc.status())