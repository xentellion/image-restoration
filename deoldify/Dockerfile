FROM pytorch/pytorch:2.0.0-cuda11.7-cudnn8-devel

ENV NUMEXPR_MAX_THREADS=16

RUN apt update && \
    apt install -y \ 
        git \
        wget \
        unzip \
        libjpeg9 \
        ffmpeg \
        libsm6 \
        libxext6

WORKDIR /
RUN git clone --recurse-submodules https://github.com/jantic/DeOldify.git
WORKDIR /DeOldify

RUN wget https://www.dropbox.com/s/axsd2g85uyixaho/ColorizeStable_gen.pth?dl=0 -O ./models/ColorizeStable_gen.pth
RUN wget https://data.deepai.org/deoldify/ColorizeArtistic_gen.pth -O ./models/ColorizeArtistic_gen.pth

RUN pip install grpcio==1.51.1 grpcio-tools==1.51.1 requests==2.25.1
RUN pip install -r requirements-colab.txt

ADD . ./ 

# ENTRYPOINT ["python", "init.py"]
ENTRYPOINT ["tail", "-f", "/dev/null"]