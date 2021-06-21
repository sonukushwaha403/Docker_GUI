#!/usr/bin/python3
import subprocess as sp 
import cgi
print("content-type: text/html")
print()

 
 

cmd= 'sudo docker ps -a' 
 
output=sp.getoutput(cmd)

print(output)
