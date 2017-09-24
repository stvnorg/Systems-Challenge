FROM centos:latest
MAINTAINER Steven Stevanus - stvn.org@gmail.com
RUN yum update -y
RUN yum install -y epel-release
RUN yum install -y net-tools
RUN yum install -y glibc-devel glibc-headers gcc
RUN yum install -y python-devel
RUN yum install -y python-pip
RUN pip install flask
RUN pip install gunicorn
WORKDIR /statusapp
ADD . /statusapp
EXPOSE 8080
CMD ["./install.sh"]

