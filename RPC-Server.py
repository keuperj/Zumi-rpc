import rpyc
from rpyc.utils.server import ThreadedServer
from rpyc.utils.authenticators import SSLAuthenticator
import ssl
import os
import datetime
from zumi.zumi import Zumi

DEBUG=True
PORT=9004

class ZumiService(rpyc.Service):
    """ RPC server class
    # Note 
        only methods that are _exposed_ are callable via rpc
    """

    def __init__(self):
        self.myConnection = ''
        self.user = ''
        #init zumi instance 
        self.zumi = Zumi()

    def on_connect(self, conn):
        """ method is automatically run at new rpc connections
        """
        self.myConnection = conn
        print ('new connection')

        #print (conn._config['credentials']['subject'])
        #self.user = conn._config['credentials']['subject'][5][0][1]
        #if DEBUG:
            #print("new connection: ",
            #      conn._config['endpoints'], "from user ", self.user)
        
        pass

    def on_disconnect(self, conn):
        """method is automatically run when rpc connection is terminated
        """
        if DEBUG:
            print ("conn ended", conn._config['connid'])
        pass

    def exposed_ping(self):
        """simple ping for rpc connection testing
        """
        if DEBUG:
            print ("ping")
        return 'pong'


    def exposed_forward(self):
        self.zumi.forward()





if __name__ == "__main__":
    print("Zumi RPC Server up ")
    auth = SSLAuthenticator("zumi_rpc.key", 
                            "zumi_rpc.crt", cert_reqs=ssl.CERT_REQUIRED, ca_certs="zumi_rpc.crt")
    server = ThreadedServer(ZumiService, port=PORT,  protocol_config={'allow_all_attr':True})
                            #authenticator=auth, protocol_config={'allow_all_attrs': True})
    server.start()
