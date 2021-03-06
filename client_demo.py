import rpyc

#pickling of return objects 
rpyc.core.protocol.DEFAULT_CONFIG['allow_pickle'] = True


ZUMI_IP = '192.168.10.1' #default IP  if connected to umi Wifi
ZUMI_PORT = 9004 #port set at the RPC server

#conn = rpyc.ssl_connect(ZUMI_IP, ZUMI_PORT, keyfile="client.key", certfile="client.crt")

conn = rpyc.connect(ZUMI_IP, ZUMI_PORT)

# ping the zumi
ping = conn.root.ping()
print(ping)

#move forward
conn.root.forward()

#any otherZimi method can be called just like 
# conn.root.METHOD()

#close an open connection with
conn.close()

#check if connection is still avilve
conn.closed #-> returns bool

