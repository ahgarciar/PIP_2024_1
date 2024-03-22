int led = 13;

void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(10);
}

int v; 
void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
      v = Serial.readString().toInt();
      digitalWrite(led, v);
  }
  delay(100);
}
