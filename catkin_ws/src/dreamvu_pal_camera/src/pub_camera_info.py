#!/usr/bin/env python

import rospy
from sensor_msgs.msg import CameraInfo

def load_camera_info():
    
    k1 = -0.225495 # distortion_coefficients of the pal camera
    k2 = -0.363048
    k3 = -0.000477994
    p1 = -0.000132753
    p2 =  0.0

    fy = 1322.0 # camera matrix of the pal camera for resolution 1322x454
    cx =  454.0
    fx = 1322.0  # equal to width
    cy =  454.0  # equal to height

    left_camera_info_msg = CameraInfo()
    left_camera_info_msg.header.frame_id = 'pal_camera_left'
    left_camera_info_msg.distortion_model = 'plumb_bob'
    left_camera_info_msg.width = fx
    left_camera_info_msg.height = cy
    left_camera_info_msg.D = [k1, k2, k3, p1, p2]
    left_camera_info_msg.K = [fx,  0.0, cx, 
                              0.0, fy,  cy, 
                              0.0, 0.0, 1.0]
    left_camera_info_msg.R = [1.0, 0.0, 0.0, 
                              0.0, 1.0, 0.0, 
                              0.0, 0.0, 1.0]
    left_camera_info_msg.P = [fx,  0.0, cx,  0.0,
                              0.0, fy,  cy,  0.0,
                              0.0, 0.0, 1.0, 0.0]

    right_camera_info_msg = CameraInfo()
    right_camera_info_msg.header.frame_id = 'pal_camera_right'
    right_camera_info_msg.distortion_model = 'plumb_bob'
    right_camera_info_msg.width = fx
    right_camera_info_msg.height = cy
    right_camera_info_msg.D = [k1, k2, k3, p1, p2]
    right_camera_info_msg.K = [fx,  0.0, cx, 
                               0.0, fy,  cy, 
                               0.0, 0.0, 1.0]
    right_camera_info_msg.R = [1.0, 0.0, 0.0, 
                               0.0, 1.0, 0.0, 
                               0.0, 0.0, 1.0]
    right_camera_info_msg.P = [fx,  0.0, cx,  0.0,
                               0.0, fy,  cy,  0.0,
                               0.0, 0.0, 1.0, 0.0]

    return left_camera_info_msg, right_camera_info_msg

if __name__ == '__main__':
    rospy.init_node('pub_camera_info', anonymous=True)
    left_camera_info_pub = rospy.Publisher('/dreamvu/pal/get/camera_info', CameraInfo, queue_size=15)
    # right_camera_info_pub = rospy.Publisher('/dreamvu/pal/get/right/camera_info', CameraInfo, queue_size=15)
    rate = rospy.Rate(10) # 10hz

    left_camera_info_msg, right_camera_info_msg = load_camera_info()

    while not rospy.is_shutdown():
        left_camera_info_pub.publish(left_camera_info_msg)
        # right_camera_info_pub.publish(right_camera_info_msg)
        rate.sleep()