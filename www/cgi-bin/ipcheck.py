#!/usr/bin/python

import  cgi
import time
import commands
import os
import collections

print  "content-type:text/html"
print  ""
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
l=[]
dict={}
f=open('qw','w')
aq=0
for  i  in  range(110)[100:]:
	x=os.system('arping  -I eno1  -c 1  192.168.10.'+str(i) +'&>/dev/null')
	#print i
	#print x
	if x == 0:
		print i
		aq=aq+1
		l.append( "192.168.10."+str(i))
		ss=int(commands.getoutput('cat /proc/meminfo | head -1 | cut -d" " -f9'))
		kk="192.168.10."+str(i)
		dict[kk]=ss
		print dict 
		f.write(kk)
		f.write("\n")

f.close()
print dict
print "lklk"
a1=dict.values()
a1.sort(reverse=True)
a2=a1[0]
a11=dict.keys()
print "hh"
print '<h2><b>YOUR NAMENODE IS </b>:   '+a11[0]+'</h2>'
print '<br>'
j=0
print "length"
print aq
print "<form name='gg' method='post' action='/cgi-bin/check3.py' >"
for i in range(0,aq):
	j=j+1
	print '<div class="radio">'
	if(i==0):
		print "<b>Enter the name of directory of namenode</b>("+a11[i]+")&nbsp&nbsp:&nbsp<label><input type='text' name="+str(j)+"><label><b></b></br>"
	else:
		print "<b>Enter the name of directory of datanode</b>&nbsp ("+a11[i]+")&nbsp&nbsp:&nbsp<label><input type='text' name="+str(j)+"><label><b></b></br>"
	print '</div>'
print "<input type ='hidden' name='p' value="+str(1)+">"
print "<input type ='submit' value='submit'>"
print "</form>"





'''
#print 'asd'
print dict.values()
#print 'zxc'
print dict.keys()
#print 'ksah'
ss= dict
ss[5245]='192.168.10.107'
dict=ss
print dict
dpp=[]
fr=dict.keys()
fr.sort(reverse=True)
aq=fr[0]
print aq
print sorted(dict.keys())
aa=dict.keys()[0]
print aa
print l
print dict[aq]
'''

