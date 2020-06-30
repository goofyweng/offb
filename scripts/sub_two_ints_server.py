#!/usr/bin/env python

from offb.srv import SubTwoInts,SubTwoIntsResponse
import rospy

def handle_sub_two_ints(req):
    print "Returning [%s - %s = %s]"%(req.a, req.b, (req.a - req.b))
    return SubTwoIntsResponse(req.a - req.b)

def sub_two_ints_server():
    rospy.init_node('sub_two_ints_server')
    s = rospy.Service('sub_two_ints', SubTwoInts, handle_sub_two_ints)
    print "Ready to sub two ints."
    rospy.spin()

if __name__ == "__main__":
    sub_two_ints_server()
