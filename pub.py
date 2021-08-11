#!/usr/bin/env python

import rospy
from std_msgs.msg import *

class msgs:

    def __init__(self):

        self.data=1
    
    def msg_callback(self,msg):


        print("received message={}".format(msg.data))

        self.data= msg.data


if __name__ == "__main__":
    rospy.init_node("topic_publisher",anonymous=True)

    move_msg=msgs()

    ros_tutorial_pub=rospy.Publisher("topic1",Int64, queue_size=100)

    ros_tutorial_sub=rospy.Subscriber("topic2",Int64,move_msg.msg_callback,queue_size=10)

    tutorial = Int64()

    rate_= rospy.Rate(1)


    while not rospy.is_shutdown():


        tutorial.data= count
        
        print("send msg = {}".format(tutorial.data))

        ros_tutorial_pub.publish(tutorial)
        
        rate_.sleep()
    
        count=move_msg.data

        

    




