#include <Arduino.h>
#include <ESP32Servo.h>
#include <WiFi.h>

String inputBuffer = "";
bool dataReady = false;

int servo_id = 0;
int grados = 0;

const char* ssid = "iPhone de Juan Sebastian";
const char* clave = "juansmp08";
const int PUERTO = 8080;

Servo base,hombro1,hombro2,codo,rotatoriomin,muneca,dedos;

const int pinBase = 15;
const int pinHombro1 = 4;
const int pinHombro2 = 18;
const int pinCodo = 17;
const int pinRotatoriomin = 27;
const int pinMuneca = 26;
const int pinDedos = 13;

WiFiServer server(PUERTO);
WiFiClient client ;

void setup() {
  Serial.begin(115200); 
  base.attach(pinBase);
  hombro1.attach(pinHombro1);
  hombro2.attach(pinHombro2);
  codo.attach(pinCodo);
  rotatoriomin.attach(pinRotatoriomin);
  muneca.attach(pinMuneca);
  dedos.attach(pinDedos);

  WiFi.begin(ssid, clave);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConectado. IP:" + WiFi.localIP().toString());

  server.begin();
  Serial.println("Servidor listo en puerto "+ String(PUERTO));
}

void parsearDatos(String data) {

  int separador = data.indexOf(',');
  
  if (separador != -1) {
    servo_id = data.substring(0, separador).toInt();
    grados    = data.substring(separador + 1).toInt();
    switch (servo_id)
    {
    case 1:{
      base.write(grados);
      break;
    }

    case 2:{
    int mov1 = hombro1.read();

    if (mov1 < grados) {
        while (mov1 <= grados) {
            hombro1.write(mov1);
            hombro2.write(180 - mov1);
            mov1++;
            delay(20);
        }
    } else {
        while (mov1 >= grados) {
            hombro1.write(mov1);
            hombro2.write(180 - mov1);
            mov1--;
            delay(20);
        }
    }
    break;

    }
    case 3:{
      codo.write(grados);
    break; 
    }
    case 4:{
      rotatoriomin.write(grados);
      break;
    }
    case 5:{
      muneca.write(grados);
      break;
    }
    case 6:{
      dedos.write(grados);
      break;
    }
    default:{
      
      break;
    }

  }
}
  }


void loop() {

  if (!client || !client.connected()) {
    client = server.available();
    if (client) Serial.println("Cliente conectado");
  }

  if (client && client.connected()) {
    while (client.available()) {
      char c = client.read();
      if (c == '\n') {
        inputBuffer.trim();
        if (inputBuffer.length() > 0) {
          parsearDatos(inputBuffer);
        }
        inputBuffer = "";
      } else {
        inputBuffer += c;
      }
    }
  }
}

