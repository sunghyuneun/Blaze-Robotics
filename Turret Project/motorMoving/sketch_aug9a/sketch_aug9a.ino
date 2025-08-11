#include <math.h>
const int stepPin = 2;
const int dirPin = 5; 

const int stepsPerRevo = 200;
const double anglePerStep = 1.8; 
const double maxAngle = 31.4;
const double maxFrame = 424;
const double FramePerAngle = 0.074;
const int maxSteps = round(maxAngle * 5 / anglePerStep);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600)
  pinMode(stepPin,OUTPUT);
  pinMode(dirPin,OUTPUT);
  delay(2000);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(dirPin, HIGH);
  for (int step = 0; step < maxSteps; step++){
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(1000);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(1000);

  }
  delay(5000);

  digitalWrite(dirPin, LOW);
  for (int step = 0; step < maxSteps; step++){
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(1000);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(1000);

  }
  delay(5000);
}
