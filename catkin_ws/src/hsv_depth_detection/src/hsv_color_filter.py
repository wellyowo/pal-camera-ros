#!/usr/bin/env python2

import rospy
import numpy as np
import cv2  # OpenCV module

from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge, CvBridgeError

class HSV_color_filter():
    def __init__(self):

        self.cv_bridge = CvBridge()

        # Subscriber
        self.left_image_sub = rospy.Subscriber('/dreamvu/pal/get/left', Image, self.left_rgb_cb)
        self.right_image_sub = rospy.Subscriber('/dreamvu/pal/get/right', Image, self.right_rgb_cb)

        ## Publisher for predict result and mask
        self.left_hsv_result = rospy.Publisher("/predict/hsv_result/left", Image, queue_size=10)
        self.right_hsv_result = rospy.Publisher("/predict/hsv_result/right", Image, queue_size=10)


    def left_rgb_cb(self, data):

        cv_image = self.cv_bridge.imgmsg_to_cv2(data, "bgr8")

        blurred_image = cv2.GaussianBlur(cv_image, (5, 5), 0)
        hsv = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2HSV)

        # detect red
        lower_red = np.array([0, 100, 50])
        upper_red = np.array([5, 255, 255])
        mask = cv2.inRange(hsv, lower_red, upper_red)	

        self.left_hsv_result.publish(self.cv_bridge.cv2_to_imgmsg(mask, encoding="passthrough"))

    def right_rgb_cb(self, data):

        cv_image = self.cv_bridge.imgmsg_to_cv2(data, "bgr8")

        blurred_image = cv2.GaussianBlur(cv_image, (5, 5), 0)
        hsv = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2HSV)

        # detect red
        lower_red = np.array([0, 100, 50])
        upper_red = np.array([5, 255, 255])
        mask = cv2.inRange(hsv, lower_red, upper_red)	

        self.right_hsv_result.publish(self.cv_bridge.cv2_to_imgmsg(mask, encoding="passthrough"))

if __name__=="__main__":
    rospy.init_node("hsv_color_filter_node", anonymous=True)
    HSV_color_filter = HSV_color_filter()
    rospy.spin()