FROM ubuntu:18.04
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y python3-minimal python3-pip git sudo
# add the user
RUN adduser user
RUN echo "user ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/user
RUN chmod 0440 /etc/sudoers.d/user
# change to user
USER user
WORKDIR /home/user
# now do the work
RUN git clone https://github.com/veltzer/pyflexebs
WORKDIR pyflexebs
RUN pip3 install --upgrade --user pip
RUN pip3 install --user . pyinstaller
RUN pyinstaller pyflexebs.spec
# run the build
USER root
WORKDIR /home/user
CMD ["su", "-", "user", "-c", "/bin/bash"]

# WORKDIR /home/user/build
# COPY build /home/user
# CMD ["bash", "build.sh"]
