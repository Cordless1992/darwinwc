import pymssql
import os
from time import gmtime, strftime
import time
from datetime import datetime
from datetime import timedelta
#Naming needs to be changed for this file it is currently Untitled2.py
import xml.dom.minidom
from xml.dom.minidom import parse, parseString
class MyListener(object):
            while 1:
                #Open DB connection (change as required)
                db = pymssql.connect(server='DESKTOP-3G1FB9B\SQLEXPRESS', user='sa', password='9964', database='Osmium')
                cursor = db.cursor()

                #Prepare information to be insered
                #cursor.execute('SELECT c.CustomerID, c.CompanyName,COUNT(soh.SalesOrderID) AS OrderCount FROM SalesLT.Customer AS c LEFT OUTER JOIN SalesLT.SalesOrderHeader AS soh ON c.CustomerID = soh.CustomerID GROUP BY c.CustomerID, c.CompanyName ORDER BY OrderCount DESC;')

                sql = "SELECT TOP 1 * FROM [delayed] Order by [ID] ASC"
                #Commit changes to database
                try:
                    #("select freq from matrix_brown where a_id in (?) and b_id in (?)", (b_item_id,b_after_id))
                    #print "Starting Execute"
                    cursor.execute(sql)
                    #print "Passed Execute"
                    results = cursor.fetchall()
                    if not cursor.rowcount:
                            os.system('cls')
                            print "Database is currently empty, is Einstein.py or Newton.py running."
                            time.sleep(1)
                    #countera = countera  + 1
                    for row in results:
                        t = row[0]
                        x = row[4]
                        y = int(x)
                        t1 = datetime.strptime(t, "%Y-%m-%d %H:%M:%S")
                        t2 = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                        t4 = datetime.strptime(t2, "%Y-%m-%d %H:%M:%S")
                        t3 = t4 - t1
                        if t3.total_seconds() > 3600:
                            sql = "DELETE FROM delayed WHERE ID=%s"
                            cursor.execute(sql, (y,))
                            db.commit()
                            print "Entry Deleted, Current Difference:", t3
                        else:
                            print "Not Enough Time Current Difference:", t3
                            time.sleep(1)
                        if not cursor.rowcount:
                            os.system('cls')
                            print "Database is currently empty, is Einstein.py or Newton.py running."
                    #print countera
                    #print "Written to Database"
                except Exception,e:
                    print e
                    #print "Failed to Write to Database"
                db.close()
                pass
        #skip if nothing found in ns3:arrived/delayed attribute        
                #print XML
