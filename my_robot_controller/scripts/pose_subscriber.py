#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose

def pose_callback(msg: Pose):
    rospy.loginfo(msg.x + msg.y)

if __name__ == '__main__':
    rospy.init_node("turtle_pose_subscriber")
    rospy.loginfo("Node has been started") 

    sub = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)

    rospy.spin()