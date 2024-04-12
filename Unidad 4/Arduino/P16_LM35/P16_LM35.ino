//SENSOR DE TEMPERATURA ANALOGICO...
//EN EL QUE CADA GRADO EQUIVALE A APROX 5mV
int lm35 = A0;

//ADC - CONVERSOR ANALOGO DIGIAL
//(CONVIERTE UNA SEÑAL ANALOGICA A UNA SEÑAL DIGITAL)
// - VOLTAJE DE REFERENCIA: 5V
// - BITS DE RESOLUCION: 10 .... 2^10 = 1024 VALORES POSIBLES
//  0V = 0
//  5V = 1023

// 5/1023 = .0048Volts....   = 4.8mV

void setup() {
  // put your setup code here, to run once:
   Serial.begin(9600); 
}

int valor;
void loop() {  
    valor = analogRead(lm35); //0 - 1023

    Serial.print("Valor leido: " + String(valor));

    valor = (5.0 * valor * 100.0)/1023.0; // °C

    Serial.println("  Temp: " + String(valor));

    delay(100);
}
