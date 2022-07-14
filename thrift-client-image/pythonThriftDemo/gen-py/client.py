from test import Transmit
from test.ttypes import *
from test.constants import *
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

import logging
import time
'''
def init_tracer(service):
    log_level = logging.DEBUG
    logging.getLogger('').handlers = []
    logging.basicConfig(format='%(asctime)s %(message)s', level=log_level)

    config = Config(
        config={ 
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'logging': True,
        },  
        service_name=service,
        validate=True,
    )
    
    return config.initialize_tracer()
'''




transport = TSocket.TSocket('127.0.0.1', 8013)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = Transmit.Client(protocol)


# Connect!
transport.open()
i= 0
 while i<3:
    msg = message (i,"hello")
     # scope.span.log_kv({'event': 'put_start'})
    client.put(msg)
     # scope.span.log_kv({'event': 'put_end'})
    i = i+1
    time.sleep(0.5)

transport.close()
time.sleep(2) # flush buffer
tracer.close()
