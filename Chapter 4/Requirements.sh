#! /bin/bash
# Author: Rudolph Ponce
# Must Run This As Root It Will Install The Need Programs to
# Run Some Of These Code

# This will install the need packages
apt-get install python-opencv python-numpy python-scipy -y
wget http://eclecti.cc/files/2008/03/haarcascade_frontalface_alt.xml

# This will create the need directories for pic_carver.py
mkdir pictures
mkdir faces