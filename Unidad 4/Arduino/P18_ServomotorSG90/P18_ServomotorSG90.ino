#include "Servo.h"   

int pinServo = 9;
Servo servo; 

void setup(){ 
  Serial.begin(9600);
  servo.attach(pinServo);
}
 
void loop(){

  servo.write(0);
  Serial.println("Servo en 0°");
  delay(500); 
    
  servo.write(180);
  Serial.println("Servo en 180°");
  delay(500); 
}