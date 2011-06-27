'''
Created on Jun 28, 2011

This module is only for testing the newsitemspicker component.
In real scenario, the queries to newsitemspicker component will
be sent by the web front end.
 
@author: Abhinav Tripathi
'''
import time
import logging
import stomp

'''
    Right now, only on_error is meaningful, we may find some use for other methods later on
'''
class QuerierListener(object):
    def on_error(self, headers, message):
        print 'received an error %s' % message

    def on_message(self, headers, message):
        for k,v in headers.iteritems():
            print('header: key %s , value %s' %(k,v))
        print('received message\n %s' %message)

logging.basicConfig()
log = logging.getLogger('stomp')
log.setLevel(logging.DEBUG)
connected = False
while not connected:
    try:
        conn = stomp.Connection()
        conn.set_listener('querierlistener', QuerierListener())
        conn.start()
        conn.connect(wait=True)
        connected = True
    except:
        pass

if connected:
    print 'Connected to broker!'
    print 'Will send in queries now to newsitemspicker component ...'

conn.send('userId:xyz,query:India', destination='/queue/queries')

time.sleep(2)
conn.disconnect()