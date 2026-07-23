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
* 
  En primera instancia se creo un nuevo tipo de mensaje especial para este proyecto, para poder tener control completo de los tipos de datos enviados en la comunicacion de nodos que se usaran     para la ejecucion del proyecto
  
* Configuración de los nodos publicador y suscriptor.
  
   ### Publicador
  
    ```python
    self.pub = self.create_publisher(Msgcmd, 'conexion', 10)
    ```
    Asi de declaro el nodo encargado de la comunicacion entre la persona que controla el robot y el robot su principal funcion es recibir informacion del teclado o comandos previamente       e       establecidos, para posteriormente publicar esta informacion a un topico,al cual en el comando mencionado inicialmente se le asigno el tipo de mensaje que transportara y el nombre de este, el topico sera el encargado de hacer llegar laa informacion al publicador el cual se encargara del siguiente proceso.

    ### Suscriptor
  
  ```python
  sub = node.create_subscription(Msgcmd,'conexion',callback,10)
  ```
  Asi se declaro el nodo suscriptor el cual es el encargado de recibir el mensaje enviado por el publicador y transportado por el topico, para que por medio de la conexion wifi con la ESP32 establecida al momento de ejecutar el nodo, enviar este mensaje para que la ESP32 realice el movimiento solicitado por la persona que controla el robot desde el nodo publicador.

### PlatformIO

* Conexion del microcontrolador a wifi.
  ```cpp
  WiFi.begin(ssid, clave);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  server.begin();
  Serial.println("\nConectado. IP: " + WiFi.localIP().toString());
  Serial.println("Servidor listo en puerto " + String(PUERTO));
  ```
  Como ya se ha mencionado el microcontrolador usado para este proyecto es la ESP32 la cual por medio de una libreria y los comandos visualizados en las lineas d ecodigo ya mostradas se conecto a wifi para establecer comunicacion con el nodo suscriptor.
  
* Switch case para controlar los servos de manera independiente con `s` para disminuir y `w` para aumentar. Además, se implementó una función para guardar (`sleep`) y una para despertar (`awake`) el brazo.

### Compilation

Como primer paso, desde la raíz del workspace de ROS 2 se ejecuta el comando de compilación `colcon build`, con el fin de generar los archivos de construcción y los ejecutables correspondientes a cada uno de los paquetes creados. Posteriormente, se ejecuta el comando `source install/setup.bash`, el cual carga el entorno del workspace en la terminal, permitiendo que ROS 2 reconozca los paquetes, nodos, mensajes personalizados y demás recursos generados durante la compilación.

```bash
cd Proyecto_ws
colcon build
source install/setup.bash
```
Una vez realizados estos pasos, se procede con la ejecucion de los nodos que conforman este proyecto. En primer lugar se inicia con el nodo encargado de la conexion wifi con la ESP32. Este nodo permanece a la espera de los mensajes publicados en el topico `conexion`.

```bash
ros2 run move_arm ras_subsccriber
```
Posteriormente, se ejecuta el nodo publicador, el cual envia los comandos de movimiento por medio del topico `conexion`.

```bash
ros2 run mover_arm ras_publisher
```

### Execution


### Keybord control

Se configuró el teleop para que funcione mediante las teclas de números del 1 al 8, de manera que las primeras 6 controlan los servos independientes y las otras dos activan las funciones de despertar y guardar el brazo.

Los servos se alimentaron con tres baterías de litio de 3.7 V: dos de 4800 mAh y una de 2200 mAh. Estas están conectadas a un botón y a un regulador de voltaje para entregar 5 V a la placa de expansión que alimenta los servos. La ESP32 es alimentada por el computador mediante USB.

* Archivos de lanzamiento para ejecutar el proyecto.
