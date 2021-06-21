FROM centos
MAINTAINER Sonu Kumar Kushwaha <sksonukushwaha403@gmail.com>
RUN yum install httpd -y 
COPY ./cgi/ /var/www/html/ 
COPY . /var/www/cgi-bin/
WORKDIR /var/www/html/
EXPOSE 80
ENTRYPOINT ["httpd"]
CMD ["-D","FOREGROUND"]
