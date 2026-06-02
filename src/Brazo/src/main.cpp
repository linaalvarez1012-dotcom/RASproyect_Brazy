#include <Arduino.h>
#include <ESP32Servo.h>
#include <WiFi.h>
#include "soc/soc.h"
#include "soc/rtc_cntl_reg.h"

const char* ssid  = "iPhone de Juan Sebastian";
const char* clave = "juansmp08";
const int   PUERTO = 8080;

const int pinBase         = 15;
const int pinHombro1      = 18;
const int pinHombro2      = 4;
const int pinCodo         = 17;
const int pinRotatoriomin = 27;
const int pinMuneca       = 26;
const int pinDedos        = 13;

Servo base, hombro1, hombro2, codo, rotatoriomin, muneca, dedos;

WiFiServer server(PUERTO);
WiFiClient client;
String inputBuffer = "";

int servo_id = 0;
int grados   = 0;

void parsearDatos(String data) {
  int separador = data.indexOf(',');
  if (separador == -1) return;

  servo_id = data.substring(0, separador).toInt();
  grados   = data.substring(separador + 1).toInt();

  Serial.println("Servo: " + String(servo_id) + " Grados: " + String(grados));

  switch (servo_id) {
    case 1:
      base.write(grados);
      break;

    case 2: {
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

    case 3:
      codo.write(grados);
      break;

    case 4:
      rotatoriomin.write(grados);
      break;

    case 5:
      muneca.write(grados);
      break;

    case 6:
      dedos.write(grados);
      break;

    default:
      Serial.println("Servo no reconocido");
      break;
  }
}

void setup() {
  WRITE_PERI_REG(RTC_CNTL_BROWN_OUT_REG, 0);
  Serial.begin(115200);

  base.attach(pinBase);
  hombro1.attach(pinHombro1);
  hombro2.attach(pinHombro2);
  codo.attach(pinCodo);
  rotatoriomin.attach(pinRotatoriomin);
  muneca.attach(pinMuneca);
  dedos.attach(pinDedos);

  WiFi.begin(ssid, clave);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  server.begin();
  Serial.println("\nConectado. IP: " + WiFi.localIP().toString());
  Serial.println("Servidor listo en puerto " + String(PUERTO));
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

