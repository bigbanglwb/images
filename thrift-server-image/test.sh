docker stop demo
docker rm demo 
docker run -it --name=demo thrift-server:v1 /bin/bash 
