'''
Created on May 16, 2011

@author: abhinav
'''
import time
import random
import logging
import stomp
import socket

class MyListener(object):
    def on_error(self, headers, message):
        print 'received an error %s' % message

    def on_message(self, headers, message):
        for k,v in headers.iteritems():
            print('header: key %s , value %s' %(k,v))
        print('received message\n %s'% message)

logging.basicConfig()
log = logging.getLogger('Stomp')
log.setLevel(logging.DEBUG)
connected = False
while not connected:
    try:
        conn = stomp.Connection()
        conn.set_listener('simplelistener', MyListener())
        conn.start()
        conn.connect(wait=True)
        conn.subscribe(destination='/queue/test', ack='auto')
        connected = True
    except:
        pass

if connected:
    print 'Connected to broker now!'

message = {'field1' : 'foo', 'field2' : 'bar'}
conn.send(message, destination='/queue/test')

time.sleep(2)
conn.disconnect()