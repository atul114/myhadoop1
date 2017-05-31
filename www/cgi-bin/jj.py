#!/usr/bin/python2
import cgi
import commands
print  "content-type:text/html"
print  ""

ik='192.168.10.103'
y=commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no  "+ik+" yum  install  ftp://192.168.10.102/pub/jdk-7u79-linux-x64.rpm -y")
print y
#commands.getoutput(' yum  install  ftp://192.168.10.102/pub/jdk-7u79-linux-x64.rpm -y')

