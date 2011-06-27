'''
Created on Jun 26, 2011

@author: Abhinav Tripathi
'''
import logging
import stomp

class NewsItemsListener(object):
    def on_error(self, headers, message):
        print 'received an error %s' % message

    def on_message(self, headers, message):
        print('received message\n %s'% message)

'''
    Initialize logging
'''
logging.basicConfig()
log = logging.getLogger('stomp')
log.setLevel(logging.DEBUG)

'''
    Initiate connection with broker, set listener for news items
'''
connected = False
while not connected:
    try:
        conn = stomp.Connection()
        conn.set_listener('newsitemslistener', NewsItemsListener())
        conn.start()
        conn.connect(wait=True)
        conn.subscribe(destination='/queue/newsitems', ack='auto')
        connected = True
    except:
        pass

if connected:
    print 'Connected to the Stomp broker!'
    print 'Listening for news item messages now ...'
