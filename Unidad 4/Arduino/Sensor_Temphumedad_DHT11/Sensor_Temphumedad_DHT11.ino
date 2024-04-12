#include <DHT.h>
#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

float h;
float t;
void loop() {

  h = dht.readHumidity();
  t = dht.readTemperature();

  Serial.println("Humedad: " + String(h) + "Temperatura: " + String(t));

  delay(2000);
}
