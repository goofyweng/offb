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
import threading

# check if reach waypoint variables
g_reachwp_0 = False
g_reachwp_1 = False
g_reachwp_2 = False

# list to store waypoint coordinates for three drones
# xc_0 = [0, -6.47, -10, -20.47, 0]
# yc_0 = [0, -4.44, 4.05, 7.02, 0]
xc_0 = []
yc_0 = []
zc_0 = []

# xc_1 = [2, 5.2, 5.39, 16.3, 40.09,2]
# yc_1 = [0, 7.666, 6.37, -7.38, -1.54,0]
xc_1 = []
yc_1 = []
zc_1 = []

# xc_2 = [0, 15.23, 19.47, 0]
# yc_2 = [2, 7.24, 6.1, 2]
xc_2 = []
yc_2 = []
zc_2 = []
def checker_callback_0(data):
    global g_reachwp_0
    g_reachwp_0 = data.data
    # rospy.loginfo("g_reachwp_0 in checker_callback %s" % g_reachwp_0)

def checker_callback_1(data):
    global g_reachwp_1
    g_reachwp_1 = data.data
    # rospy.loginfo("g_reachwp_1 in checker_callback %s" % g_reachwp_1)

def checker_callback_2(data):
    global g_reachwp_2
    g_reachwp_2 = data.data
    # rospy.loginfo("g_reachwp_2 in checker_callback %s" % g_reachwp_2)

def getwps_callback_0(data):
    global xc_0
    xc_0 = data.x
    global yc_0
    yc_0 = data.y
    # rospy.loginfo(rospy.get_name()+ "I heard x=%s y=%s z=%s", xc, yc, zc)
    # print rospy.get_name(), rospy.get_time(), "I heard x=%s y=%s"%(xc[2], yc[2]), type(xc)

def getwps_callback_1(data):
    global xc_1
    xc_1 = data.x
    global yc_1
    yc_1 = data.y
    # rospy.loginfo(rospy.get_name()+ "I heard x=%s y=%s z=%s", xc, yc, zc)
    # print rospy.get_name(), rospy.get_time(), "I heard x=%s y=%s"%(xc[2], yc[2]), type(xc)

def getwps_callback_2(data):
    global xc_2
    xc_2 = data.x
    global yc_2
    yc_2 = data.y
    # rospy.loginfo(rospy.get_name()+ "I heard x=%s y=%s z=%s", xc, yc, zc)
    # print rospy.get_name(), rospy.get_time(), "I heard x=%s y=%s"%(xc[2], yc[2]), type(xc)

class Commander:
    def __init__(self):
        # self.reachwp = None
        rospy.init_node("commander_node")

        rate = rospy.Rate(20)
        self.position_target_pub_0 = rospy.Publisher('/uav0/gi/set_pose/position', PoseStamped, queue_size=10)
        self.yaw_target_pub_0 = rospy.Publisher('/uav0/gi/set_pose/orientation', Float32, queue_size=10)
        self.custom_activity_pub_0 = rospy.Publisher('/uav0/gi/set_activity/type', String, queue_size=10)

        self.position_target_pub_1 = rospy.Publisher('/uav1/gi/set_pose/position', PoseStamped, queue_size=10)
        self.yaw_target_pub_1 = rospy.Publisher('/uav1/gi/set_pose/orientation', Float32, queue_size=10)
        self.custom_activity_pub_1 = rospy.Publisher('/uav1/gi/set_activity/type', String, queue_size=10)

        self.position_target_pub_2 = rospy.Publisher('/uav2/gi/set_pose/position', PoseStamped, queue_size=10)
        self.yaw_target_pub_2 = rospy.Publisher('/uav2/gi/set_pose/orientation', Float32, queue_size=10)
        self.custom_activity_pub_2 = rospy.Publisher('/uav2/gi/set_activity/type', String, queue_size=10)

        rospy.Subscriber("/uav0/check_waypoint_bool_0", Bool, checker_callback_0)
        rospy.Subscriber("/uav0/floats_0", Floatsxyz, getwps_callback_0)

        rospy.Subscriber("/uav1/check_waypoint_bool_1", Bool, checker_callback_1)
        rospy.Subscriber("/uav1/floats_1", Floatsxyz, getwps_callback_1)

        rospy.Subscriber("/uav2/check_waypoint_bool_2", Bool, checker_callback_2)
        rospy.Subscriber("/uav2/floats_2", Floatsxyz, getwps_callback_2)


    def move_0(self, x, y, z, BODY_OFFSET_ENU=True):
            while True:
                 #show if drone have reach waypoint
                #if drone have reach waypoint , publish new waypoint to the drone and done
                if g_reachwp_0==False :
                    # rospy.loginfo( "Have not reach last waypoint! %s" % g_reachwp_0)
                    time.sleep(0.1)
                    continue

                # if drone have not reach waypoint go back and check again
                else:
                    rospy.loginfo( "uav0 Reach last waypoint? %r" % g_reachwp_0)
                    self.position_target_pub_0.publish(self.set_pose(x, y, z, BODY_OFFSET_ENU))
                    rospy.loginfo("uav0 fly to next waypoint: %d, %d, %d" %(x, y, z) )
                    time.sleep(1)
                    rospy.loginfo('move0!!!!!!!!!!!!!!!!!!')
                    # if g_reachwp_0==False:
                    #     rospy.loginfo( "uav0 Reach new waypoint %d, %d, %d? %s" % (x, y, z, g_reachwp_0))
                    # elif g_reachwp_0==True:
                    #     rospy.loginfo( "uav0 Reach new waypoint %d, %d, %d? %s" % (x, y, z, g_reachwp_0))
                    # else:
                    #     rospy.loginfo("uav0 wtf?!%s" % g_reachwp_0)
                    time.sleep(0.1)
                    break
            rospy.loginfo("uav0 move Done!")
#================================================================================================================
#================================================================================================================
    def move_1(self, x, y, z, BODY_OFFSET_ENU=True):
            while True:
                 #show if drone have reach waypoint
                #if drone have reach waypoint , publish new waypoint to the drone and done
                if g_reachwp_1==False :
                    # rospy.loginfo( "Have not reach last waypoint! %s" % g_reachwp_1)
                    time.sleep(0.1)
                    continue

                # if drone have not reach waypoint go back and check again
                else:
                    rospy.loginfo( "uav1 Reach last waypoint? %r" % g_reachwp_1)
                    self.position_target_pub_1.publish(self.set_pose(x, y, z, BODY_OFFSET_ENU))
                    rospy.loginfo("uav1 fly to next waypoint: %d, %d, %d" %(x, y, z) )
                    time.sleep(1)
                    rospy.loginfo('move1!!!!!!!!!!!!!!!!!!')
                    # if g_reachwp_1==False:
                    #     rospy.loginfo( "uav1 Reach new waypoint %d, %d, %d? %s" % (x, y, z, g_reachwp_1))
                    # elif g_reachwp_1==True:
                    #     rospy.loginfo( "uav1 Reach new waypoint %d, %d, %d? %s" % (x, y, z, g_reachwp_1))
                    # else:
                    #     rospy.loginfo("uav1 wtf?!%s" % g_reachwp_1)
                    time.sleep(0.1)
                    break
            rospy.loginfo("uav1 move Done!")
#================================================================================================================
#================================================================================================================
    def move_2(self, x, y, z, BODY_OFFSET_ENU=True):
            while True:
                 #show if drone have reach waypoint
                #if drone have reach waypoint , publish new waypoint to the drone and done
                if g_reachwp_2==False :
                    # rospy.loginfo( "Have not reach last waypoint! %s" % g_reachwp_2)
                    time.sleep(0.1)
                    continue

                # if drone have not reach waypoint go back and check again
                else:
                    rospy.loginfo( "uav2 Reach last waypoint? %r" % g_reachwp_2)
                    self.position_target_pub_2.publish(self.set_pose(x, y, z, BODY_OFFSET_ENU))
                    rospy.loginfo("uav2 fly to next waypoint: %d, %d, %d" %(x, y, z) )
                    time.sleep(0.2)
                    rospy.loginfo('move2!!!!!!!!!!!!!!!!!!')
                    # if g_reachwp_2==False:
                    #     rospy.loginfo( "uav2 Reach new waypoint %d, %d, %d? %s" % (x, y, z, g_reachwp_2))
                    # elif g_reachwp_2==True:
                    #     rospy.loginfo( "uav2 Reach new waypoint %d, %d, %d? %s" % (x, y, z, g_reachwp_2))
                    # else:
                    #     rospy.loginfo("uav2 wtf?!%s" % g_reachwp_2)
                    time.sleep(0.1)
                    break
            rospy.loginfo("uav2 move Done!")


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

# after getting the waypoints for each drones
# ask each drone to go through their designated waypoints independently
def uav0_mission_start():
    # print('uav0 waypoints:',xc_0 , yc_0)
    for i in range(len(xc_0)):
        rospy.loginfo(rospy.get_name() + "uav0 heard x=%s y=%s ", xc_0[i], yc_0[i])
        con.move_0(xc_0[i], yc_0[i], 3, BODY_OFFSET_ENU=False)
        rospy.loginfo('uav0 move to waypoint #%d' %(i+1))
    rospy.loginfo("uav0 mission completed!!! Retuening home...")

def uav1_mission_start():
    # print('uav1 waypoints:',xc_1 , yc_1)
    for i in range(len(xc_1)):
        rospy.loginfo(rospy.get_name() + "uav1 heard x=%s y=%s ", xc_1[i], yc_1[i])
        con.move_1(xc_1[i], yc_1[i], 3, BODY_OFFSET_ENU=False)
        rospy.loginfo('uav1 move to waypoint #%d' %(i+1))
    rospy.loginfo( "uav1 mission completed!!! Retuening home...")

def uav2_mission_start():
    for i in range(len(xc_2)):
        rospy.loginfo(rospy.get_name() + "uav2 heard x=%s y=%s ", xc_2[i], yc_2[i])
        con.move_2(xc_2[i], yc_2[i], 3, BODY_OFFSET_ENU=False)
        rospy.loginfo('uav2 move to waypoint #%d' %(i+1))
    rospy.loginfo("uav2 mission completed!!! Retuening home...")

# a mission timer 
# to record how much time we need to complete mission in simulation
def mission_timer(t1):
        while True:
            if g_reachwp_0==True and g_reachwp_1==True and g_reachwp_2==True:
                finish = time.time()
                rospy.loginfo( "All uavs returned home!!! Finished in %s second(s)" %round((finish-t1),2) )
                break
            else:
                # print("mission not done yet! waiting...")
                continue

if __name__ == "__main__":


    con = Commander()

    rospy.sleep(1)
    # con.move_0(3 ,6 ,3 ,BODY_OFFSET_ENU=False)

    start = time.time()
    # for i in range(len(xc_0)):
    #     rospy.loginfo(rospy.get_name() + "uav0 heard x=%s y=%s ", xc_0[i], yc_0[i])
    #     con.move_0(xc_0[i], yc_0[i], 3, BODY_OFFSET_ENU=False)
    #
    #     rospy.loginfo(rospy.get_name() + "uav1 heard x=%s y=%s ", xc_1[i], yc_1[i])
    #     con.move_1(xc_1[i], yc_1[i], 3, BODY_OFFSET_ENU=False)
    #
    #     rospy.loginfo(rospy.get_name() + "uav2 heard x=%s y=%s ", xc_2[i], yc_2[i])
    #     con.move_2(xc_2[i], yc_2[i], 3, BODY_OFFSET_ENU=False)
    #
    #     print('the %d time in for loop' %(i+1))
    # rospy.loginfo("uavs mission completed!!!")

    m0 = threading.Thread(target=uav0_mission_start)
    m1 = threading.Thread(target=uav1_mission_start)
    m2 = threading.Thread(target=uav2_mission_start)

    m0.start()
    m1.start()
    m2.start()

    m0.join()
    m1.join()
    m2.join()

    mission_timer(start)

    rospy.spin()
