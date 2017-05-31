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
#user=int(data.getvalue('p'))
#print user
f=open('qw','r')
ip=f.read().splitlines()
print  ip

#i=user
#pi=ip[user-1]
g=open('nameip','r')
pi=g.read()
g.close()
print"namenode"
print pi

user1=int(data.getvalue('op'))
print user1
flag=True
#making a sample directory
def one():
	print '<pre>'
	print commands.getoutput(" sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@" +pi+' sudo hadoop fs -mkdir /sample')
	print '</pre>'

#upload a sample file make and upload
def two():
	a0=raw_input('Enter the name of file to upload:-')
	a00=raw_input('Enter the location to upload:-')
	a1=raw_input('Enter the size of sample file to upload in Mb')
	if(flag==False):
		b2=raw_input('Enter the replication size ')
		b3=raw_input('Enter the block size in bytes ') 
	else:
		b2='3'
		b3='67108864'
	commands.getoutput('ssh root@'+pi+' fallocate -l '+a1+'M '+a0) 
	commands.getoutput('ssh root@'+pi+' hadoop fs -Ddfs.replication='+b2+' -Ddfs.block.size='+b3+' -put '+a0+' '+a00)


#upload an existing file from your own computer
def three(flag):
	a0=raw_input('Enter the location of file to upload:-')
	a00=raw_input('Enter the location to upload:-')
	if(flag==False):
		b2=raw_input('Enter the replication size ')
		b3=raw_input('Enter the block size in bytes ') 
	else:
		b2='3'
		b3='67108864'
	if(flag==False):
		commands.getoutput('ssh root@'+pi+' hadoop fs -Ddfs.replication='+b2+' -Ddfs.block.size='+b3+' -put '+a0+' '+a00)
	else:
		commands.getoutput('ssh root@'+pi+' hadoop fs -put '+a0+' ' +a00)
	flag=True

#go in safe mode

def four():
	#b0=input('Enter the safe interval in seconds ')
	print '<pre>'
	print commands.getoutput(" sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@" +pi+' sudo hadoop dfsadmin -safemode enter')
	print '</pre>'

#set user Quota

def five():
	print "oo"
	print '<form method="post" action="/cgi-bin/checkfunction5.py">'
	print '<b>Enter the number of content a user can upload :</b>'
	print '<label><input type="text" name="1"></label>'
	print '<br><b>Enter the location of the directory whose quota you want to set : </b>'	
	print '<label><input type="text" name="2"></label>'
	print '<label><input type="submit" value="Click to set"></label>'
	print '</form>'
	#print '</body>
	#c0=raw_input('Enter the number of content a user can upload :')
	#c1=raw_input('Enter the location of the directory whose quota you want to set : ')
	#commands.getoutput('ssh root@'+pi+' hadoop dfsadmin -setQuota '+c0+' '+c1)


#set space Quota
def six():
	print "oo"
	print '<form method="post" action="/cgi-bin/checkfunction6.py">'
	print '<b>Enter the space in Mb : </b>'
	print '<label><input type="text" name="1"></label>'
	print '<br><b>Enter the location of the directory whose quota you want to set : </b>'	
	print '<label><input type="text" name="2"></label>'
	print '<label><input type="submit" value="Click to set"></label>'
	print '</form>'
	#c0=raw_input('Enter the space in Mb :')
	#c1=raw_input('Enter the location of the directory whose quota you want to set : ')
	#commands.getoutput('ssh root@'+pi+' hadoop dfsadmin -setSpaceQuota '+c0+'M '+c1)

#clear user Quota
def seven():
	print "oo"
	print '<form method="post" action="/cgi-bin/checkfunction7.py">'
	print '<b>Enter the location of the directory whose quota you want to free : </b>'
	print '<label><input type="text" name="1"></label>'
	print '<label><input type="submit" value="Click to set"></label>'
	print '</form>'
	#c1=raw_input('Enter the location of the directory whose quota you want to free : ')
	#commands.getoutput('ssh root@'+pi+' hadoop dfsadmin -clrQuota '+c1)

#clear space Quota

def eight():
	print "oo"
	print '<form method="post" action="/cgi-bin/checkfunction8.py">'
	print '<b>Enter the location of the directory whose quota you want to free : </b>'
	print '<label><input type="text" name="1"></label>'
	print '<label><input type="submit" value="Click to set"></label>'
	print '</form>'
	#c1=raw_input('Enter the location of the directory whose space quota you want to free : ')
	#commands.getoutput('ssh root@'+pi+' hadoop dfsadmin -clrSpaceQuota '+c1)

#see the Quota that is set
def nine():
	print "oo"
	print '<form method="post" action="/cgi-bin/checkfunction9.py">'
	print '<b>Enter the location of the directory whose quota you want to see :</b>'
	print '<label><input type="text" name="1"></label>'
	print '<label><input type="submit" value="Click to see"></label>'
	print '</form>'
	#c1=raw_input('Enter the location of the directory whose quota you want to see : ')
	#ko=commands.getoutput(' hadoop fs -count -q '+c1)
	
	print ko
#see the uplaoded directories and files
def ten():
	print '<pre>'
	kk=commands.getoutput(" sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@" +pi+' sudo hadoop fs -ls /')
	print kk
	print '</pre>'

#set the replication and block size permanently
def eleven():
	d1=raw_input("Enter the required replication : ")
	d2=raw_input("Enter the required block size in bytes : ")

	y='<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>/'+d+'</value>\n</property>\n<property>\n<name>dfs.replication</name>\n<value>'+d1+'</value>\n</property>\n<property>\n<name>dfs.block.size</name>\n<value>'+d2+'</value>\n</property>\n</configuration>'
	f=open('/tmp/hdfs-site.xml','w')
	f.write(y)
	f.close()
	commands.getoutput('scp   /tmp/hdfs-site.xml   root@'+pi+':/etc/hadoop/hdfs-site.xml')

#set the default values of the replication and block size

def twelve():
	y='<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>/'+d+'</value>\n</property>\n</configuration>'
	f=open('/tmp/hdfs-site.xml','w')
	f.write(y)
	f.close()
	commands.getoutput('scp   /tmp/hdfs-site.xml   root@'+pi+':/etc/hadoop/hdfs-site.xml')

#set flag false

def thirteen():
	flag=False
	three()

#common

def fourteen():
	print 'Press a for uploading with default replication and block'
	print 'Press b for uploading with prev. set replication and block'
	print 'Press c for uploading with run time decision'
	ch=raw_input();
	if(ch=='a'):
		twelve()
		flag=True
		three(flag)
	elif(ch=='b'):
		flag=True
		three(flag)
	elif(ch=='c'):
		flag=False
		three(flag)
		
# leave safe mode

def fifteen():
	print '<pre>'
	print commands.getoutput(" sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@" +pi+' sudo hadoop dfsadmin -safemode leave')
	print '</pre>'

def sixteen():
	print '<pre>'
	print commands.getoutput(" sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@" +pi+' sudo hadoop dfsadmin -report | head -9')
	print '</pre>'
def seventeen():
	print '<meta http-equiv=REFRESH CONTENT=0;url=/phphtml.html>'
	
def eighteen():
	print "oo"
	print '<form method="post" action="/cgi-bin/checkfunction18.py">'
	print '<b>Enter the location with name : </b>'
	print '<label><input type="text" name="1"></label>'
	print '<label><input type="submit" value="Click to set"></label>'
	print '</form>'

#set the heartbeat of the data node
s1=user1
print s1

if(s1==1):
	one()
elif(s1=='2'):
	two()
elif(s1=='3'):
	three()
elif(s1==4):
	four()
elif(s1==5):
	five()
elif(s1==6):
	six()
elif(s1==7):
	seven()
elif(s1==8):
	eight()
elif(s1==9):
	nine()
elif(s1==10):
	ten()
elif(s1=='11'):
	eleven()
elif(s1=='12'):
	twelve()
elif(s1=='13'):
	thirteen()
elif(s1=='14'):
	fourteen()
elif(s1==15):
	fifteen()
elif(s1==16):
	sixteen()
elif(s1==17):
	seventeen()
elif(s1==18):
	eighteen()

print '<form method="post" action="/cgi-bin/check4.py">'
print '<label><input type="submit" value="Click to perform more"></label>'
print '</form>'
print '</body>'
	
