#!/usr/bin/python3

# Include rospy library
import rospy

# Include ros msgs
from std_msgs.msg import String

# Subscriber callback function
def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def main():
	# ROS Node initializer
	rospy.init_node('listener', anonymous=True, log_level=rospy.DEBUG)

	# ROS Subscriber on chatter topic
	rospy.Subscriber('chatter', String, callback)

	# Listening to callback with spin
	rospy.spin()

if __name__ == '__main__':
	main()
