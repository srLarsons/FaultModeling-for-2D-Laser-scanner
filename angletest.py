#!/usr/bin/env python
import csv
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
import numpy as np

counter = 0
measurement = []
min_angle=0
max_angle=0
allangles=[]
angle= []
resolution=0
r =0
def callback(data):
  #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.ranges)
  global counter, angle,allangles,resolution, min_angle, max_angle,r
  counter = counter +1
  
  print counter
  
  min_angle=data.angle_min*630/11
  max_angle= data.angle_max*630/11
  datalength= len(data.ranges)
  resolution=(max_angle-min_angle)/(datalength-1)
 
  #print data.ranges
  #print len(data.ranges)
  print "start "+ "=" + str(min_angle)      # start angle of the scan [rad]
  print "end"+ "=" + str(max_angle)
  #print "resolution" + "=" +str(resolution)
  measurement.append(data.ranges[0])
  
  for angle in np.arange(min_angle, max_angle, resolution):
    measurement.append(data.ranges[0])
    allangles.append(angle)
    #print angle 
   
  #for allangles in xrange(float(min_angle),float(max_angle),float(resolution)):
      #print allangles
  #print measurement
  #print allangles
  
  #allangles.append(angle)
  #print allangles
  #if counter==21: 
  # print measurement
   #print angle
 

def listener():
  rospy.init_node('LaserScannerCatch', anonymous=True)
  rospy.Subscriber("/scan", LaserScan, callback)
  rospy.spin()

if __name__ == '__main__':
 listener()
 
def writeTocsv(data):
   measurement.append(data.ranges[0])
   allangles.append(angle)
   
   
with open('test.csv','w')as fp:
  a=csv.writer(fp)
  b=csv.writer(fp)
  
  data1= [],[measurement]
  data2= [],[allangles]
  a.writerows(data1)
  b.writerows(data2)

  
  
 
  