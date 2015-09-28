FROM centos:7
MAINTAINER pugna

RUN yum install python
RUN yum install pip
RUN yum install python-devel
RUN yum install libcurl4-gnutls-devel
RUN pip install pycurl
#RUN pip install -r file

COPY . /pro_dir
WORKDIR /pro_dir

ENTRYPOINT python /pro_dir/python xx.py


#docker build .
#docker run -id centos:7
