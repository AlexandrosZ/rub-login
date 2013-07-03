#!/bin/bash

username=YourUsername #Replace "YourUsername" with your username
password=YourPassword #Replace "YourPassword" with your password

wget -q --post-data 'loginid='"$username"'&password='"$password"'&action=Login' https://login.rz.ruhr-uni-bochum.de/cgi-bin/laklogin -O tmplogin

reply=$(grep "Authentisierung gelungen" tmplogin)
if [ "$reply" ]; then
	echo "Logged in succesfully"
else
	echo "Login failed, check your username/password"
fi

