FROM ubuntu:18.04

ENV THRIFT_VERSION v0.16.0
WORKDIR /root
RUN buildDeps=" \
		automake \
		bison \
		curl \
		flex \
		g++ \
		libboost-dev \
		libboost-filesystem-dev \
		libboost-program-options-dev \
		libboost-system-dev \
		libboost-test-dev \
		libevent-dev \
		libssl-dev \
		libtool \
		make \
		pkg-config \
 		python3-distutils  \
		python3-setuptools \
	"; \
	apt-get update \
	&& apt-get install -y python3 \
	&& apt-get install -y --no-install-recommends $buildDeps  \ 
	&& curl -k -sSL "https://github.com/apache/thrift/archive/${THRIFT_VERSION}.tar.gz" -o thrift.tar.gz \
	&& mkdir -p /usr/src/thrift \
	&& tar zxf thrift.tar.gz -C /usr/src/thrift --strip-components=1 \
	&& rm thrift.tar.gz \
	&& cd /usr/src/thrift \
 	&& apt-get remove python2.7 && apt-get remove python2.7 && apt-get purge python2.7 \
	&& ./bootstrap.sh \
	&& ./configure \
	&& make -j16 \
	&& make install 

RUN apt-get install -y  python3-pip\
&& pip3 install thrift 

RUN cd / \
	&& rm -rf /usr/src/thrift \
	&& apt-get purge -y --auto-remove $buildDeps \
	&& rm -rf /var/lib/apt/lists/* \
	&& rm -rf /var/cache/apt/* \
	&& rm -rf /var/lib/apt/lists/* \
	&& rm -rf /tmp/* \
	&& rm -rf /var/tmp/*

COPY ./run.sh .

COPY ./pythonThriftDemo ./pythonThriftDemo

RUN chmod +x ./run.sh
EXPOSE 8013

