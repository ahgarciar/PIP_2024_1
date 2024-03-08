// EL ARDUINO POSEE UN LED INTERNO DE PRUEBAS EN EL PIN DIGITAL 13..
int led = 13; // 2, 3, 4, 5.....13
int v;

void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT); 
}

void loop() {
  // put your main code here, to run repeatedly:

  digitalWrite(led, HIGH);
  Serial.println("LED PRENDIDO");
  delay(1000);
  digitalWrite(led, LOW);
  Serial.println("LED APAGADO");
  delay(1000);

}
