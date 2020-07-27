FROM ubuntu:18.04
RUN apt-get install apt-utils
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
ADD current.tar.gz /home/user/pyflexebs
USER root
RUN chown -R user:user pyflexebs
USER user
WORKDIR pyflexebs
# install deps for the code
RUN pip3 install --user .
RUN pyinstaller pyflexebs.spec
CMD ["/bin/bash"]
