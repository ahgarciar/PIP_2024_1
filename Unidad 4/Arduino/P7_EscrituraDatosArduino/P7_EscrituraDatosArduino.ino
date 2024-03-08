int v;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){ //comprueba el buffer del arduino
    //readString leera a todos los bytes que le sea posible antes de que
    //se acabe su tiempo de espera (timeout)
    //POR DEFECTO EL TIMEOUT ES DE 1 SEGUNDO
    v = Serial.readString().toInt();
    Serial.println(v);
  }
}
