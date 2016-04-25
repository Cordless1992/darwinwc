import MySQLdb
from time import gmtime, strftime
from datetime import datetime
from datetime import timedelta
#Naming needs to be changed for this file it is currently Untitled2.py
import xml.dom.minidom
from xml.dom.minidom import parse, parseString
class MyListener(object):
            while 1:
                #Open DB connection (change as required)
                db = MySQLdb.connect("sql8.freesqldatabase.com","sql8116670","u47HNmCYr8","sql8116670")
                cursor = db.cursor()

                #Prepare information to be insered
                sql = "(SELECT * FROM TRAINS ORDER BY TME LIMIT 1)"
                #Commit changes to database
                try:
                    #("select freq from matrix_brown where a_id in (?) and b_id in (?)", (b_item_id,b_after_id))
                    #print "Starting Execute"
                    cursor.execute(sql)
                    #print "Passed Execute"
                    results = cursor.fetchall()
                    #countera = countera  + 1
                    for row in results:
                        t = row[0]

                    t1 = datetime.strptime(t, "%H:%M:%S")
                    t2 = strftime("%H:%M:%S", gmtime())
                    t4 = datetime.strptime(t2, "%H:%M:%S")
                    t3 = t4 - t1
                    print t3
                    print t3.seconds
                    #print countera
                    #print "Written to Database"
                except Exception,e:
                    print e
                    db.rollback()
                    #print "Failed to Write to Database"
                db.close()
                pass
        #skip if nothing found in ns3:arrived/delayed attribute        
                #print XML
