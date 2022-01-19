cmake_minimum_required(VERSION 3.5)
project(dreamvu_pal_camera)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic -g)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(cv_bridge REQUIRED)
find_package(image_transport REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(builtin_interfaces REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(rosidl_default_runtime REQUIRED)
find_package(std_msgs REQUIRED)


set(msg_files 
   "msg/BoundingBoxArray.msg"
   "msg/BoundingBox.msg"
)
rosidl_generate_interfaces(
  ${PROJECT_NAME}
  ${msg_files}
  DEPENDENCIES std_msgs
)

set(PAL_INCLUDE_DIR /home/argnctu/pal-camera-ros/dev_ws/src/dreamvu_pal_camera/include )
set(PAL_LIBRARY /home/argnctu/pal-camera-ros/dev_ws/src/dreamvu_pal_camera/lib/libPAL.so /home/argnctu/pal-camera-ros/dev_ws/src/dreamvu_pal_camera/lib/libPAL_CAMERA.so )

include_directories(
  include
  ${rclcpp_INCLUDE_DIRS}
  ${PAL_INCLUDE_DIR}
  ${OpenCV_INCLUDE_DIRS}
)

find_package(PkgConfig REQUIRED)
pkg_search_module(PKG_OPENCV REQUIRED opencv)



add_executable(capture src/pal_camera_node.cpp )
target_link_libraries(capture ${ament_LIBRARIES} ${PKG_OPENCV_LDFLAGS} ${V4l2_LIBRARIES} ${PAL_LIBRARY})
ament_target_dependencies(capture rclcpp image_transport cv_bridge)

add_executable(detect src/person_detection_node.cpp )
target_link_libraries(detect ${ament_LIBRARIES} ${PKG_OPENCV_LDFLAGS} ${V4l2_LIBRARIES} ${PAL_LIBRARY})
ament_target_dependencies(detect rclcpp image_transport cv_bridge)
rosidl_target_interfaces(detect ${PROJECT_NAME} "rosidl_typesupport_cpp")

install(TARGETS
  capture
  detect
  DESTINATION lib/${PROJECT_NAME})


if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()