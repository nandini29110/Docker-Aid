#!/usr/bin/python3.6
print ("content type: text/html\n\n");
print ("");
import os
os.system("echo 'hey there script is running' >> /root/Desktop/demo.txt")
print ("<html><head><title>CGI</title></head><body>");
print ("hello-cgi");
print ("</body>");
print ("</html>");

