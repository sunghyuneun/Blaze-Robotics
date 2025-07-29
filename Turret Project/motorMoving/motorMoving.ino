const int stepPin = 2;
const int dirPin = 5; 

String str;
void setup() {
  // put your setup code here, to run once:
  pinMode(stepPin,OUTPUT);
  pinMode(dirPin,OUTPUT);
  Serial.begin(9600);
  left();
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() == 0) {
    str = Serial.readString();
  }
  str.trim();
  if (str == "left"){
    for (int i = 0; i < 50; i++){
      left();
    }
  } else if (str == "right"){
    for (int i = 0; i < 50; i++){
      right();
    }
  } else{
    noTarget();
  }
  delay(100);
}


void left(){
  digitalWrite(dirPin,HIGH);
  for (int x = 0; x < 5; x++){
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(stepPin,LOW);
    delayMicroseconds(10);
  }
  delay(10);
  
}

void right(){
  digitalWrite(dirPin,LOW);
  for (int x = 0; x < 5; x++){
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(stepPin,LOW);
    delayMicroseconds(10);
  }
  delay(10);
}

void noTarget(){
  digitalWrite(dirPin,LOW);
  digitalWrite(stepPin,LOW);
  delay(10);
}
/*
const int stepPin = 2;
const int dirPin = 5; 

String str;
void setup() {
  // put your setup code here, to run once:
  pinMode(stepPin,OUTPUT);
  pinMode(dirPin,OUTPUT);
  Serial.begin(9600);
  left();
  delay(100);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() == 0) {
    str = Serial.readString();
  }
  str.trim();
  if (str == "left"){
    left();
  } else if (str == "right"){
    right();
  } else if (str == "turn"){
    left();
  }
  delay(100);
}

void left(){
  digitalWrite(dirPin,HIGH);
  for (int y = 0; y < 10; y++){
    for (int x = 0; x < 5; x++){
      digitalWrite(stepPin, HIGH);
      delayMicroseconds(10);
      digitalWrite(stepPin,LOW);
      delayMicroseconds(10);
    }
    delay(10);
  }
}

void right(){
  digitalWrite(dirPin,LOW);
  for (int y = 0; y < 10; y++){
    for (int x = 0; x < 5; x++){
      digitalWrite(stepPin, HIGH);
      delayMicroseconds(10);
      digitalWrite(stepPin,LOW);
      delayMicroseconds(10);
    }
    delay(10);
  }
}
*/
