import rpyc

ZUMI_IP = '91.250.118.129'#'192.168.10.1'
ZUMI_PORT = 9004

#conn = rpyc.ssl_connect(ZUMI_IP, ZUMI_PORT, keyfile="client.key", certfile="client.crt")

conn = rpyc.connect(ZUMI_IP, ZUMI_PORT)

# ping the zumi
ping = conn.root.ping()
print(ping)

#move forward
conn.root.forward()


