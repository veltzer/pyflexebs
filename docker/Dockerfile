FROM ubuntu:18.04
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y python3-minimal python3-pip
RUN useradd -ms /bin/bash user
# change to user
USER user
WORKDIR /home/user
ENV PATH="/home/user/.local/bin:${PATH}"
RUN pip3 install --user pyinstaller
RUN pip3 install --upgrade --user pip
# now get the code and build it
ADD --chown=user:user current.tar.gz /home/user
RUN tar xf current.tar.gz
WORKDIR pyflexebs
# install deps for the code
RUN pip3 install --user .
RUN pyinstaller pyflexebs.spec
# run shell
ADD --chown=user:user pyinstaller_docker/inside.sh /home/user/inside.sh
CMD ["/bin/bash", "inside.sh"]
