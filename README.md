# pal-camera-ros-ubuntu-18.04

This unoffical repo provide a docker container to run [DreamVu PAL_USB camera](https://dreamvu.com/pal-usb/).

## How to run

### Before you start
give your usb video highest permission
$ sudo chmod 777 /dev/video*

### Clone the repo
We use submodule with ssh-key in this repo, so please clone this repo with the command list below.
```
$ git clone --recursive git@github.com:Louis5228/pal-camera-ros.git
```

### Run docker container
```
$ source docker_run.sh
```

### If you want to enter the same docker images
```
$ source docker_join.sh
```

### Compile ROS workspace
```
Docker $ source catkin_make.sh
```

### Init ROS workspace
```
Docker $ source environment.sh
```

### Setup the calibration data for pal_usb (according to your serial number)
* PUM8D210022
```
Docker $ cd PUM8D210022/
Docker $ source setup.sh
```

* PUM8D210024
```
Docker $ cd PUM8D210024/
Docker $ source setup.sh
```

### Launch the PAL camera node
```
Docker $ roslaunch dreamvu_pal_camera pal_rviz.launch use_rviz:=true
```
