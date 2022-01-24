#! /bin/bash

source /opt/ros/foxy/setup.bash

cd dev_ws/
colcon build --cmake-clean-cache
cd ..
