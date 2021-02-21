import rospy
from geometry_msgs.msg import Twist
from kobuki_msgs.msg import BumperEvent
from math import radians
from random import random
import pyttsx3


class Executer():

    
    def __init__(self, queue):
        self.queue = queue
        rospy.init_node('executer', anonymous=False)
        rospy.on_shutdown(self.shutdown)
        self.rate = rospy.Rate(5)
        self.commander = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
        #self.bumper = rospy.Subscriber('mobile_base/events/bumper', BumperEvent, self.processBump)

        
    def run(self):

        twist = Twist()

        while not rospy.is_shutdown():

            if not self.queue.empty():
                command = self.queue.get()
                print(command)
                twist = Twist()
                if command[0] == 0:
                    print('going')
                    twist.linear.x = command[1]
                if command[0] == 1:
                    twist.linear.x = 0
                    twist.angular.z = radians(command[1])
                print(twist)

            self.commander.publish(twist)
            self.rate.sleep()

            
    def shutdown(self):
        # stop turtlebot
        rospy.loginfo("Stopping")
        self.commander.publish(Twist())
        rospy.sleep(1)
