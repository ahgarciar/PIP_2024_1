int led = 13;

void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    //CONSIDERANDO USUARIOS SEMI PERFECTOS ...
    //CUALQUIER VALOR NUMERICO >0 OR <0 -> PRENDE EL LED
    //CUALQUIER VALOR NO NUMERO AAPGA EL LED
    int v = Serial.readString().toInt();
    digitalWrite(led, v); 
  }
}
