import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


class MoveForward(Node):

    def __init__(self):
        super().__init__('move_forward_node')

        self.publisher_ = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

        self.scan_subscriber = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

        self.front_distance = float('inf')
        self.left_distance = float('inf')
        self.right_distance = float('inf')

        self.timer = self.create_timer(
            0.1,
            self.move_robot
        )

    def scan_callback(self, msg):

        self.front_distance = msg.ranges[0]
        self.left_distance = msg.ranges[90]
        self.right_distance = msg.ranges[270]

        print(
            f"Front: {self.front_distance:.2f}, "
            f"Left: {self.left_distance:.2f}, "
            f"Right: {self.right_distance:.2f}"
        )

    def move_robot(self):

        msg = Twist()

        if self.front_distance < 0.3:

            msg.linear.x = 0.0

            if self.left_distance > self.right_distance:
                msg.angular.z = 0.5
            else:
                msg.angular.z = -0.5

        else:

            msg.linear.x = 0.2
            msg.angular.z = 0.0

        self.publisher_.publish(msg)


def main(args=None):

    rclpy.init(args=args)

    node = MoveForward()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
