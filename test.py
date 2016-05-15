import zlib, stomp
import pymssql
from time import gmtime, strftime
import xml.dom.minidom
from xml.dom.minidom import parse, parseString
class MyListener(object):
	def on_error(self, headers, message):
		print('received an error %s' % message)

	def on_message(self, headers, message):

		decompressed_data=zlib.decompress(message, 16+zlib.MAX_WBITS)

		XML = decompressed_data
		f = open("test.xml","wb")
		f.write(XML)
		f.close()
		dom = parse("test.xml")
		a = "r"
		L = "0"
				
		for node1 in dom.getElementsByTagName('uR'):
			x = node1.attributes["updateOrigin"]      #Information Source
			c = x.value
		for node2 in dom.getElementsByTagName('TS'):
			y = node2.attributes["uid"]               #UID
			a = y.value
		for node in dom.getElementsByTagName('ns3:Location'):
			o = node.attributes["tpl"]               #TIPLOC Information
			b = o.value
		db = pymssql.connect(server='DESKTOP-3G1FB9B\SQLEXPRESS', user='sa', password='9964', database='Osmium')
		cursor = db.cursor()

		if b == "TD":
                        print "Last report from TD, feature currnetly switched off"

                elif b == "CIS":
                        print "Last report from CIS, feature currnetly switched off"
                        
                else:
                        try:
                                sql = "SELECT TOP 1 * FROM [delayed] Order by [ID] DESC"
                                cursor.execute(sql)
                                results = cursor.fetchall()
                                for row in results:
                                        L = row[1]
                        except:
                                pass

                        db.close()

                        try:
                                for node3 in dom.getElementsByTagName('ns3:arr'):
                                        d = node3.attributes["delayed"]

                                t = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		
                        except KeyError:
                                print "Train is not delayed"
								
                                a = L
                                pass

                        if a == L:
                                try:
                                        db = pymssql.connect(server='DESKTOP-3G1FB9B\SQLEXPRESS', user='sa', password='9964', database='Osmium')
                                        cursor = db.cursor()
                                        sql = "DELETE FROM delayed WHERE UID=%s"
                                        cursor.execute(sql, (a))
                                        print "Train", y.value, "has been deleted from the database"
                                except Exception,e:
                                        print e
                                        print "Train not in database"
                                pass
                        else:
                                print "Received at: ", t, "UID: ", a, " TIPLOC: ", b, " Source: ", c, " Status: Delayed"
                                db = pymssql.connect(server='DESKTOP-3G1FB9B\SQLEXPRESS', user='sa', password='9964', database='Osmium')
                                cursor = db.cursor()

                                sql = "INSERT INTO `delayed`(`TME`, `UID`, `TPL`, `SOU`) VALUES (%s,%s,%s,%s)"

                                try:
                                        cursor.executemany(
                                                "INSERT INTO delayed VALUES (%s, %s, %s, %s)",
                                                [(t, a, b, c)])

                                        db.commit()
                                except Exception,e:
                                        print e
                                        db.rollback()
                                db.close()


conn = stomp.Connection([("datafeeds.nationalrail.co.uk", 61613)])

conn.set_listener('', MyListener())

conn.start()

conn.connect("d3user", "d3password")

QUEUE = "D379de05de-a524-4030-a862-a1f611eda684" # Your queue name here

conn.subscribe("/queue/"+QUEUE, id=1, ack='auto')

while 1:

	pass
