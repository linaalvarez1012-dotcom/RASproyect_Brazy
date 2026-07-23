# RAS Proyect ¨Brazy¨
![ROS2](https://img.shields.io/badge/ROS2-Jazzy-22314E?logo=ros&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-24.04-E95420?logo=ubuntu&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![PlatformIO](https://img.shields.io/badge/PlatformIO-IDE-F5822A?logo=platformio&logoColor=white)
![ESP32](https://img.shields.io/badge/ESP32-DevKit-blue)

Brazy is a **6-DOF robotic arm** controlled by an **ESP32** microcontroller using **ROS 2 Jazzy** and **PlatformIO**. Although the arm provides six independent degrees of freedom, it is actuated by **seven servo motors**. The shoulder joint is driven by two synchronized servos operating in opposite directions, increasing the  torque and improving the  performance of the movement.

It is based on **ROS 2** communication. User commands are generated through a keyboard teleoperation interface and transmitted to the ESP32 over a **Wi-Fi** connection, where they are interpreted to actuate correspondingly. Firmware development and deployment uses **PlatformIO** via a USB serial connection.

---

## Team memebers

Juan Sebastián Moya Perdomo

Lina Sofía Álvarez Martínez

Samuel Arango Hernández

---

## Tools

### Software

* Ubuntu Linux
* ROS 2
* PlatformIO
* Arduino
* Python
* C++
* ESP32Servo Library
* ROS 2 Teleoperation (Teleop)
* Git & GitHub


### Hardware

* ESP32
* 7 servomotors
* Jumper cables
* Arm chassis
* Coputer with Linux
* Three 3.7 V lithium batteries (2 × 4800 mAh, 1 × 2200 mAh)
* 5 V voltage regulator
* Power switch

## Software requirements

* Ubuntu 24.04
* ROS 2 Jazzy
* PlatformIO
* Visual Studio Code
* Python 3
* Colcon
* Git

---

# Step by step


## ROS 2

### Custom Message

A custom ROS 2 message was created to provide complete control over the data exchanged between the different nodes in the system. This allows the project to transmit all the information required to control the robotic arm while maintaining simple and efficient communication.


### Publisher Node

The publisher node serves as the interface between the operator and the robotic arm. It receives keyboard commands from the teleoperation interface and publishes them to the `conexion` topic using the custom `Msgcmd` message type.

```python
self.pub = self.create_publisher(Msgcmd, 'conexion', 10)
```

### Subscriber Node

The subscriber node listens to the `conexion` topic and receives the commands published by the teleoperation node. Each received message is forwarded to the ESP32 through the Wi-Fi connection, allowing the microcontroller to execute the requested movement.

```python
sub = node.create_subscription(Msgcmd, 'conexion', callback, 10)
```

---

## PlatformIO

### ESP32 Wi-Fi Communication

The ESP32 establishes a Wi-Fi connection to communicate with the ROS 2 subscriber node. Once the connection is established, it continuously waits for incoming commands that will be translated into servo movements.

```cpp
WiFi.begin(ssid, clave);
while (WiFi.status() != WL_CONNECTED) { delay(500);
Serial.print("."); } server.begin();
Serial.println("\nConectado. IP: " + WiFi.localIP().toString());
Serial.println("Servidor listo en puerto " + String(PUERTO));
```

### Servo Control

Each joint is controlled independently using a `switch-case` structure. The `W` key increases the selected joint angle, while the `S` key decreases it with a resolution of one degree per command. Additionally, predefined **Awake** and **Sleep** positions were implemented to initialize or safely store the robotic arm.

---

## Build and Execution

### Build the Workspace

 1. From the ROS2 workspace root: execute the compilation command colcon build.   This, to generate the building and executable files that correspond to each package created. 

  2. Execute the command source install/setup.bash, wich uploads the entorno del workspace in the terminal, allowing the recognition of the packages, nodes, custom messages, among other resources generated during the compilation 

```bash
cd Proyecto_ws
colcon build
source install/setup.bash
```

   3.Execute the nodes: First, the node responsible of the Wifi connection with the ESP32. this node will be expecting the messages published by the node `conexion`.

```bash
ros2 run move_arm ras_subsccriber
```

  4. Execute the publisher node which will send movement commands through the topic connection.

```bash
ros2 run mover_arm ras_publisher
```

---

## Keyboard Teleoperation

The robotic arm is controlled through a keyboard teleoperation interface.

| Key | Function |
|:---:|----------|
| **1 – 6** | Select and control each of the six joints |
| **7** | Move the arm to the **Awake** position |
| **8** | Move the arm to the **Sleep** position |
| **W** | Increase the selected joint angle |
| **S** | Decrease the selected joint angle |

---

## Power Supply

The servo motors are powered by three **3.7 V lithium batteries** (two **4800 mAh** batteries and one **2200 mAh** battery). The batteries are connected through a power switch and a **5 V voltage regulator**, which supplies the servo expansion board.

The ESP32 is powered independently via the computer's USB connection during programming and operation.
