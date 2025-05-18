import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import NavSatFix

class SimpleSubscriber(Node):
    def __init__(self):
        super().__init__('simple_subscriber')
        self.subscription = self.create_subscription(
            NavSatFix, 'topic', self.callback, 10)
        self.subscription  # Evita advertencias de variable no utilizada

    def callback(self, msg):
        self.get_logger().info(f'Recibido: {msg.latitude}, {msg.longitude}, {msg.altitude}')

def main(args=None):
    rclpy.init(args=args)
    node = SimpleSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
