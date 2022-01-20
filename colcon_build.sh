#! /bin/bash

cd dev_ws/
source /opt/ros/foxy/setup.bash
colcon build --cmake-clean-cache
cd ..
