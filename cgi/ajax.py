#!/usr/bin/python3
import subprocess as sp 
import cgi
print("content-type: text/html")
print()
'''
a=cgi.FieldStorage()
osname=a.getvalue("y")
'''
b=cgi.FieldStorage()
osimage=b.getvalue("x")

'''cmd= 'sudo docker run -d -it --name {} {}'.format(osname,osimage)'''
cmd= 'sudo docker run -d -it  {}'.format(osimage)
output=sp.getoutput(cmd)
print(output)
'''status=output[0]
out=output[1]
if status ==0 :
    print ("os launched with name {}".format(osname))
    print ("os launched with the image called {}".format(osimage))
else:
    print("some error occured : {}".format(out))
'''
