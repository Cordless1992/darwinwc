import zlib, stomp #, xmltodict
import pymssql
from time import gmtime, strftime
#from bs4 import BeautifulSoup
#import lxml
#import xml.etree.ElementTree
#from xml.etree import ElementTree
#from collections import OrderedDict
#Naming needs to be changed for this file it is currently Untitled.py
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
                #Store values of data in a, b and c variables
                a = y.value
                b = o.value
                c = x.value
                t = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                print "Received at: ", t, "UID: ", a, " TIPLOC: ", b, " Source: ", c, " Status: Delayed"

                #Open DB connection (change as required)
                db = pymssql.connect(server='DESKTOP-3G1FB9B\SQLEXPRESS', user='sa', password='9964', database='Osmium')
                cursor = db.cursor()

                #Prepare information to be insered
                sql = "INSERT INTO `delayed`(`TME`, `UID`, `TPL`, `SOU`) VALUES (%s,%s,%s,%s)"
                
                #Commit changes to database
                try:
                    #("select freq from matrix_brown where a_id in (?) and b_id in (?)", (b_item_id,b_after_id))
                    #print "Starting Execute"
                    #cursor.execute(sql, (t,a,b,c))
                    cursor.executemany(
                        "INSERT INTO delayed VALUES (%s, %s, %s, %s)",
                        [(t, a, b, c)])
                    #print "Passed Execute"
                    db.commit()
                    #countera = countera  + 1
                    #print countera
                    #print "Written to Database"
                except Exception,e:
                    print e
                    db.rollback()
                    #print "Failed to Write to Database"
                db.close()

        #skip if nothing found in ns3:arrived/delayed attribute        
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
