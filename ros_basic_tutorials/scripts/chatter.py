#!/usr/bin/python3

# Include rospy library
import rospy

# Include ros msgs
from std_msgs.msg import String


def main():
	# ROS Node initializer
	rospy.init_node('talker', anonymous=True, log_level=rospy.DEBUG)

	# ROS Publisher to chatter topic
	pub = rospy.Publisher('chatter', String, queue_size=10)

	# Defining publishing rate of node
	rate = rospy.Rate(1)

	while not rospy.is_shutdown():
		name = "Your Name %s" % rospy.get_time()
		rospy.loginfo(name)
		pub.publish(name)
		rate.sleep()

if __name__ == "__main__":
	try:
		main()
	except rospy.ROSInterruptException:
		pass
