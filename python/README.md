Setup:
======

1)Save librublak.py ,rub-login.py in the same folder

2)Save default.conf to your home folder. If you can not save the file in the home folder (you have windows) or you do not want to, save it in the folder of your choosing and edit in the file "rub-login.py" the line   path = os.path.expanduser("~/.rub-loginrc")   to   path = os.path.expanduser("WhateverYouWant/.rub-loginrc")    .

3)Edit default.conf: The file consists of KEY=VALUE pairs. (It's also possible to have a system-wide configuration file named "/etc/rublogin", which is currently not advised, because LoginID and password are stored in plain text.

4)Rename default.conf to ".rub-loginrc" . (or edit the librublak.py file for a custom name)

Usage:
======

On Linux use crontab to execute the python programm every 0-30 minutes (25 is recommended)

       
Requirements:
=============

1)python
