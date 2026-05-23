import rclpy
from brazy.msg import Msgcmd

global pub
def callback_timer():
    global pub
    msg = Msgcmd()
    msg.servo = input("Servo: ")
    msg.grados = int(input("Grados: "))
    pub.publish(msg)


def main():
    global pub
    rclpy.init()
    node = rclpy.create_node('bridge')
    pub = node.create_publisher(Msgcmd, 'conexion',10)
    node.create_timer(0.5, callback_timer)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()