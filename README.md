#Welcome

#Requirements
Docker: version 1.8.2+
docker image: centos:7 (docker pull centos:7)



test cmd:
curl -C 2 -L -O http://host_ip:8766/pro_dir/sent_test

#Build
http_server:
cd ./http_server
docker build -t http_server .
docker run --rm -id -p host_ip:8766:5000 --name http_server http_server

http_agent:
cd ./http_agent
docker build -t http_agent .
docker run --rm -id -p host_ip:8765:5000 --name http_agent http_agent

