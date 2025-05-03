import rclpy
from geometry_msgs.msg import Twist
import time
import serial


x = z = 0
port = "/dev/ttyUSB0"
baudrate = 115200


def cmd_vel_listener(msg):
    global x, z
    x = msg.linear.x
    z = msg.angular.z
    serial_writer(x, z)


def serial_writer(x, z):
    ser = serial.Serial(port, baudrate, timeout = 1)
    data = "*{};{}#".format(x, z)
    ser.write(data.encode('utf-8'))
    time.sleep(5)
    ser.close()


def main():
    print('Starting serial_reader.')
    rclpy.init()
    node = rclpy.create_node("serial_listener")
    sub = node.create_subscription(Twist, "cmd_vel", cmd_vel_listener, 10)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

