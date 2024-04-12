int Pin_echo = 13; 
int Pin_trig = 12; 
 
void setup() { 
  Serial.begin (9600); 
  pinMode(Pin_trig, OUTPUT); 
  pinMode(Pin_echo, INPUT); 
}

 int pulso, cm; 
void loop() {   
  digitalWrite(Pin_trig, LOW); 
  delayMicroseconds(2); 
  digitalWrite(Pin_trig, HIGH); 
  delayMicroseconds(10); 
  digitalWrite(Pin_trig, LOW); 
  
  pulso = pulseIn(Pin_echo, HIGH); //Medición del ancho de pulso recibido en el pin Echo
  cm = pulso / 29 / 2;             // Convertimos ese pulso en una distancia y a cm
  
  Serial.println("Distancia:" + String(cm) + "cm."); 
  
  delay(100); 
}
