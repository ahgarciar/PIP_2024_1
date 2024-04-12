int PIR = 2;

void setup() {
  Serial.begin (9600);
  pinMode(PIR, INPUT_PULLUP);
}

int val;
void loop() {

  val = digitalRead(PIR);
  Serial.println("Señal:" + String(val));
  
  delay(100);
}
