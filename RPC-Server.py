#------------------------------------------------------
#
# Zumi RPC
#
# A light-weight remote API for Zumi Robots,
# see Zumi API for method descriptions: http://docs.robolink.com/zumi-library
#
# 2020 by Janis Keuper
# Institute for Machine Learning and Analytics - www.imla.ai
# Offenburg University, Germany
#
# License: GPLv3
#------------------------------------------------------

import rpyc
from rpyc.utils.server import ThreadedServer
from rpyc.utils.authenticators import SSLAuthenticator
import ssl
import os
import datetime
from zumi.zumi import Zumi
import picamera


# server parameters 
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

#-----------------------------------------------------------------------------
# reproducing ZUMI API - see http://docs.robolink.com/zumi-library for details
#-----------------------------------------------------------------------------

# DRIVING
    def exposed_right_circle(self, speed=30, step=2):
        self.zumi.right_circle(speed, step)

    def exposed_hard_brake(self):
        self.zumi.hard_brake()

    def exposed_parallel_park(self,speed=15, step=1, delay=0.01):
        self.zumi.parallel_park(speed, step, delay)

    def exposed_circle(self,speed=30, step=2, direction=1, delay=0.02):
        self.zumi.circle(speed, step, direction, delay)

    def exposed_triangle(self,speed=40, seconds=1.5, direction=1):
        self.zumi.triangle(speed, seconds, direction)

    def exposed_go_straight(self,speed, desired_angle, max_speed=127):
        self.zumi.go_straight(speed, desired_angle, max_speed)

    def exposed_right_u_turn(self,speed=30, step=4, delay=0.02):
        self.zumi.right_u_turn(speed, step, delay)

    def exposed_figure_8(self,speed=30, step=3, delay=0.02):
        self.zumi.figure_8(speed, step, delay)

    def exposed_rectangle(self,speed=40, seconds=1.0, direction=1, ratio=2):
        self.zumi.rectangle(speed, seconds, direction, ratio)

    def exposed_reverse(self,speed=40, duration=1.0, desired_angle=123456):
        self.zumi.reverse(speed, duration, desired_angle)

    def exposed_left_u_turn(self,speed=30, step=4, delay=0.02):
        self.zumi.left_u_turn(speed, step, delay)

    def exposed_square(self,speed=40, seconds=1, direction=1):
        self.zumi.square(speed, seconds, direction)

    def exposed_square_left(self,speed=40, seconds=1.0):
        self.zumi.square_left(speed, seconds)

    def exposed_turn_left(self,desired_angle=90, duration=1.0):
        self.zumi.turn_left(desired_angle, duration)

    def exposed_j_turn(self,speed=80, step=4, delay=0.005):
        self.zumi.j_turn(speed, step, delay)

    def exposed_left_circle(self,speed=30, step=2):
        self.zumi.left_circle(speed, step)

    def exposed_forward(self,speed=40, duration=1.0, desired_angle=123456):
        self.zumi.forward(speed, duration, desired_angle)

    def exposed_turn_right(self,desired_angle=-90,duration=1.0):
        self.zumi.turn_right(desired_angle,duration)

    def exposed_square_right(self,speed=40, seconds=1.0):
        self.zumi.square_right(speed, seconds)

    def exposed_go_reverse(self, speed, desired_angle, max_speed=127):
        self.zumi.go_reverse(speed, desired_angle, max_speed)

#SENSORS

    def exposed_get_all_IR_data(self):
        return self.zumi.get_all_IR_data()

    def exposed_get_battery_voltage(self):
        return self.zumi.get_battery_voltage()

    #this is undocumented in the Zumi API
    def exposed_get_battery_percentage(self):
        self.zumi.get_battery_percentage()

    def exposed_get_IR_data(self,ir_sensor_index):
        self.zumi.get_IR_data(ir_sensor_index)

# CAM - here we use picamera directly, avoiding the poor zumi interface

    def exposed_get_picture(self, resolution=(1024,768)):
        with picamera.PiCamera() as camera:
            camera.resolution = resolution
            camera.rotation = 180
            output = np.empty((resolution[0],resolution[1],3),dtype=np.uint8)
            camera.capture(output , 'rgb')

        return output



if __name__ == "__main__":
    print("Zumi RPC Server up ")
    auth = SSLAuthenticator("zumi_rpc.key", 
                            "zumi_rpc.crt", cert_reqs=ssl.CERT_REQUIRED, ca_certs="zumi_rpc.crt")
    server = ThreadedServer(ZumiService, port=PORT,  protocol_config={'allow_all_attr':True})
                            #authenticator=auth, protocol_config={'allow_all_attrs': True})
    server.start()
