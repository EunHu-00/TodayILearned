#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):

    def __init__(self):
        super().__init__("first_node")
        self.get_logger().info("Hello from ROS2")

def main(args=None):
    #initialize ros2 communication, features
    rclpy.init(args=args)
    
    #create node
    node = MyNode()

    #kept alive until I kill it
    rclpy.spin(node)

    #destroy the node, all communication
    rclpy.shutdown()

if __name__ == '__main__':
    main()
