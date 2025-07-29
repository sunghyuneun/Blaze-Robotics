import cv2
import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from std_msgs.msg import String
from cameraDir import aimer

class cameraMover(Node):
    
    def __init__(self):
        super().__init__('camera_aim')
        self.publisher_ = self.create_publisher(String, 'user_input', 10)
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            self.get_logger().error("Camera no open")
        
        self.timer = self.create_timer(1.5  , self.timer_callback)

    def timer_callback(self):
        ret,frame = self.cap.read()
        if not ret:
            self.get_logger().warn("Failed to frame")
            return
        
        direction, frame = aimer(frame)
        if direction and direction != "none":
            msg = String()
            msg.data = direction
            self.publisher_.publish(msg)
            self.get_logger().info(f'Published: "{direction}"')

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