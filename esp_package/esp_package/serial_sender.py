import rclpy
import serial
import time
from geometry_msgs.msg import Twist


port = '/dev/esp_32'
baudrate = 115200


def cmd_vel_listener(msg):
    ser = serial.Serial(port, baudrate)
    x = msg.linear.x
    z = msg.angular.z
    data = "*"+str(x)+";"+str(z)+";1#"
    ser.write(data.encode('utf-8'))
    ser.close()
    

def main():
    print('Starting serial_sender.')
    rclpy.init()
    node = rclpy.create_node("serial_sender")
    
    time.sleep(2)

    sub = node.create_subscription(Twist, "cmd_vel", cmd_vel_listener, 3)
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()
    
