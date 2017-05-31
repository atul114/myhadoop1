#!/usr/bin/python2
import  cgi
import time
import commands
import os

print  "content-type:text/html"
print  ""
data=cgi.FieldStorage()
print data
yyy='''
<head>
  <title>List of services provided : </title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="/static/c1.css">
  <script src="/static/j2.js"></script>
  <script src="/static/j3.js"></script>
</head>
<body>
<div class="container">
<h2>YOUR OPTIONS ARE:-</h2>
<p>Choose the desired</p>
'''
print yyy
g=open('nameip','r')
pi=g.read()
g.close()
print"namenode"
print pi
g=open('/var/www/html/loc','r')
loc=g.read().splitlines()
g.close()


#print commands.getoutput(" sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@" +pi+' sudo hadoop fs -mkdir /sample')
print '<pre>'
print commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+pi+' sudo hadoop fs -Ddfs.replication='+loc[1]+' -Ddfs.block.size='+loc[2]+' -put '+loc[0]+' '+loc[3])
print '</pre>'
print '<form method="post" action="/cgi-bin/check4.py">'
print '<label><input type="submit" value="Click to perform more"></label>'
print '</form>'





