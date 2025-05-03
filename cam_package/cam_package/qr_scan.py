#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
import numpy as np

class QRCodeDetector(Node):
    def __init__(self):
        super().__init__('qr_code_detector')
        self.subscription = self.create_subscription(
            Image,
            '/camera/color/image_raw',  # Adjust this topic as necessary for your setup
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        # Convert ROS Image message to OpenCV format
        img = np.frombuffer(msg.data, np.uint8).reshape(msg.height, msg.width, -1)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect QR codes in the image
        detector = cv2.QRCodeDetector()
        data, bbox, _ = detector.detectAndDecode(img_gray)

        if bbox is not None and data:
            self.get_logger().info(f'Detected QR Code: {data}')
            # Draw bounding box around detected QR code (optional)
            #for i in range(len(bbox)):
                #cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % 4][0]), (255, 0, 0), 3)

            # Display the image with bounding box (optional)
            #cv2.imshow("QR Code Detection", img)
            #cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    qr_code_detector = QRCodeDetector()
    rclpy.spin(qr_code_detector)
    qr_code_detector.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
