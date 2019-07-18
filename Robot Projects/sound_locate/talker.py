#!/usr/bin/env python
# coding=UTF-8
import serial
import sys
import rospy 
from std_msgs.msg import Int32

def talker():
    pub = rospy.Publisher('chatter', Int32, queue_size=1000)
      #Publisher函数创建发布节点（topic名‘chatter’，消息类型String，queue_size发布消息缓冲区大小都是未被接收走的）
    
    rospy.init_node('talker', anonymous=True)
      #启动节点talker，同时为节点命名，若anoymous为真则节点会自动补充名字，实际名字以talker_322345等表示，
      #若为假，则系统不会补充名字，采用用户命名。如果有重名，则最新启动的节点会注销掉之前的同名节点
    
    #rate = rospy.Rate(100) # 10hz
      #延时的时间变量赋值，通过rate.sleep()实现延时
    try:
	ser = serial.Serial('/dev/ttyUSB1', 115200)
    except Exception, e:
	print 'open serial failed.'
	exit(1)
    while not rospy.is_shutdown():
           # 判定开始方式，循环发送，以服务程序跳出为终止点 一般ctrl+c也可
	i=0	

	print 'A Serial Echo Is Running...'
	angle = 0
	while True:
	# echo
		arr=ser.readline().decode("gbk")
		i=i+1
		if i==17:
			i=0
		if i==4:
			if arr[16]==' ':
				angle=(int)(arr[15])
				pub.publish(angle)
			
			elif arr[17]==' ':
				angle=(int)(arr[15])*10+(int)(arr[16])
				pub.publish(angle)
			
			else :
				angle=(int)(arr[15])*100+(int)(arr[16])*10+(int)(arr[17])
				pub.publish(angle)
			
		#print arr[15],arr[16],arr[17]
		# write to stdout and flush it
		#sys.stdout.write(s)

		sys.stdout.flush()
		#hello_str = "hello world %s" % rospy.get_time()
		  # 数据变量的内容 rospy.get_time() 是指ros系统时间，精确到0.01s 
		
		#rospy.loginfo(hello_str)
		  #在运行的terminal界面info 出信息，可不加，可随意改
		
		#pub.publish(angle)
		  #发布数据 必须发布
		
		#rate.sleep()
		  # 按rospy.Rate()设置的速率延迟 

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
