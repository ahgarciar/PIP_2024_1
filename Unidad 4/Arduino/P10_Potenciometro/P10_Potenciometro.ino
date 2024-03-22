//Voltaje de Referencia: 5v
//Bits de resolucion: 10bits de resolucion.... 1024 valores posibles...

//cada valor que les da el arduino se distancia uno del otro en 4.8mv 

//la señala analogica del arduino funciona con los pines analogicos ( A# ....)

int potenciomentro = A0; //pin analogico A0

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
  //pinMode no se utiliza para pines analogicos...

  //NOTA: un pin analogico solo es de entrada....
}

// P1    P2    P3
//GND    A#     5V
//       A0

int valor;
void loop() {
  // put your main code here, to run repeatedly:
  valor = analogRead(potenciomentro);
  Serial.println(valor);
  delay(100);
}
