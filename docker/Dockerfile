FROM ubuntu:18.04
# upgrade the system
ENV DEBIAN_FRONTEND=noninteractive
ENV DEBIAN_PRIORITY=critical
RUN apt-get -qy update
RUN apt-get -qy -o "Dpkg::Options::=--force-confdef" -o "Dpkg::Options::=--force-confold" upgrade
RUN apt-get -qy autoclean
# we need python
RUN apt-get -qy install python3-minimal python3-pip
# add user and switch to it
RUN useradd -ms /bin/bash user
USER user
WORKDIR /home/user
ENV PATH="/home/user/.local/bin:${PATH}"
RUN pip3 install --upgrade --user pip
RUN pip3 install --user pyinstaller
# now get the code and build it
ADD current.tar.gz /home/user/pyflexebs
USER root
RUN chown -R user:user pyflexebs
USER user
# go into the folder
WORKDIR pyflexebs
# install deps for the code
RUN pip3 install --user .
RUN pyinstaller pyflexebs.spec
# if running then run shell
CMD ["/bin/bash"]
