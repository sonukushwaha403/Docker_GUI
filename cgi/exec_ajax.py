#!/usr/bin/python3
import subprocess as sp 
import cgi
print("content-type: text/html")
print()

 

b=cgi.FieldStorage()
osname=b.getvalue("x")

cmd= 'sudo docker exec -it {} bash '.format(osname)
 
output=sp.getstatusoutput(cmd)
status=output[0]
out=output[1]
if status ==0 :
    o= (" Inside the os  with name {}".format(osname))
    
else:
    o =("some error occured : {}".format(out))
print(o)
