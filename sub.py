#!/usr/bin/env python

import rospy
from std_msgs.msg import *

def msgCallback(msg):

    print("received message={}".format(msg.data))

    ros_tutorial_pub= rospy.Publisher("topic2",Int64,queue_size=10)

    tutorial_pub= Int64()

    tutorial_pub.data=msg.data+1
    
    print("send_message= {}".format(tutorial_pub.data))
    
    ros_tutorial_pub.publish(tutorial_pub)

if __name__ == "__main__":

    rospy.init_node("topic_subscriber",anonymous=True)

    ros_tutorial_sub = rospy.Subscriber("topic1",Int64,msgCallback,queue_size=10)

    rospy.spin()

