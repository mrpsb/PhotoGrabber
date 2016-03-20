#!/bin/bash
pkill fbi
fbi -a -T 2 -t 30 -u -noverbose -d /dev/fb0 /home/pi/Pictures/*

