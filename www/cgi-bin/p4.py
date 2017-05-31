#!/usr/bin/python2
import  cgi
import time
import commands
import os

print  "content-type:text/html"
print  ""

ik='192.168.10.102'
#print commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no  "+ik+" yum  install  ftp://192.168.10.102/pub/jdk-7u79-linux-x64.rpm -y")
print "<pre>"
#print "hello"
#print commands.getoutput(" sshpass -p 'q' ssh -o StrictHostKeyChecking=no  root@"+ik+" sudo yum  install  ftp://192.168.10.102/pub/jdk-7u79-linux-x64.rpm -y")

#print "dhsuh"
print commands.getoutput(" sshpass -p 'q' sudo scp -o StrictHostKeyChecking=no /root/.bashrc  root@"+ik+":/root/ ")
print "</pre>"
