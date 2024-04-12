int LDR = A0;

void setup() {
  // put your setup code here, to run once:
   Serial.begin(9600);
  
}

int valor;
void loop() {  
    valor = analogRead(LDR); //0 - 1023

    Serial.println("Valor leido: " + String(valor));
   
    delay(200);
}

