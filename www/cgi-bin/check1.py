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
<h2>LIST OF AVAILABLE IP's</h2>
<p>SELECT YOUR NAMENODE</p>
'''
print yyy
user=data.getvalue('op')
#print user
j=0
if user=='1':
	print "<form name='gg' method='post' action='/cgi-bin/check2.py' >"
	#ip=['192.168.10.102','192.168.10.103','192.168.10.122','192.168.10.104','192.168.10.109','192.168.10.171']
	f=open('qw','r')
	ip=f.read().splitlines()
	for i in ip:
		j=j+1
		print '<div class="radio">'
		#print j
		print "<label><input type='radio' name='op' value="+str(j)+"><label><b>"+i+"</b></br>"
		print '</div>'
	print "<input type ='submit' value='submit'>"
	print "</form>"
	print "</body>"
	
else:
	execfile('ipcheck.py')












