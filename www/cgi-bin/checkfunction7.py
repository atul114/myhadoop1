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
g=open('nameip','r')
pi=g.read()
g.close()
u1=data.getvalue('1')
print u1
print pi
print commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+pi+" sudo hadoop dfsadmin -clrQuota "+u1)
print '<form method="post" action="/cgi-bin/check4.py">'
print '<label><input type="submit" value="Click to perform more"></label>'
print '</form>'





