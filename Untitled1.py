import zlib, stomp#, xmltodict
#from bs4 import BeautifulSoup
#import lxml
#import xml.etree.ElementTree
#from xml.etree import ElementTree
#from collections import OrderedDict
import xml.dom.minidom
from xml.dom.minidom import parse, parseString

class MyListener(object):
    def on_error(self, headers, message):
        print('received an error %s' % message)

    def on_message(self, headers, message):

        decompressed_data=zlib.decompress(message, 16+zlib.MAX_WBITS)

        #print('received a message %s' % decompressed_data)
        XML = decompressed_data
        f = open("test.xml","wb")
        f.write(XML)
        f.close()
        dom = parse("test.xml")
        
#Example <uR updateOrigin="Darwin"><TS rid="201604221223687" ssd="2016-04-22" uid="W05044">
        
        for node1 in dom.getElementsByTagName('uR'):
            x = node1.attributes["updateOrigin"]      #Information Source
            
        for node2 in dom.getElementsByTagName('TS'):
            y = node2.attributes["uid"]               #UID
            
        for node in dom.getElementsByTagName('ns3:Location'):
            o = node.attributes["tpl"]               #TIPLOC Information
            #print y.value, o.value, x.value

            #print XML for testing purposes (if commented its off)
            
        try:
            for node3 in dom.getElementsByTagName('ns3:arr'):
                d = node3.attributes["delayed"]
                print y.value, o.value, x.value, d.value
        except KeyError:
                pass
                #print XML

conn = stomp.Connection([("datafeeds.nationalrail.co.uk", 61613)])

conn.set_listener('', MyListener())

conn.start()

conn.connect("d3user", "d3password")

QUEUE = "D379de05de-a524-4030-a862-a1f611eda684" # Your queue name here

conn.subscribe("/queue/"+QUEUE, id=1, ack='auto')

while 1:

    pass
