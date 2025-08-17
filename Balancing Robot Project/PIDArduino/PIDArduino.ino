#include <cmath>

void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:

}

class PID {
private:
  double kp;
  double ki;
  double kd;
  double prevError;
  double integral;

public:
  PID(double kp_, double ki_, double kd_){
    prevError = 0.0;
    integral = 0.0;
  }
}