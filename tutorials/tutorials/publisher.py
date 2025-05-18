import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import NavSatFix

class SimplePublisher(Node):
    def __init__(self):
        super().__init__('simple_publisher')
        self.publisher = self.create_publisher(NavSatFix, 'topic', 10)
        self.timer = self.create_timer(1.0, self.publish_message)

    def publish_message(self):
        msg = NavSatFix()
        msg.latitude = 37.3891    # ejemplo de latitud
        msg.longitude = -5.9845   # ejemplo de longitud
        msg.altitude = 100.0      # ejemplo de altitud
        self.publisher.publish(msg)
        self.get_logger().info(f'Publicado: {msg.latitude}, {msg.longitude}, {msg.altitude}')

def main(args=None):
    rclpy.init(args=args)
    node = SimplePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
