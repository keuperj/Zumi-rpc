import rpyc

ZUMI_IP = '192.168.10.1' #default IP  if connected to umi Wifi
ZUMI_PORT = 9004

#conn = rpyc.ssl_connect(ZUMI_IP, ZUMI_PORT, keyfile="client.key", certfile="client.crt")

conn = rpyc.connect(ZUMI_IP, ZUMI_PORT)

# ping the zumi
ping = conn.root.ping()
print(ping)

#move forward
conn.root.forward()

#any otherZimi method can be called just like 
# conn.root.METHOD()

