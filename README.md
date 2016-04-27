README - DarwinWC Alpha V0.5

"DarwinWC" is a work in progress which is aimed at finding train services which are not moving. The main purpose of "DarwinWC" is to be a backend data collecter, which can then be used for other purposes.

Quick Start -
For Stable Releases -

On Windows download .zip, extract and then just click 
Run_(Stable).bat
For NEW (Unstable) Releases -

On Windows download .zip, extract and then just click 
Run_BETA_Unstable).bat
For the Database Management (Stable) Release -

On Windows download .zip, extract and then just click 
Run_(Database_Manager).bat

Current Status - Alpha

1. Only show 1 UID per message
2. Only show location where train is set to delayed

Pre-install Requirements
https://pypi.python.org/pypi/MySQL-python/1.2.5 - MySQLdb

Update Notes for update from V0.3 to V0.5
--------------
+1. Changed the format of the time stored to include the date, this will allow for the database management part of the program to work more effceintly with the data stream software.

+2. The database management software will now delete records which are over an hour old (this can be changed).

 3. Further tests are now required to ensure that the database can manage itself over a 24 hour period. 

-4. Removed 'comments.py' as this file is no longer required and was only kept for reference.

-5. Removed 'start.py' as this file is no longer required.

-6. Removed 'setup.py' I am not sure if this is required but will remove from V0.5 and will reintroduce in V0.6 if needed.

Planned for V0.6 onwards
--------------
1. Alter code to retrieve database connection details (hostname, login, password, database name) from a text file so it can easily be changed.

2. Security system - This will be designed to control the usage of the software and is not intended to be implemented until the BETA/Release stage of the project development.
