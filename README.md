# Zumi-rpc
Remote procedure call server and client for remote control of [Zumi robots](https://www.robolink.com/zumi/).

* *Python* API mirroring the [*Zumi* API](http://docs.robolink.com/zumi-library) from remote 
* allows compute intensive robot algorithms 
* uses the [*RPYC*](https://rpyc.readthedocs.io/en/latest/) remote procedure call lib for efficient and **secure** remote calls 

## Setup

### On the Zumi and the Client PC
Install ``rpyc``:
```
pip install rpyc
```

### On Zumi
*use ssh or the Jupyter terminal to get on a console*

Clone this Git repo:
```
git clone https://github.com/keuperj/Zumi-rpc.gi
```

 
#### Generate Certificates
in the ``Zumi-rpc`` folder, generate server credentials 
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
Now copy the client key and cert to your client machine and set proper rights:
```
chmod 700 client.*
```


#### Start Server
Use ssh or the Jupyter terminal to 
```
python3 RPC-Server.py &
```
For an automatic start at boot time, you can add this command to ```/etc/rc.local``` 

#### Working with Jupyter
The RPC Server does not interfer with the Jupyter frontend. You can run them both at the same time. Our typical workflow is to start the RPC-Server from a Jupyter terminal. 

#### Remote access over the Internet
If you want to access the Zumi not only from it's own Wifi, but accross the internet, you need a relay server. Details are explained in [our Zumi Repo](https://github.com/keuperj/ZumiWorld) - just replace the Jupyter Port 8888 with your RPC-Server port... 

## API
Zumi-RPC simply reproduces the original [*Zumi* API](http://docs.robolink.com/zumi-library), with some exceptions:

### Camera
We bypass the Zumi camera methods and interface ``picamera`` directly, allowing us to get high resolution images:
```
get_picture(resolution=(1024,768))
```  
returns a *NumPy* array of size (resolution_x, resolution_y,3) -> RGB image.

### get return values
if you call a function which returns an object, you need to make a copy of this object. Otherwise, you will only have a local reference to this object and the data remains on the Zumi! So, for the cam example:
```
frame = np.array(get_picture())
```
will produce a local copy of the output.

## Multtiple Connectons
The Zumi API and the RPC Server are non-blocking. Hence, you can have multiple RPC-clients connected to one server as well as use RPC and Jupyter simultaneously.

# More Zumi Libs and Hacks
see [our Zumi Repo](https://github.com/keuperj/ZumiWorld)
