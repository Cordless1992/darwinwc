#WARNING - This is an unstable testing copy and should only be used by testers
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

		#print('received a message %s' % decompressed_data)
		XML = decompressed_data
		f = open("test.xml","wb")
		f.write(XML)
		f.close()
		dom = parse("test.xml")
		#print "written to file"
		a = "r"
		L = "0"
		#Example <uR updateOrigin="Darwin"><TS rid="201604221223687" ssd="2016-04-22" uid="W05044">
		
		for node1 in dom.getElementsByTagName('uR'):
			x = node1.attributes["updateOrigin"]      #Information Source
			
		for node2 in dom.getElementsByTagName('TS'):
			y = node2.attributes["uid"]               #UID
			a = y.value
		for node in dom.getElementsByTagName('ns3:Location'):
			o = node.attributes["tpl"]               #TIPLOC Information
			#print y.value, o.value, x.value

			#print XML for testing purposes (if commented its off)
		#print "TEST"
		db = pymssql.connect(server='DESKTOP-3G1FB9B\SQLEXPRESS', user='sa', password='9964', database='Osmium')
		cursor = db.cursor()
		try:
                        sql = "SELECT TOP 1 * FROM [delayed] Order by [ID] DESC"
                        #print "Conneceted to database and etc"
                        cursor.execute(sql)
                        results = cursor.fetchall()
                        for row in results:
                                L = row[1]
                except:
                        pass

                db.close()
		#print y.value
		#print L
		print "value inputted to L"
		try:
			for node3 in dom.getElementsByTagName('ns3:arr'):
				d = node3.attributes["delayed"]
				#Store values of data in a, b and c variables
			
			b = o.value
			c = x.value
			t = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			#print "Stored delayed services to variables"
		
		except KeyError:
			#Check for change in movement
								
			a = L
			pass

		if a == L:
			try:
                                db = pymssql.connect(server='DESKTOP-3G1FB9B\SQLEXPRESS', user='sa', password='9964', database='Osmium')
                                cursor = db.cursor()
				sql = "DELETE FROM delayed WHERE UID=%s"
				cursor.execute(sql, (a))
				print "Train", y.value, "from database"
			except Exception,e:
                                print e
				print "Train not in database"
			
			#print "Already stored or not delayed"
			pass
		else:
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
						 #print XML

conn = stomp.Connection([("datafeeds.nationalrail.co.uk", 61613)])

conn.set_listener('', MyListener())

conn.start()

conn.connect("d3user", "d3password")

QUEUE = "D379de05de-a524-4030-a862-a1f611eda684" # Your queue name here

conn.subscribe("/queue/"+QUEUE, id=1, ack='auto')

while 1:

	pass
