import rclpy
import sys
import tty
import termios
import select
from rclpy.node import Node
from brazy.msg import Msgcmd

PASO = 10

class TeleopBrazo(Node):
    def __init__(self):
        super().__init__('teleop_brazo')
        self.pub = self.create_publisher(Msgcmd, 'conexion', 10)

        self.posiciones = {
            '1': 90, '2': 90, '3': 90,
            '4': 90, '5': 90, '6': 90
        }

        self.activo = None
        self.create_timer(0.05, self.loop)
        self.get_logger().info('Teleop listo. 1-6 mueve con W/S | 7=awake | 8=sleep | Q=salir')


    def leer_tecla(self):
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
        return ch   
import time

def Mover_obj(self):
    self.activo = None  
    
    self.publicar_accion('5', 180)
    time.sleep(1.0)   

    self.publicar_accion('6', 30)
    time.sleep(1.0)

    self.publicar_accion('6', 50)
    time.sleep(1.0)

    self.publicar_accion('5', 100)
    time.sleep(1.0)

    self.publicar_accion('1', 160)
    time.sleep(1.0)

    self.publicar_accion('5', 180)
    time.sleep(1.0)

    self.publicar_accion('6', 30)
    time.sleep(1.0 )

    self.get_logger().info('Mover_obj completo')
    
    def publicar_accion(self, servo, grados):
        msg = Msgcmd()
        msg.servo  = servo
        msg.grados = grados
        self.pub.publish(msg)

    def loop(self):
        if not select.select([sys.stdin], [], [], 0)[0]:
            return

        tecla = self.leer_tecla()

        # salir
        if tecla == 'q':
            rclpy.shutdown()
            return

        # switch case de selección
        match tecla:
            case '1' | '2' | '3' | '4' | '5' | '6':
                # activa teleop continuo para ese servo
                self.activo = tecla
                self.get_logger().info(f'Servo {tecla} activo — usa W/S para mover')

            case '7':
                # awake — solo publica, no usa W/S
                self.activo = None
                self.publicar_accion('7', 0)
                self.get_logger().info('Awake enviado')

            case '8':
                # sleep — solo publica, no usa W/S
                self.activo = None
                self.publicar_accion('8', 0)
                self.get_logger().info('Sleep enviado')
            case '9':
                #balecito - solo publica, no usa W/S
                self.activo = None
                self.publicar_accion('9',0)
                self.get_logger().info('Dance start')

            case 'w':
                # mueve hacia arriba si hay servo activo
                if self.activo is None:
                    self.get_logger().info('Selecciona un servo primero (1-6)')
                    return
                self.posiciones[self.activo] += PASO
                self.posiciones[self.activo] = min(180, self.posiciones[self.activo])
                self.publicar_accion(self.activo, self.posiciones[self.activo])
                self.get_logger().info(f'Servo {self.activo} → {self.posiciones[self.activo]}°')

            case 's':
                # mueve hacia abajo si hay servo activo
                if self.activo is None:
                    self.get_logger().info('Selecciona un servo primero (1-6)')
                    return
                self.posiciones[self.activo] -= PASO
                self.posiciones[self.activo] = max(0, self.posiciones[self.activo])
                self.publicar_accion(self.activo, self.posiciones[self.activo])
                self.get_logger().info(f'Servo {self.activo} → {self.posiciones[self.activo]}°')

            case _:
                # cualquier otra tecla — ignora
                pass

def main():
    rclpy.init()
    nodo = TeleopBrazo()
    rclpy.spin(nodo)
    nodo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()