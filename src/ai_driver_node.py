#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""AI wheel driver node"""

# Import required Python code.
import rospy
from geometry_msgs.msg import Twist
from pprint import pprint


class AiDriverNode(object):

    def callback(self, twist):
        """Handle subscriber data."""
        # Simply print out values in our custom message.

        rospy.loginfo(
            "Linear velocity: %f  Angular velocity: %f ", twist.linear.x, twist.angular.z
        )


    def listener(self):
        """Configure subscriber."""
        # Create a subscriber with appropriate topic, custom message and name of
        # callback function.
        # rospy.Subscriber("cmd_vel", , callback)
        self.vel_subscribe = rospy.Subscriber("/cmd_vel", Twist, self.callback, queue_size=2)


# Main function.
if __name__ == "__main__":
    # Initialize the node and name it.
    rospy.init_node("ai_motor_driver")
    # Go to the main loop.
    node = AiDriverNode()
    node.listener()
    # Wait for messages on topic, go to callback function when new messages
    # arrive.
    rospy.spin()
