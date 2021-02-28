import rospy
from geometry_msgs.msg import Twist
from kobuki_msgs.msg import BumperEvent
from multiprocessing import Process
from math import radians
from random import random
from mediator import Mediator
import pyttsx3


class Executer():

    
    def __init__(self, queue):
        self.receiver = Queue()
        self.sender = Queue()
        self.mediator = Mediator(self.receiver, self.sender)
        self.mediator.start()
        rospy.init_node('executer', anonymous=False)
        rospy.on_shutdown(self.shutdown)
        self.rate = rospy.Rate(5)
        self.commander = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
        self.bumper = rospy.Subscriber('mobile_base/events/bumper', BumperEvent, self.processBump)


    def processBump(self, data):
        if (data.state == BumperEvent.PRESSED):
            package = {
                'type': 'bumper',
            }
            if data.bumper == 1:
                package['value'] = 'front'
            elif data.bumper == 0:
                package['value'] = 'left'
            elif data.bumper == 2:
                package['value'] = 'right'
            sender.put(package)
        else:
            rospy.loginfo("Bumper Event")
            rospy.loginfo(data.bumper)


    def run(self):

        twist = Twist()

        while not rospy.is_shutdown():

            if not self.receiver.empty():
                command = self.receiver.get()
                twist = Twist()
                if command['type'] == 'straight':
                    twist.linear.x = command['value']
                if command['type'] == 'turn':
                    twist.linear.x = 0
                    twist.angular.z = radians(command['value'])
                print(command)

            self.commander.publish(twist)
            self.rate.sleep()

            
    def shutdown(self):
        # stop turtlebot
        rospy.loginfo("Stopping")
        self.commander.publish(Twist())
        rospy.sleep(1)
