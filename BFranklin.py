import MySQLdb
import os
from time import gmtime, strftime
from datetime import datetime
from datetime import timedelta
#Naming needs to be changed for this file it is currently Untitled2.py
import xml.dom.minidom
from xml.dom.minidom import parse, parseString
class MyListener(object):
            while 1:
                #Open DB connection (change as required)
                db = MySQLdb.connect("localhost","root","","trains")
                cursor = db.cursor()

                #Prepare information to be insered
                sql = "(SELECT * FROM `delayed` ORDER BY `TME` LIMIT 1)"
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
                        x = row[4]

                    y = int(x)
                    t1 = datetime.strptime(t, "%Y-%m-%d %H:%M:%S")
                    t2 = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                    t4 = datetime.strptime(t2, "%Y-%m-%d %H:%M:%S")
                    t3 = t4 - t1
                    print t3
                    print t3.total_seconds()
                    if t3.total_seconds() > 3600:
                        sql = "DELETE FROM 'delayed' WHERE ID=%s"
                        cursor.execute(sql, (y,))
                        db.commit()
                        print "Entry Deleted"
                    else:
                        print "Not Enough Time"
                    #print countera
                    #print "Written to Database"
                except Exception,e:
                    print e
                    #print "Failed to Write to Database"
                db.close()
                pass
        #skip if nothing found in ns3:arrived/delayed attribute        
                #print XML
