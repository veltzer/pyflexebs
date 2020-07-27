FROM ubuntu:18.04
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y python3-minimal python3-pip git
RUN pip3 install --upgrade pip
RUN pip3 install pyinstall
RUN git clone https://github.com/veltzer/pyflexebs
WORKDIR pyflexebs
RUN pip3 install .
RUN pyinstaller pyflexebs.spec
COPY build /build
WORKDIR /build
CMD ["bash", "build.sh"]
