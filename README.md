# RAS Proyect ¨Brazy¨

The Brazy project is a robotic arm with six degrees of freedom controlled by servomotors through an ESP32 microcontroller using ROS 2 and PlatformIO. The system uses a total of seven servomotors to achieve six independent movements, as the shoulder joint is driven by two parallel servomotors that operate in opposite directions. This configuration provides greater torque, improving the arm's strength and overall performance.

The robotic arm can be controlled using a keyboard through a teleoperation (Teleop) system. Control commands are transmitted from ROS 2 to the ESP32 over a Wi-Fi connection to actuate the different joints, while PlatformIO is used to upload the firmware to the ESP32 via a serial connection.

## Team memebers

Juan Sebastián Moya Perdomo

Lina Sofía Álvarez Martínez

Samuel Arango Hernández

---

## Tools

### Software

* Linux
* ROS 2
* PlatformIO
* Programing lenguges: Arduino, Python y C++
* library ESP32Servo
* Teleop
* GitHub

### Hardware

* ESP32
* 7 servomotors
* Jumper cables
* Arm chassis
* Coputer with Linux
* Three 3.7 V lithium batteries (two 4800 mAh batteries and one 2200 mAh battery)
* 5 V voltage regulator
* Button

## Software requirements

* Ubuntu 24.04
* ROS 2 Jazzy
* PlatformIO
* Visual Studio Code
* Python 3
* Colcon
* Git

## Execution

### ROS 2

* Creación del custom message.
* Configuración de los nodos publicador y suscriptor para la comunicación de ROS 2.

  * Implementación del nodo teleop en el publicador para configurar los grados, aumentar y disminuir.
  * Configuración del suscriptor para la comunicación Wi-Fi con la ESP32.

### PlatformIO

* Switch case para controlar los servos de manera independiente con `s` para disminuir y `w` para aumentar. Además, se implementó una función para guardar (`sleep`) y una para despertar (`awake`) el brazo.
* Control de los servos mediante una función de movimiento grado a grado.
* Comando para que la ESP32 se conecte a Wi-Fi. ********

### Compilation

* *Pendiente*

### Keybord control

Se configuró el teleop para que funcione mediante las teclas de números del 1 al 8, de manera que las primeras 6 controlan los servos independientes y las otras dos activan las funciones de despertar y guardar el brazo.

Los servos se alimentaron con tres baterías de litio de 3.7 V: dos de 4800 mAh y una de 2200 mAh. Estas están conectadas a un botón y a un regulador de voltaje para entregar 5 V a la placa de expansión que alimenta los servos. La ESP32 es alimentada por el computador mediante USB.

* Archivos de lanzamiento para ejecutar el proyecto.
