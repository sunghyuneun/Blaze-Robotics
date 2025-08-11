import cv2
import time
import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Int16
from cameraDir import aimer

class cameraMover(Node):
    
    def __init__(self):
        super().__init__('camera_aim')
        self.publisher = self.create_publisher(Int16, 'centrePixel', 10)
        self.subscription_ = self.create_subscription(String, 'motor_done', self.motor_done_call, 10)

        self.last_center = None
        self.last_change_time = time.time()
        self.get_logger().info("Motor is ready")
        self.motor_ready = True

        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            self.get_logger().error("Camera no open")
        
        self.timer = self.create_timer(.1, self.timer_callback)

    def motor_done_call(self,msg):
        if msg.data == "ready":
            self.get_logger().info("Motor is ready")
            self.motor_ready = True

    def timer_callback(self):

        print(f'Last Center: {self.last_center}, Last Time: {self.last_change_time}, Motor Ready: {self.motor_ready}')
        ret,frame = self.cap.read()
        if not ret:
            self.get_logger().warn("Failed to frame")
            return
        
        centrePixel, frame = aimer(frame)
        if centrePixel == -1:
            self.last_center = None
            return


        if self.last_center and abs(centrePixel - self.last_center) < 20:
            if (time.time() - self.last_change_time) > 2.0 and self.motor_ready:
                msg = Int16()
                msg.data = centrePixel
                self.get_logger().info(f'Pixel Location: {centrePixel}')
                self.publisher.publish(msg)
                self.motor_ready = False
        else:
            self.last_change_time = time.time()

        self.last_center = centrePixel

        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.destroy_node()
            rclpy.shutdown()

    def destroy_node(self):
        self.cap.release()
        cv2.destroyAllWindows()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    camera = cameraMover()
    try:
        rclpy.spin(camera)
    except (KeyboardInterrupt, ExternalShutdownException):
        #ser.close()
        pass
    finally:
        camera.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()