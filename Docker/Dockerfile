FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV ROS_DISTRO melodic

###################################### user #####################################

ENV SHELL=/bin/bash \
    USER=argnctu \
    UID=1000 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8

ENV HOME=/home/${USER}

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${UID} \
    ${USER} 

RUN echo "root:root" | chpasswd
RUN echo "${USER}:111111" | chpasswd

###################################### basic tools #####################################

RUN apt-get -o Acquire::ForceIPv4=true update && apt-get -yq dist-upgrade \
    && apt-get -o Acquire::ForceIPv4=true install -yq --no-install-recommends \
    locales \
    cmake \
    make \
    git \
    vim \
    gedit \
    wget \
    curl \
    unzip \
    sudo \
    lsb-release \
    build-essential \
    net-tools \
    pkg-config \
    dirmngr \
    gnupg2 \
    mercurial \
    xorg \
    g++ \
    libglu1-mesa-dev \
    freeglut3 \
    freeglut3-dev \
    mesa-common-dev \
    qt5-default \
    libcanberra-gtk-module \
    libcanberra-gtk3-module \
    libpcap-dev \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    # libjasper-dev \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
    libv4l-dev \
    libxvidcore-dev \
    libx264-dev \
    libgtk-3-dev \
    libgtk2.0-dev \
    libhdf5-dev \
    libatlas-base-dev \
    gfortran \
    python-gtk2 \
    python-gobject \
    python-tk \
    python3.6-dev \
    python3.6-venv \
    python3-tk \
    python3-pip \
    python3-setuptools \
    python3-opencv \
    python3-numpy \
    python3-empy  \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

##################################### PIP ######################################

RUN pip3 install --upgrade setuptools pip

RUN pip3 install \
    gdown \
    rospkg \
    absl-py==0.11.0 \
    appdirs==1.4.4 \
    astunparse==1.6.3 \
    attrs==20.3.0 \
    cachetools==4.1.1 \
    certifi==2020.6.20 \
    chardet==3.0.4 \
    cloudpickle==1.6.0 \
    cycler==0.10.0 \
    Cython==0.29.21 \
    dataclasses==0.8 \
    decorator==4.4.2 \
    dm-tree==0.1.5 \
    fire==0.3.1 \
    gast==0.3.3 \
    geffnet==1.0.0 \
    glog==0.3.1 \
    google-auth==1.23.0 \
    google-auth-oauthlib==0.4.2 \
    google-pasta==0.2.0 \
    grpcio==1.33.2 \
    h5py==2.10.0 \
    idna==2.10 \
    imageio==2.9.0 \
    importlib-metadata==2.0.0 \
    joblib==0.16.0 \
    kiwisolver==1.2.0 \
    lxml==4.6.1 \
    Mako==1.1.3 \
    Markdown==3.3.3 \
    MarkupSafe==1.1.1 \
    matplotlib==3.2.2 \
    munch==2.5.0 \
    networkx==2.5 \
    neural-structured-learning==1.3.1 \
    numpy==1.17.0 \
    oauthlib==3.1.0 \
    onnx==1.7.0 \
    onnxruntime==1.5.2 \
    opencv-python==4.4.0.44 \
    opencv-python-headless==4.4.0.44 \
    opt-einsum==3.3.0 \
    Pillow==6.1.0 \
    # pkg-resources==0.0.0 \
    pretrainedmodels==0.7.4 \
    protobuf==3.13.0 \
    pyasn1==0.4.8 \
    pyasn1-modules==0.2.8 \
    pyparsing==2.4.7 \
    python-dateutil==2.8.1 \
    python-gflags==3.1.2 \
    pytools==2020.4.3 \
    PyWavelets==1.1.1 \
    PyYAML==5.3.1 \
    requests==2.25.0 \
    requests-oauthlib==1.3.0 \
    rsa==4.6 \
    scikit-image==0.14.5 \
    scipy==1.5.2 \
    six==1.15.0 \
    tensorboard==2.4.0 \
    tensorboard-plugin-wit==1.7.0 \
    tensorboardX==2.1 \
    tensorflow==2.3.1 \
    tensorflow-addons==0.11.2 \
    tensorflow-estimator==2.3.0 \
    tensorflow-hub==0.12.0 \
    tensorflow-model-optimization==0.5.0 \
    termcolor==1.1.0 \
    torch==1.4.0 \
    torchsummary==1.5.1 \
    torchvision==0.5.0 \
    tqdm==4.50.0 \
    typeguard==2.10.0 \
    typing-extensions==3.7.4.3 \
    urllib3==1.26.2 \
    Werkzeug==1.0.1 \
    wget==3.2 \
    wrapt==1.12.1 \
    zipp==3.4.0

###################################### ROS #####################################

RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

RUN apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

RUN apt-get -o Acquire::ForceIPv4=true update && apt-get -o Acquire::ForceIPv4=true install --no-install-recommends -y \
    ros-$ROS_DISTRO-desktop-full \
    python-rosdep \
    python-rosinstall \
    python-rosinstall-generator \
    python-wstool \
    && rm -rf /var/lib/apt/lists/*

RUN rosdep init \
    && rosdep update

##################################### OpenCV ######################################

RUN wget -O opencv.zip https://github.com/opencv/opencv/archive/3.4.4.zip \
    && unzip opencv.zip \
    && rm opencv.zip \
    && mv opencv-3.4.4 opencv

RUN wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/3.4.4.zip \
    && unzip opencv_contrib.zip \
    && rm opencv_contrib.zip \
    && mv opencv_contrib-3.4.4 opencv_contrib

RUN cd opencv/ \
    && mkdir build \
    && cd build \
    && cmake -D CMAKE_BUILD_TYPE=RELEASE \
        -D CMAKE_INSTALL_PREFIX=/usr/local \
        -D INSTALL_PYTHON_EXAMPLES=OFF \
        -D OPENCV_EXTRA_MODULES_PATH=/opencv_contrib/modules \
        -D OPENCV_ENABLE_NONFREE=OFF \
        -D BUILD_EXAMPLES=OFF .. \
    && make -j4 \
    && make install \
    && ldconfig \
    && pkg-config --modversion opencv

##################################### setting ###################################################
RUN gdown --id 1J0_NwNQ02ZLUEPq_yCCMU-bZDfcVoEKE -O camera_data.zip \
    && unzip camera_data.zip \
    && cp camera_data/dualenet.onnx /usr/local/bin/ \
    && cp camera_data/depth*.bin /usr/local/bin/ \
    && cp -r camera_data/data/ /usr/local/bin/ \
    && rm camera_data.zip

RUN gdown --id 1sZWs7M4Q8A-2pPVdR06EgNmW4LbbwwIA -O PAL_lib.zip \
    && unzip PAL_lib.zip \
    && cp PAL_lib/PAL_PYTHON.cpython-36m-x86_64-linux-gnu.so /usr/local/lib/python3.6/dist-packages \
    && rm PAL_lib.zip

RUN echo "${USER} ALL=(ALL)  ALL" >> /etc/sudoers
RUN echo "KERNEL==\"video*\", SUBSYSTEMS==\"usb\", ATTRS{idVendor}==\"2560\", ATTR{index}==\"0\", ATTRS{manufacturer}==\"e-con systems\", SYMLINK+=\"pal5\"" 1> /etc/udev/rules.d/pal5.rules
RUN echo "export LD_LIBRARY_PATH=$"LD_LIBRARY_PATH":/PAL_lib" >> ${HOME}/.bashrc

RUN chown -R ${USER}:${USER} ${HOME}/
RUN chown -R ${USER}:${USER} /usr/local/bin/depth*.bin /usr/local/bin/dualenet.onnx /usr/local/bin/data/*/*.png

RUN ldconfig

# Support of nvidia-docker 2.0
ENV NVIDIA_VISIBLE_DEVICES=all
ENV NVIDIA_DRIVER_CAPABILITIES=all

# setup entrypoint
COPY ./ros_entrypoint.sh /

ENTRYPOINT ["/ros_entrypoint.sh"]

WORKDIR ${HOME}