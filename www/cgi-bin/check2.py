#!/usr/bin/python2
import  cgi
import time
import commands
import os

print  "content-type:text/html"
print  ""
data=cgi.FieldStorage()
#print data
yyy='''
<head>
  <title>List of services provided : </title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="/static/c1.css">
  <script src="/static/j2.js"></script>
  <script src="/static/j3.js"></script>
</head>
<style type="text/css">
body{
background-color: #b0e0e6;
padding 20px;
}
</style>
<body>
<div class="container">
<h2></h2>
<p></p>
'''
print yyy
user=int(data.getvalue('op'))
#ip=['192.168.10.102','192.168.10.103','192.168.10.122','192.168.10.104','192.168.10.109','192.168.10.171']
f=open('qw','r')
ip=f.read().splitlines()
print '<h2><b>YOUR NAMENODE IS </b>:   '+ip[user-1]+'</h2>'
g=open('nameip','w')
g.write(ip[user-1])
g.close()
print '<br>'
j=0
print "<form name='gg' method='post' action='/cgi-bin/check3.py' >"

#ip=['192.168.10.102','192.168.10.103','192.168.10.122','192.168.10.104','192.168.10.109','192.168.10.171']
for i in ip:
	j=j+1
	print '<div class="radio">'
	#print j
	if(i==ip[user-1]):
		print "<b>Enter the name of directory of namenode</b>("+i+")&nbsp&nbsp:&nbsp<label><input type='text' name="+str(j)+"><label><b></b></br>"
	else:
		print "<b>Enter the name of directory of datanode</b>&nbsp ("+i+")&nbsp&nbsp:&nbsp<label><input type='text' name="+str(j)+"><label><b></b></br>"
	print '</div>'
print "<input type ='hidden' name='p' value="+str(user)+">"
print "<input type ='submit' value='Submit'>"
print "</form>"
	


