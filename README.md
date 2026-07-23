# RAS Proyect ¨Brazy¨

El proyecto Brazy se trata de un brazo robótico que cuenta con 6 grados de libertad. El brazo es controlado mediante ROS 2, PlatformIO y un microcontrolador ESP32. Utiliza 7 servomotores, ya que el movimiento de los “hombros” es manejado por dos servomotores en paralelo, los cuales se mueven en espejo para mejorar el funcionamiento del brazo.

El proyecto permite el movimiento del robot con el teclado mediante un sistema teleop. Desde ROS 2 se envían comandos de control por Wi-Fi que permiten activar diferentes articulaciones, mientras que PlatformIO carga el código de manera serial a la ESP32.

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
* Lenguajes: Arduino, Python y C++
* Librería ESP32Servo
* Teleop
* GitHub

### Hardware

* ESP32
* 7 servomotores
* Cables jumper
* Carcasa del brazo
* Computador con Linux
* Tres baterías de litio de 3.7 V: dos de 4800 mAh y una de 2200 mAh
* Regulador de voltaje
* Botón

## Requirements

* Ubuntu 24.04
* ROS 2 Jazzy
* PlatformIO
* Visual Studio
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
