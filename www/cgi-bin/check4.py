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
<h2>YOUR OPTIONS ARE:-</h2>
'''
print yyy
f=open('qw','r')
ip=f.read().splitlines()
#print  ip
g=open('nameip','r')
pi=g.read()
g.close()
#print"namenode"
#print pi
print '<b>'
hhh='''
<form method="post" action="/cgi-bin/check5.py">
<div class="radio">
      <label><input type="radio" name="op" value='1'>Select for making a sample directory</label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='18'>Select for making a sample directory in other location of your choice </label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='2'>Select for making and uploading a sample file </label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='3'>Select for uploading an existing file from your own computer </label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='4'>Select for going in safe mode </label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='5'>Select for setting user Quota</label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='6'>Select for setting space Quota</label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='7'>Select for clearing user Quota</label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='8'>Select for clearing space Quota</label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='9'>Select for seeing the Quota that is set</label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='10'>Select for seeing the uplaoded directories and files</label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='11'>Select to permanently set the replication and block size</label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='12'>Select to change the replication and block to the default values</label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='13'>Select to upload with different replication and block size</label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='14'>Select to upload</label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='15'>Select to leave safe mode</label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='0'>Select to exit</label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='16'>Select to see total space</label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='17'>UPLOAD</label>
    </div>
'''
print hhh
print '<label><input type="submit" value="Click to perform"></label>'
#print "<input type ='hidden' name='p' value="+str(user)+">"
print '</form>'
print '</b>'
print '</body>'
