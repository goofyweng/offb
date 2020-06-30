#!/usr/bin/env python
import rospy
from mavros_msgs.msg import PositionTarget
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Float32, String, Bool

class Server:
    def __init__(self):
        self.curposx = None
        self.curposy = None
        self.curposz = None
        self.targetwpx = None
        self.targetwpy = None
        self.targetwpz = None
        self.reachwp = None

    def curpos_callback(self, msg):
        # "Store" message received.
        self.curposx = msg.pose.position.x
        self.curposy = msg.pose.position.y
        self.curposz = msg.pose.position.z

        # Compute stuff.
        self.compute_stuff()

    def targetwp_callback(self, msg):
        # "Store" the message received.
        self.targetwpx = msg.position.x
        self.targetwpy = msg.position.y
        self.targetwpz = msg.position.z

        # Compute stuff.
        self.compute_stuff()

    def compute_stuff(self):
        if self.curposx is not None and self.targetwpx is not None:
            pub = rospy.Publisher('/uav1/check_waypoint_1', String, queue_size=10)
            pub_bool = rospy.Publisher('/uav1/check_waypoint_bool_1', Bool, queue_size=10)
            if abs(self.curposx - self.targetwpx) <  0.5 and abs(self.curposy - self.targetwpy) <  0.5 and abs(self.curposz - self.targetwpz) <  0.5:
                check_result = 'uav1 Reach waypoint!:', self.targetwpx, self.targetwpy, self.targetwpz % rospy.get_time()
                self.reachwp = True
                # rospy.loginfo("%s %r" %(check_result,self.reachwp))
                pub.publish(check_result)
                pub_bool.publish(self.reachwp)
                # print("Reach waypoint! ", self.targetwpx, self.targetwpy, self.targetwpz % rospy.get_time())
            else:
                 check_result = 'uav1 Fly to next waypoint:', self.targetwpx, self.targetwpy, self.targetwpz % rospy.get_time()
                 self.reachwp = False
                 # rospy.loginfo("%s %r" %(check_result,self.reachwp))
                 pub.publish(check_result)
                 pub_bool.publish(self.reachwp)
                # print("Flying to new waypoint", self.targetwpx, self.targetwpy, self.targetwpz % rospy.get_time())
            # pass  # Compute something.


if __name__ == '__main__':
    rospy.init_node('checker_1')

    server = Server()

    rospy.Subscriber("/uav1/mavros/local_position/pose", PoseStamped , server.curpos_callback)
    rospy.Subscriber("/uav1/mavros/setpoint_raw/local", PositionTarget, server.targetwp_callback)

    rospy.spin()
