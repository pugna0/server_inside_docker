FROM centos:7
MAINTAINER pugna

RUN yum install -y epel-release
RUN yum install -y python-devel
RUN yum install -y libcurl-devel


ENV PUGNA_DIR /pro_dir
COPY . $PUGNA_DIR
WORKDIR ${PUGNA_DIR}

EXPOSE 5000

ENTRYPOINT python /pro_dir/python http_server.py



