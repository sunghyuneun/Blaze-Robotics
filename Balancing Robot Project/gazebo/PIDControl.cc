#include <iostream>
#include <string>
#include <chrono>
#include <gz/msgs.hh>
#include <gz/transport.hh>
#include <gz/math/Quaternion.hh>


class PID{
    public:
        double kp; double ki; double kd;
        double integral; double prev_error;

        PID(double kp_, double ki_, double kd_)
            : kp(kp_), ki(ki_), kd(kd_), integral(0.0), prev_error(0.0) {}

        double calculate(double setpoint, double measured_value, double dt) {
            double error = setpoint - measured_value;
            integral += error * dt;
            double derivative = (error - prev_error) / dt;
            prev_error = error;
            return -1.0 * (kp * error + ki * integral + kd * derivative);
        }
};


void cb(const gz::msgs::IMU &_msg);


PID pid(0.7, 0.0, 0.5);
gz::transport::Node node;
std::string subscribeTopic = "/imu";
std::string publishTopic = "/balanceVel";
auto pub = node.Advertise<gz::msgs::Twist>(publishTopic);
auto lastTime = std::chrono::steady_clock::now();


int main(int argc, char **argv)
{
    if (!node.Subscribe(subscribeTopic, cb)){
        std::cerr << "Error subscribing to topic [" << subscribeTopic << "]" << std::endl;
        return -1;
    }

    gz::transport::waitForShutdown();
 
    return 0;
}



void cb(const gz::msgs::IMU &_msg)
{
    gz::math::Quaterniond quat(
        _msg.orientation().w(),
        _msg.orientation().x(),
        _msg.orientation().y(),
        _msg.orientation().z()
    );

    double roll = quat.Roll();
    double xVel = _msg.angular_velocity().x();
    //double roll = atan2(2*(wQuat*xQuat + yQuat*zQuat), 1 - 2*(xQuat*xQuat + yQuat*yQuat));
    
    auto currentTime = std::chrono::steady_clock::now();
    double dt = std::chrono::duration<double>(currentTime - lastTime).count();
    lastTime = currentTime;

    double correction = pid.calculate(0.0, roll, dt);
    
    gz::msgs::Twist msg;
    msg.mutable_linear()->set_x(correction);
    msg.mutable_angular()->set_z(0.0); // No rotation correction
    pub.Publish(msg);

    //gz topic -t "/cmd_vel" -m gz.msgs.Twist -p "linear: {x: 0.5}, angular: {z: 0.05}"
    //std::cout << "Roll: " << roll << std::endl;
    //std::cout << "X Velocity: " << xVel << std::endl;
    
}

