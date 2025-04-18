#!/usr/bin/env bash
set -e

WORKDIR="$1"

# Requirements:
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get install python3.9 python3.9-venv 

if [ ! -d ".venv" ]; then
    echo "Creating .venv"
    python3.9 -m venv .venv
else
    echo ".venv already exists"
fi

source .venv/bin/activate

python3.9 -m pip install --upgrade "pip==20.3.4"
echo "$(python3.9 -m pip3 --version)"

# For mininet
sudo apt-get install mininet
# For ryu
git clone https://github.com/osrg/ryu.git 
cd ryu
pip install -r tools/pip-requires
pip install .
# For dependencies
sudo apt-get install -y --no-install-recommends \
  autoconf \
  automake \
  bison \
  build-essential \
  ca-certificates \
  cmake \
  cpp \
  curl \
  flex \
  git \
  libboost-dev \
  libboost-filesystem-dev \
  libboost-iostreams-dev \
  libboost-program-options-dev \
  libboost-system-dev \
  libboost-test-dev \
  libboost-thread-dev \
  libc6-dev \
  libevent-dev \
  libffi-dev \
  libfl-dev \
  libgc-dev \
  libgc1 \
  libgflags-dev \
  libgmp-dev \
  libgmp10 \
  libgmpxx4ldbl \
  libjudy-dev \
  libpcap-dev \
  libreadline-dev \
  libtool \
  libssl-dev \
  linux-headers-$KERNEL\
  make \
  tcpdump \
  unzip \
  vim \
  wget \
  xcscope-el \
  xterm \
  git \
  mininet \
  openvswitch-switch \
  openvswitch-common \
  vlc

pip install ryu mininet eventlet==0.30.2 networkx matplotlib networkx ipaddr psutil scapy setuptools

deactivate

