#include "Servo.h"   

int pinServo = 9;
Servo servo; 

void setup(){ 
  Serial.begin(9600);
  servoMotor.attach(pinServo);
}
 
void loop(){

  servoMotor.write(0);
  Serial.println("Servo en 0°");
  delay(500); 
    
  servoMotor.write(180);
  Serial.println("Servo en 180°");
  delay(500); 
}