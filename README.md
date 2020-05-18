# Zumi-rpc
remote procedure call server and client for remote control of zumi robots

## Setup

### Generate Certificates
```
openssl genrsa -out zumi_rpc.key 4096
openssl req -new -x509 -days 3650 -key zumi_rpc.key -out zumi_rpc.crt
chmod 600 zumi_rpc.key
chmod 600 zumi_rpc.crt
```
Copy key to ...
