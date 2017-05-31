#!/usr/bin/python

import  os,commands

l=[]
dict={}
for  i  in  range(150)[100:]  :
	
	x=os.system('arping  -I br0  -c 1  192.168.10.'+str(i) +'&>/dev/null')
	#print i
	#print x
	if x == 0:
		print i
		l.append( "192.168.10."+str(i))
		ss=int(commands.getoutput('cat /proc/meminfo | head -1 | cut -d" " -f9'))
		dict[ss]="192.168.10."+str(i)


a1=dict.keys()
a1.sort(reverse=True)
a2=a1[0]
print a2
print dict[(a2)]

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

