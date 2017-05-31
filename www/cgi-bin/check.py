#!/usr/bin/python2
import  cgi

print  "content-type:text/html"
print  ""


data=cgi.FieldStorage()
#print data
user=data.getvalue('firstname')

password=data.getvalue('lastname')
web='''
<html> 
<meta http-equiv=REFRESH CONTENT=1;url=/p1.html>
</html>
'''
qw='''
<html> 
<script> alert("WRONG CREDENTIALS")</script>
<meta http-equiv=REFRESH CONTENT=0;url=/>
</html>
'''
if  user == 'atul'  and  password  == '123' :
        
        print  web
else :
        print   "ERROR PAGE !! "
	print    qw

