FROM ubuntu:18.04
# upgrade the system
ENV DEBIAN_FRONTEND=noninteractive
ENV DEBIAN_PRIORITY=critical
RUN apt-get -qy update \
	&& apt-get -qy -o "Dpkg::Options::=--force-confdef" -o "Dpkg::Options::=--force-confold" upgrade \
	&& apt-get -qy autoclean \
	&& apt-get -qy install --no-install-recommends python3-minimal python3-pip \
	&& rm -rf /var/lib/apt/lists/*
# add user and switch to it
RUN useradd -u 1000 -ms /bin/bash user
USER 1000
WORKDIR /home/user
ENV PATH="/home/user/.local/bin:${PATH}"
RUN pip3 install --no-cache-dir --upgrade --user pip
RUN pip3 install --no-cache-dir --user pyinstaller
# now get the code and build it
ADD current.tar.gz /home/user/pyflexebs
USER 0
RUN chown -R user:user pyflexebs
USER 1000
# go into the folder
WORKDIR /home/user/pyflexebs
# install deps for the code
RUN pip3 install --no-cache-dir --user .
RUN pyinstaller pyflexebs.spec
# if running then run shell
CMD ["/bin/bash"]
