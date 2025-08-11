#include <math.h>

const int stepPin = 2;
const int dirPin = 5; 
//r = 91 cm 
//d = 95 cm
const int stepsPerRevo = 200;
const double stepPerAngle = 5 / 1.8; 
const double maxAngle = 31.4;
const double maxFrame = 424;
const double anglePerFrame = 0.074;
const double stepPerFrame = stepPerAngle * anglePerFrame;

void setup() {
  // put your setup code here, to run once:
  pinMode(stepPin,OUTPUT);
  pinMode(dirPin,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    String str = Serial.readStringUntil('\n');
    str.trim();
    move(str.toInt());
    
    //Serial.print("I received: ");
    //Serial.println(str);
    delay(2000);
    Serial.println("done");
  }
  //delay(100);
}


void noTarget(){
  digitalWrite(dirPin,LOW);
  digitalWrite(stepPin,LOW);
  delay(10);
}

void move(int frames){
  int realFrames = frames - 424;
  if (realFrames < -10){
    digitalWrite(dirPin, HIGH);
    for (int step = 0; step < round(realFrames*(-1)*stepPerFrame); step++){
      digitalWrite(stepPin, HIGH);
      delayMicroseconds(1000);
      digitalWrite(stepPin, LOW);
      delayMicroseconds(1000);
    }
  } else if (realFrames > 10){
    digitalWrite(dirPin, LOW);
    for (int step = 0; step < round(realFrames*stepPerFrame); step++){
      digitalWrite(stepPin, HIGH);
      delayMicroseconds(1000);
      digitalWrite(stepPin, LOW);
      delayMicroseconds(1000);
    }

  } else{

  }
  delay(500);
}