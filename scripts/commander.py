#!/usr/bin/env python
import rospy
from mavros_msgs.msg import GlobalPositionTarget, State
from mavros_msgs.srv import CommandBool, CommandTOL, SetMode
from geometry_msgs.msg import PoseStamped, Twist
from sensor_msgs.msg import Imu, NavSatFix
from std_msgs.msg import Float32, String, Bool
from pyquaternion import Quaternion
from offb.msg import Floatsxyz
import time
import math


g_reachwp = False
xc = []
yc = []
zc = []
def checker_callback(data):
    global g_reachwp
    g_reachwp = data.data
    # rospy.loginfo("g_reachwp in checker_callback %s" % g_reachwp)

def getwps_callback(data):
    global xc
    xc = data.x
    global yc
    yc = data.y
    # rospy.loginfo(rospy.get_name()+ "I heard x=%s y=%s z=%s", xc, yc, zc)
    # print rospy.get_name(), rospy.get_time(), "I heard x=%s y=%s"%(xc[2], yc[2]), type(xc)

class Commander:
    def __init__(self):
        # self.reachwp = None
        rospy.init_node("commander_node")

        rate = rospy.Rate(20)
        self.position_target_pub = rospy.Publisher('gi/set_pose/position', PoseStamped, queue_size=10)
        self.yaw_target_pub = rospy.Publisher('gi/set_pose/orientation', Float32, queue_size=10)
        self.custom_activity_pub = rospy.Publisher('gi/set_activity/type', String, queue_size=10)
        rospy.Subscriber("check_waypoint_bool", Bool, checker_callback)
        rospy.Subscriber("floats", Floatsxyz, getwps_callback)

    def move(self, x, y, z, BODY_OFFSET_ENU=True):
            while True:
                 #show if drone have reach waypoint
                #if drone have reach waypoint , publish new waypoint to the drone and done
                if g_reachwp==False :
                    # rospy.loginfo( "Have not reach last waypoint! %s" % g_reachwp)
                    time.sleep(0.1)
                    continue

                # if drone have not reach waypoint go back and check again
                else:
                    rospy.loginfo( "Reach last waypoint? %r" % g_reachwp)
                    self.position_target_pub.publish(self.set_pose(x, y, z, BODY_OFFSET_ENU))
                    rospy.loginfo("fly to next waypoint: %d, %d, %d" %(x, y, z) )
                    rospy.sleep(0.2)
                    if g_reachwp==False:
                        rospy.loginfo( "Reach new waypoint %d, %d, %d? %s" % (x, y, z, g_reachwp))
                    elif g_reachwp==True:
                        rospy.loginfo( "Reach new waypoint %d, %d, %d? %s" % (x, y, z, g_reachwp))
                    else:
                        rospy.loginfo("wtf?!%s" % g_reachwp)
                    time.sleep(0.1)
                    break
            rospy.loginfo("move Done!")






    def turn(self, yaw_degree):
        self.yaw_target_pub.publish(yaw_degree)


    # land at current position
    def land(self):
        self.custom_activity_pub.publish(String("LAND"))


    # hover at current position
    def hover(self):
        self.custom_activity_pub.publish(String("HOVER"))


    # return to home position with defined height
    def return_home(self, height):
        self.position_target_pub.publish(self.set_pose(0, 0, height, False))


    def set_pose(self, x, y, z=3, BODY_FLU = True):
        pose = PoseStamped()
        pose.header.stamp = rospy.Time.now()

        # ROS uses ENU internally, so we will stick to this convention
        if BODY_FLU:
            pose.header.frame_id = 'base_link'

        else:
            pose.header.frame_id = 'map'

        pose.pose.position.x = x
        pose.pose.position.y = y
        pose.pose.position.z = z

        return pose





if __name__ == "__main__":


    con = Commander()

    time.sleep(5)
    rospy.loginfo(rospy.get_name()+ "I heard x=%s y=%s ", xc, yc)
    for i in range(len(xc)):
        rospy.loginfo(rospy.get_name() + "I heard x=%s y=%s ", xc[i], yc[i])
        con.move(xc[i], yc[i], 3, BODY_OFFSET_ENU=False)
    # rospy.spin()
    rospy.loginfo("commander completed!!!")
