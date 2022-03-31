#!/usr/bin/env python2

import rospy
import numpy as np
import cv2  # OpenCV module

import message_filters
from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge, CvBridgeError

class Detect_depth():
    def __init__(self):

        self.cv_bridge = CvBridge()

        # Subscriber
        self.left_hsv_result_sub = message_filters.Subscriber('/predict/hsv_result/left', Image)
        self.right_hsv_result_sub = message_filters.Subscriber('/predict/hsv_result/right', Image)
        self.depth_sub = message_filters.Subscriber('/dreamvu/pal/get/depth', Image)

        self.ts = message_filters.TimeSynchronizer([self.left_hsv_result_sub, self.right_hsv_result_sub, self.depth_sub], 10)
        self.ts.registerCallback(self.callback)
    
    def callback(self, left_hsv_result, right_hsv_result, depth):

        cv_left_hsv_mask = self.cv_bridge.imgmsg_to_cv2(left_hsv_result, desired_encoding="passthrough")
        cv_right_hsv_mask = self.cv_bridge.imgmsg_to_cv2(right_hsv_result, desired_encoding="passthrough")
        cv_depth = self.cv_bridge.imgmsg_to_cv2(depth, desired_encoding="32FC1")

        num_nonzero_pixel = np.count_nonzero(cv_left_hsv_mask)
        # print("num_nonzero_pizel = {}".format(num_nonzero_pixel))
        
        if num_nonzero_pixel >= 500:
            avg_dist = np.mean(cv_depth[np.nonzero(cv_left_hsv_mask)])
            print("Avg_dist = {} ".format(avg_dist))


if __name__=="__main__":
    rospy.init_node("depth_detection_node", anonymous=True)
    Detect_depth = Detect_depth()
    rospy.spin()