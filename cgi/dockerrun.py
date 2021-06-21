#!/usr/bin/python3
print("content-type: text/html")
print()
import subprocess as sp 
import cgi
form=cgi.FieldStorage()
#osname= input("Enter your os name: ")
osname=form.getvalue("x")
osimage=form.getvalue("y")
cmd= 'sudo docker run -d -it --name {} {}'.format(osname,osimage)
output=sp.getstatusoutput(cmd)
status=output[0]
out=output[1]
if status ==0 :
    print ("os launched with name {}".format(osname))
else:
    print("some error occured : {}".format(out))
