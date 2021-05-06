FROM nvidia/cuda:8.0-devel-ubuntu14.04
COPY . /workspace/corner

# HACK to fix handshake error
RUN set -ex
RUN sed -i 's/https/http/g' /etc/apt/sources.list.d/*.list

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget

WORKDIR /workspace

# install miniconda

RUN mkdir -p /miniconda3
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
RUN bash /miniconda3/miniconda.sh -b -u -p /miniconda3
RUN rm -rf /miniconda3/miniconda.sh
RUN /miniconda3/bin/conda init bash
RUN /miniconda3/bin/conda init zsh

RUN conda install pytorch=0.2.0_3 cuda80 -c pytorch

WORKDIR ./corner
RUN sh ./make.sh

