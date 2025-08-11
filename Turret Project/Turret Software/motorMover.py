import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
import serial
from std_msgs.msg import Int16
from std_msgs.msg import String
import time
import os

if os.path.exists('/dev/ttyACM0'):
    ser = serial.Serial('/dev/ttyACM0',9600,timeout = 1.0)
else:
    ser = serial.Serial('/dev/ttyACM1',9600,timeout = 1.0)

class OutputSubscriber(Node):
    def __init__(self):
        super().__init__('motor_mover')
        self.subscription = self.create_subscription(Int16, 'centrePixel', self.listener_callback, 10)
        self.publisher = self.create_publisher(String, 'motor_done', 10)
        self.subscription  # prevent unused variable warning
        
        time.sleep(2)

    def listener_callback(self, msg):
        self.get_logger().info('Pixel: "%s"' % msg.data)

        pixel = str(msg.data)
        ser.write((pixel + '\n').encode('utf-8'))

        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()
                if line == "done":
                    self.publisher.publish(String(data='ready'))
                    self.get_logger().info('ready')
                    break
        

def main(args = None):
    try:
        with rclpy.init(args=args):
            outputSubscribe = OutputSubscriber()
            rclpy.spin(outputSubscribe)
            outputSubscribe.destroy_node()
            rclpy.shutdown()
    except (KeyboardInterrupt, ExternalShutdownException):
        ser.close()

if __name__ == "__main__":
    main()

