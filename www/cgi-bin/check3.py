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
<h2></h2>
<p></p>
'''
print yyy
user=int(data.getvalue('p'))
print user
l=str(user)
d=data.getvalue(l)
#ip=['192.168.10.102','192.168.10.103']
f=open('qw','r')
ip=f.read().splitlines()
print  ip

i=user
pi=ip[user-1]
print"namenode"
print pi

print d
print "<pre>"
flag=True
for ik in ip:
	
	# installing JDK 
	print "------------------------------------------INSTALLING JDK    : "+ik+"-------------------------------------------------------"
	#kk=commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no  "+ik+' yum  install  ftp://192.168.10.102/pub/jdk-7u79-linux-x64.rpm -y')
	kk=commands.getoutput(" sshpass -p 'q' ssh -o StrictHostKeyChecking=no  root@"+ik+' sudo yum  install  ftp://192.168.10.102/pub/jdk-7u79-linux-x64.rpm -y')
	print kk
	
	#  Installing  Hadoop 
	print "------------------------------------------INSTALLING HADOOP : "+ik+"----------------------------------------------------"
	print commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+ik+' sudo rpm -ivh  ftp://192.168.10.102/pub/hadoop-1.2.1-1.x86_64.rpm  --replacefiles')

	#  setting  JAVA PATH
	print "------------------------------------------SETTING JAVA PATH : "+ik+"----------------------------------------------------"
	print commands.getoutput(" sshpass -p 'q' sudo scp -o StrictHostKeyChecking=no /root/.bashrc  root@"+ik+":/root/ ")
	
	# setting  core-site.xml 
	print "------------------------------------------SETTING CORE_SITE : "+ik+"-----------------------------------------------------"
	x='<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://'+pi+':10001</value>\n</property>\n</configuration>'

	f=open('/tmp/core-site.xml','w')
	f.write(x)
	f.close()
	#print commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+ik+' sudo scp   /tmp/core-site.xml   root@'+ik+':/etc/hadoop/core-site.xml')
	print commands.getoutput(" sshpass -p 'q' sudo scp -o StrictHostKeyChecking=no /tmp/core-site.xml  root@"+ik+":/etc/hadoop/core-site.xml ")
	
#  configure  hdfs-site.xml for  namenode 
print "-------------------------------------------------SETTING HDFS_SITE : "+pi+"------------------------------------------------------"
y='<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>/'+d+'</value>\n</property>\n</configuration>'


f=open('/tmp/hdfs-site.xml','w')
f.write(y)
f.close()
commands.getoutput("sshpass -p 'q' sudo scp -o StrictHostKeyChecking=no /tmp/hdfs-site.xml root@"+pi+":/etc/hadoop/hdfs-site.xml")
commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+pi+' sudo hadoop namenode  -format')
commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+pi+' sudo hadoop-daemon.sh start  namenode')
commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+pi+' sudo jps')


#  setting  up  data  node IPS  

print   "-------------------------------plz wait for a moment  we are making  requirement for data node --------------------------------------"
#time.sleep(2)

dnip=ip
'''
ll=-1
mn=0
for kk in ip:
	ll=ll+1
	u=ip[ll]
	if(u==pi):
		mn=ll
		break
ip.pop(mn)
print dnip
'''
print  "-----------------------------------------------------setting up  datanode  : -----------------------------------------------------"

#  creating  datanode  hdfs-site.xml
ll=1
print "user"
print user
for j in dnip:
	if(ll==user):
		ll=ll+1
	else:
		dnd=data.getvalue(str(ll))
		print dnd
		print "SETTING HDFS_SITE : "+j
		z='<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in thisfile. -->\n<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>/'+dnd+'</value>\n</property>\n</configuration>'
		f=open('/tmp/hdfsdn-site.xml','w')
		f.write(z)
		f.close()
		commands.getoutput("sshpass -p 'q' sudo scp -o StrictHostKeyChecking=no /tmp/hdfsdn-site.xml root@"+j+":/etc/hadoop/hdfs-site.xml")
		print commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+j+' sudo hadoop-daemon.sh start datanode')
		print commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+j+' sudo jps')
		ll=ll+1

# showing details of nodes 

commands.getoutput('ssh '+pi+' firefox '+pi+':50070')

print '</pre>'
print '<h2>CLUSTER SETUP SUCCESSFUL!!</h2>'
print '<form method="post" action="/cgi-bin/check4.py">'
print '<div>'
print '<label><input type="submit" value="Click to start uploading files in cluster "></label>'
print '</div>'
print "<input type ='hidden' name='p' value="+str(user)+">"
print '</form>'
#making a sample directory
def one():
	commands.getoutput('ssh root@'+pi+' hadoop fs -mkdir /sample')

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
	b0=input('Enter the safe interval in seconds ')
	commands.getoutput('ssh root@'+pi+' hadoop dfsadmin -safemode enter')
	time.sleep(b0)
	commands.getoutput('ssh root@'+pi+' hadoop dfsadmin -safemode leave')

#set user Quota

def five():
	c0=raw_input('Enter the number of content a user can upload :')
	c1=raw_input('Enter the location of the directory whose quota you want to set : ')
	commands.getoutput('ssh root@'+pi+' hadoop dfsadmin -setQuota '+c0+' '+c1)


#set space Quota
def six():
	c0=raw_input('Enter the space in Mb :')
	c1=raw_input('Enter the location of the directory whose quota you want to set : ')
	commands.getoutput('ssh root@'+pi+' hadoop dfsadmin -setSpaceQuota '+c0+'M '+c1)

#clear user Quota
def seven():
	c1=raw_input('Enter the location of the directory whose quota you want to free : ')
	commands.getoutput('ssh root@'+pi+' hadoop dfsadmin -clrQuota '+c1)

#clear space Quota

def eight():
	c1=raw_input('Enter the location of the directory whose space quota you want to free : ')
	commands.getoutput('ssh root@'+pi+' hadoop dfsadmin -clrSpaceQuota '+c1)

#see the Quota that is set
def nine():
	c1=raw_input('Enter the location of the directory whose quota you want to see : ')
	ko=commands.getoutput(' hadoop fs -count -q '+c1)
	
	print ko
#see the uplaoded directories and files
def ten():
	kk=commands.getoutput(' hadoop fs -ls /')
	print kk

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
		

#set the heartbeat of the data node

g='''
press 1 for making a sample directory
Press 2 for making and uploading a sample file 
Press 3 for uploading an existing file from your own computer
Press 4 for going in safe mode
Press 5 for setting user Quota
Press 6 for setting space Quota
Press 7 for clearing user Quota
Press 8 for clearing space Quota
Press 9 for seeing the Quota that is set
Press 10 for seeing the uplaoded directories and files
Press 11 to permanently set the replication and block size
Press 12 to change the replication and block to the default values
Press 13 to upload with different replication and block size
Press 14 to upload
Press 0 to exit
'''
q=1
while(q!=0):
	print g
	s1=raw_input("Enter the option : ")
	if(s1=='1'):
		one()
	elif(s1=='2'):
		two()
	elif(s1=='3'):
		three()
	elif(s1=='4'):
		four()
	elif(s1=='5'):
		five()
	elif(s1=='6'):
		six()
	elif(s1=='7'):
		seven()
	elif(s1=='8'):
		eight()
	elif(s1=='9'):
		nine()
	elif(s1=='10'):
		ten()
	elif(s1=='11'):
		eleven()
	elif(s1=='12'):
		twelve()
	elif(s1=='13'):
		thirteen()
	elif(s1=='14'):
		fourteen()
	else:
		q=0

print "</pre>"


















