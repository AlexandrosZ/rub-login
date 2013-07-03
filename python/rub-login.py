#!/usr/bin/env python
# -*- coding: utf-8 -*-
#    CLI Lock-and-Key (LaK) automation script for the Ruhr-University
#    of Bochum
#    Original Author: (c) 2010 by Jan Holthuis <jan.holthuis@ruhr-uni-bochum.de>
#    Modified by: https://github.com/AlexandrosZ
#
#    This file is part of the "rub-login"-project.
#
#    rub-login is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    rub-login is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with rub-login.  If not, see <http://www.gnu.org/licenses/>.


# Define Lock-and-Key (LaK) credentials here
import sys, os.path, ConfigParser, datetime, librublak
path = os.path.expanduser("~/.rub-loginrc")
if not os.path.isfile(path):
  if os.name != "posix":
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print "%s: No config file found!" % time
    sys.exit(1);
  else:
    path = "/etc/rub-login.conf"
    if not os.path.isfile(path):
      time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      print "%s: No config file found!" % time
      sys.exit(1);

cp = ConfigParser.SafeConfigParser()
cp.read(path)
if not cp.has_section("LoginIDs"):
  time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  print "%s: Section 'LoginIDs' is missing in config file!" % time
  sys.exit(1);
  
creds = cp.items("LoginIDs")

for username, password in creds:
  time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  if librublak.login(username, password):
    print "%s: Login successful with %s!" % (time, username)
    break
  else:
    print "%s: Login failed with %s!" % (time, username)
