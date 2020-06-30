#include "ros/ros.h"
#include "rospy_tutorials/AddTwoInts.h"

bool sub(rospy_tutorials::AddTwoInts::Request  &req,
         rospy_tutorials::AddTwoInts::Response &res)
{
  res.sum = req.a - req.b;
  ROS_INFO("request: x=%ld, y=%ld", (long int)req.a, (long int)req.b);
  ROS_INFO("sending back response: [%ld]", (long int)res.sum);
  return true;
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "sub_two_ints_server");
  ros::NodeHandle n;

  ros::ServiceServer service = n.advertiseService("sub_two_ints", sub);
  ROS_INFO("Ready to sub two ints.");
  ros::spin();

  return 0;
}  
