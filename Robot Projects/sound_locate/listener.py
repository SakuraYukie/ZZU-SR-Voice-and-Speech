#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from math import pi
from std_msgs.msg import Int32
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'The angle is %d', data.data)
    # Publisher to control the robot's speed
    cmd_vel = rospy.Publisher('cmd_vel', Twist, queue_size=1)
        
        # How fast will we update the robot's movement?
    rate = 100
    #rospy.sleep(5)
        # Set the equivalent ROS rate variable
    r = rospy.Rate(rate)
        
       # Set the forward linear speed to 0.2 meters per second 
    linear_speed = 0.2
        
        # Set the travel distance to 1.0 meters
    goal_distance = 0.0
        
        # How long should it take us to get there?
    linear_duration = goal_distance / linear_speed
        
        # Set the rotation speed to 1.0 radians per second
   # angular_speed = 1.0
        
        # Set the rotation angle to Pi radians (180 degrees)
    if(data.data>=180):
	angular_speed = 1.0
	goal_angle = (360-data.data)*pi/180
	angular_duration = goal_angle / angular_speed
    else:
	angular_speed=-1.0
	goal_angle = (data.data)*pi/180
	angular_duration = goal_angle
        
        # How long should it take to rotate?
    #angular_duration = goal_angle / angular_speed
     
        # Loop through the two legs of the trip  
    for i in range(1):
            # Initialize the movement command
        move_cmd = Twist()
            
            # Set the forward speed
        move_cmd.linear.x = linear_speed
            
            # Move forward for a time to go the desired distance
        ticks = int(linear_duration * rate)
            
        for t in range(ticks):
            cmd_vel.publish(move_cmd)
            r.sleep()
            
            # Stop the robot before the rotation
        move_cmd = Twist()
        cmd_vel.publish(move_cmd)
        rospy.sleep(1)
            
            # Now rotate left roughly 180 degrees  
            
            # Set the angular speed
        move_cmd.angular.z = angular_speed

            # Rotate for a time to go 180 degrees
        ticks = int(angular_duration * rate)
            
        for t in range(ticks):           
            cmd_vel.publish(move_cmd)
            r.sleep()
                
            # Stop the robot before the next leg
        move_cmd = Twist()
        cmd_vel.publish(move_cmd)
        rospy.sleep(1)    
            
        # Stop the robot
    cmd_vel.publish(Twist())

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('chatter', Int32, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
