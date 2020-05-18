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

### On Zumi
Clone this Git repo:
```
git clone https://github.com/keuperj/Zumi-rpc.gi
```

 
#### Generate Certificates
in the ``Zumi-rpc`` folder, generate server credetials 
```
openssl genrsa -out zumi_rpc.key 4096
openssl req -new -x509 -days 3650 -key zumi_rpc.key -out zumi_rpc.crt
chmod 600 zumi_rpc.key
chmod 600 zumi_rpc.crt
```

Then generate client credentials 
```
openssl genrsa -out client.key 4096
openssl req -new -key client.key -out client.csr  -passin pass:""
openssl x509 -req -days 3652 -in client.csr -CA zumi_rpc.crt -CAkey zumi_rpc.key -set_serial 01 -out client.crt
rm client.csr
```
Now cop the client key and cert to your client machine and set propper rights:
```
chmod 700 client.*
```


#### Start Server
```
python3 RPC-Server.py &
```

