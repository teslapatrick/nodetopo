
class nodeInfo:
    def __init__(self, enode='', id='', name='', caps=[], network={}, protocols={}):
        self.enode = enode
        self.id = id
        self.name = name
        self.caps = caps
        self.network = dict(localAddress='' if network.get('localAddress') is None else network['localAddress'],
                            remoteAddress='' if network.get('localAddress') is None else network['localAddress'],
                            inbound=False if network.get('inbound') is None else network['inbound'],
                            trusted=False if network.get('trusted') is None else network['trusted'],
                            static=False if network.get('static') is None else network['static'])
        self.protocols = dict(eth=dict(version=65 if protocols.get('eth').get('version') is None else protocols['eth']['version'],
                                       difficulty=0 if protocols.get('eth').get('difficulty') is None else protocols['eth']['difficulty'],
                                       head='' if protocols.get('eth').get('head') is None else protocols['eth']['head']))
