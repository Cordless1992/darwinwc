import zlib, stomp, untangle, xmltodict
from bs4 import BeautifulSoup
import lxml
import xml.etree.ElementTree
from xml.etree import ElementTree
from collections import OrderedDict

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
        #print XML
        with open('test.xml') as fd:
            p = xmltodict.parse(fd.read())
            #x = xmltodict.parse('test.xml')
        #x = p['Pport']['uR']['@updateOrigin']
        #if x == "TD":
        #print "Source from TD has been skipped"
        #lif x != "TD":
        #    uid = p['Pport']['uR']['TS']['@uid']
        #    ssd = p['Pport']['uR']['TS']['@ssd']
            #for location, value in p['Pport']['uR']['TS']['ns3:Location'].items():
            #    print(location['@tpl'])
            #locationA = p['Pport']['uR']['TS']['ns3:Location']['@tpl'][0]
        print p    
        #    print uid, ssd #, locationA #, arrtime #, locationA
        
        #obj = xmltodict.parse(XML)
        #obj = obj["Pport"]
        #root_elements = obj["uR"] if type(obj) == OrderedDict else [obj["uR"]] 
        # Above step ensures that root_elements is always a list
        #for element in root_elements:
        #    print element["tpl"]

conn = stomp.Connection([("datafeeds.nationalrail.co.uk", 61613)])

conn.set_listener('', MyListener())

conn.start()

conn.connect("d3user", "d3password")

QUEUE = "D379de05de-a524-4030-a862-a1f611eda684" # Your queue name here

conn.subscribe("/queue/"+QUEUE, id=1, ack='auto')

while 1:

    pass