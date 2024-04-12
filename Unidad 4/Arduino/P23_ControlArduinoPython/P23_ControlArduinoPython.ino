int led = 13;

void setup() {
  Serial.begin (9600);
  Serial.setTimeout(10);
  pinMode(led, OUTPUT);
}

int val;
void loop() {

  if(Serial.available()>0){
    val = Serial.readString().toInt();
    digitalWrite(led, val);
    if(val == 1){
      Serial.println("Led Prendido");
    }
    else{
      Serial.println("Led Apagado");
    }
  }

  delay(100);
}
