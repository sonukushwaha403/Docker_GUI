#!/usr/bin/python3
import subprocess as sp 
import cgi
print("content-type: text/html")
print()

a=cgi.FieldStorage()
osname=a.getvalue("y")

b=cgi.FieldStorage()
osimage=b.getvalue("x")

cmd= 'sudo docker run -d -it --name {} {}'.format(osname,osimage)
 
output=sp.getstatusoutput(cmd)
status=output[0]
out=output[1]
if status ==0 :
    o= ("os launched with name {}".format(osname))
    
else:
    o =("some error occured : {}".format(out))
print(o)
