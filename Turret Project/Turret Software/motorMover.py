import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
import serial
from std_msgs.msg import String
import os

if os.path.exists('/dev/ttyACM0'):
    ser = serial.Serial('/dev/ttyACM0',9600,timeout = 1.0)
else:
    ser = serial.Serial('/dev/ttyACM1',9600,timeout = 1.0)

class OutputSubscriber(Node):
    def __init__(self):
        super().__init__('motor_mover')
        self.subscription = self.create_subscription(String, 'user_input', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        mess = msg.data.strip().lower()

        if (mess == "left"):
            ser.write(b'left')
        elif (mess == "right"):
            ser.write(b'right')
        elif (mess == "fire"):
            ser.write(b'fire')
        else:
            ser.write(b'none')
        

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

