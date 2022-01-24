FROM nvidia/cuda:11.1-cudnn8-devel-ubuntu20.04

ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV ROS_DISTRO foxy

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
    gfortran \
    libcanberra-gtk-module \
    libcanberra-gtk3-module \
    libatlas-base-dev \
    libpcap-dev \
    libpng-dev \
    libjpeg-dev \
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
    libpython3-dev \
    # python-gtk2 \
    python-gobject \
    python-tk \
    python3.8-dev \
    python3-venv \
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
    absl-py==0.12.0 \
    appdirs==1.4.4 \
    argcomplete==1.12.3 \
    astunparse==1.6.3 \
    attrs==20.3.0 \
    cachetools==4.2.2 \
    catkin-pkg==0.4.23 \
    certifi==2020.12.5 \
    chardet==4.0.0 \
    cloudpickle==1.6.0 \
    colcon-argcomplete==0.3.3 \
    colcon-bash==0.4.2 \
    colcon-cd==0.1.1 \
    colcon-cmake==0.2.26 \
    colcon-common-extensions==0.2.1 \
    colcon-core==0.6.1 \
    colcon-defaults==0.2.5 \
    colcon-devtools==0.2.2 \
    colcon-library-path==0.2.1 \
    colcon-metadata==0.2.5 \
    colcon-notification==0.2.13 \
    colcon-output==0.2.12 \
    colcon-package-information==0.3.3 \
    colcon-package-selection==0.2.10 \
    colcon-parallel-executor==0.2.4 \
    colcon-pkg-config==0.1.0 \
    colcon-powershell==0.3.6 \
    colcon-python-setup-py==0.2.7 \
    colcon-recursive-crawl==0.2.1 \
    colcon-ros==0.3.21 \
    colcon-test-result==0.3.8 \
    colcon-zsh==0.4.0 \
    coverage==5.5 \
    cycler==0.10.0 \
    Cython==0.29.23 \
    dataclasses==0.6 \
    decorator==4.4.2 \
    distlib==0.3.1 \
    dm-tree==0.1.6 \
    docutils==0.17.1 \
    empy \
    fire==0.4.0 \
    flatbuffers==1.12 \
    gast==0.3.3 \
    geffnet==1.0.0 \
    glog==0.3.1 \
    google-auth==1.30.0 \
    google-auth-oauthlib==0.4.4 \
    google-pasta==0.2.0 \
    grpcio==1.32.0 \
    h5py==2.10.0 \
    idna==2.10 \
    imageio==2.9.0 \
    importlib-metadata==4.0.1 \
    iniconfig==1.1.1 \
    joblib==1.0.1 \
    Keras-Preprocessing==1.1.2 \
    kiwisolver==1.3.1 \
    lark==0.11.3 \
    lxml==4.6.3 \
    Mako==1.1.4 \
    Markdown==3.3.4 \
    MarkupSafe==1.1.1 \
    matplotlib==3.4.1 \
    munch==2.5.0 \
    networkx==2.5.1 \
    neural-structured-learning==1.3.1 \
    notify2==0.3.1 \
    numpy==1.19.5 \
    oauthlib==3.1.0 \
    onnx==1.9.0 \
    onnxruntime==1.7.0 \
    opencv-python==4.5.1.48 \
    opencv-python-headless==4.5.1.48 \
    opt-einsum==3.3.0 \
    packaging==20.9 \
    Pillow==8.2.0 \
    # pkg-resources==0.0.0 \
    pluggy==0.13.1 \
    pretrainedmodels==0.7.4 \
    protobuf==3.15.8 \
    py==1.10.0 \
    pyasn1==0.4.8 \
    pyasn1-modules==0.2.8 \
    pyparsing==2.4.7 \
    pytest==6.2.4 \
    pytest-cov==2.11.1 \
    pytest-repeat==0.9.1 \
    pytest-rerunfailures==9.1.1 \
    python-dateutil==2.8.1 \
    python-gflags==3.1.2 \
    pytools==2021.2.6 \
    PyWavelets==1.1.1 \
    PyYAML==5.4.1 \
    requests==2.25.1 \
    requests-oauthlib==1.3.0 \
    rsa==4.7.2 \
    scikit-image==0.18.1 \
    scipy==1.6.3 \
    six==1.15.0 \
    tensorboard==2.5.0 \
    tensorboard-data-server==0.6.0 \
    tensorboard-plugin-wit==1.8.0 \
    tensorboardX==2.2 \
    tensorflow==2.4.1 \
    tensorflow-addons==0.12.1 \
    tensorflow-estimator==2.4.0 \
    tensorflow-hub==0.12.0 \
    tensorflow-model-optimization==0.5.0 \
    termcolor==1.1.0 \
    tifffile==2021.4.8 \
    toml==0.10.2 \
    torch==1.8.1 \
    torchsummary==1.5.1 \
    torchvision==0.9.1 \
    tqdm==4.60.0 \
    typeguard==2.12.0 \
    typing-extensions==3.7.4.3 \
    urllib3==1.26.4 \
    Werkzeug==1.0.1 \
    wget==3.2 \
    wrapt==1.12.1 \
    zipp==3.4.1

###################################### ROS #####################################

RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg

RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

RUN apt-get -o Acquire::ForceIPv4=true update && apt-get -o Acquire::ForceIPv4=true install --no-install-recommends -y \
    ros-$ROS_DISTRO-desktop \
    ros-$ROS_DISTRO-ros-base \
    python3-colcon-common-extensions \
    python3-rosdep

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
RUN gdown --id 1FFtwL4EGfWl5w8nJZ5WZzMoISyg0OHda -O camera_data.zip \
    && unzip camera_data.zip \
    && cp camera_data/dualenet.onnx /usr/local/bin/ \
    && cp camera_data/depth*.bin /usr/local/bin/ \
    && cp -r camera_data/data/ /usr/local/bin/ \
    && rm camera_data.zip

RUN gdown --id 1s1Ph1oCzJDUFluXePc89aUqLE7ucu2yl -O PAL_lib.zip \
    && unzip PAL_lib.zip \
    && rm PAL_lib.zip

RUN echo "KERNEL==\"video*\", SUBSYSTEMS==\"usb\", ATTRS{idVendor}==\"2560\", ATTR{index}==\"0\", ATTRS{manufacturer}==\"e-con systems\", SYMLINK+=\"pal5\"" 1> /etc/udev/rules.d/pal5.rules
RUN echo "export LD_LIBRARY_PATH=$"LD_LIBRARY_PATH":/PAL_lib" >> ${HOME}/.bashrc

RUN chown -R ${USER}:${USER} ${HOME}/
RUN chown -R ${USER}:${USER} /usr/local/bin/depth*.bin /usr/local/bin/dualenet.onnx /usr/local/bin/data/*/*.png
RUN echo "${USER} ALL=(ALL)  ALL" >> /etc/sudoers

# Support of nvidia-docker 2.0
ENV NVIDIA_VISIBLE_DEVICES=all
ENV NVIDIA_DRIVER_CAPABILITIES=all

WORKDIR ${HOME}