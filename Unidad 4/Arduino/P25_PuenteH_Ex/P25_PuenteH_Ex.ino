//l298d --- módulo 
//--- 2 puentes h   --- motor driver 

//ENA.  - VELOCIDAD DE GIRO
//IN1   .... SENTIDO
//IN2   ....
//OUT1
//OUT2

//ENB
//IN3
//IN4
//OUT3
//OUT4

int ENA = 3; //Pin PWM
int in1 = 5;
int in2 = 6;

//conectados al motor
//out1 y out2 se conectan diractemente del puente h al motor

void setup() {
  // put your setup code here, to run once:
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  //ENA ... no lleva pinmode porque es de PWM

  Serial.begin(9600);
  Serial.setTimeout(10);

}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
      int v = Serial.readString().toInt();
      if (v == 0){
        Serial.println("Detenerse");
        digitalWrite(in1, 0);
        digitalWrite(in2, 0);
        analogWrite(ENA, 0);
      }
      else if(v==1){
        Serial.println("Girar Izquierda");
        digitalWrite(in1, 0);
        digitalWrite(in2, 1);
        analogWrite(ENA, 255);
      }
      else if (v == 2){
        Serial.println("Girar Derecha");      
        digitalWrite(in1, 1);
        digitalWrite(in2, 0);
        analogWrite(ENA, 255);
      }
      else{
        Serial.println("Movimiento no valido!");
      }
  }
  delay(100);
}


