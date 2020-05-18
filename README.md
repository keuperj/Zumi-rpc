# Zumi-rpc
Remote procedure call server and client for remote control of [Zumi robots](https://www.robolink.com/zumi/).

* *Python* API mirroring the [*Zumi* API](http://docs.robolink.com/zumi-library) from remote 
* allows compute intensive robot algoriths 
* uses the [*RPYC*](https://rpyc.readthedocs.io/en/latest/) remote procedure call lib for efficent and **secure** remote calls 

## Setup

### On the Zumi an the Client PC
Install ``rpyc``:
```
pip install rpyc
```

 
### Generate Certificates
```
openssl genrsa -out zumi_rpc.key 4096
openssl req -new -x509 -days 3650 -key zumi_rpc.key -out zumi_rpc.crt
chmod 600 zumi_rpc.key
chmod 600 zumi_rpc.crt
```
Copy key to ...
