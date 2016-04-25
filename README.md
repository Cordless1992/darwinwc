README - DarwinWC V0.1b

"DarwinWC" is a work in progress which is aimed at finding train services which are not moving. The main purpose of "DarwinWC" is to be a backend data collecter, which can then be used for other purposes.


Quick Start -
On Windows download .zip, extract and then just click run.bat.

Current Status - Ongoing (Status: B)

1. Only show 1 UID per message
2. Only show location where train is set to delayed

Pre-install Requirements
https://pypi.python.org/pypi/MySQL-python/1.2.5 - MySQLdb

Added Files
--------------
Untitled2.py - The base elements of retrieving the oldest item in the database and checking it against a set amount of time then delete it if it is over the set time. Currently this only displays the difference in seconds and does nothing with the data

Removed Files
--------------
None

Edited Files
--------------
Untitled1.py - Added Time of message received

Other Changes
--------------
Test completed for amount of data stored see test notes