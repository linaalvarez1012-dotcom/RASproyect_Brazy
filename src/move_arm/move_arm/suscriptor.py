import rclpy
from brazy.msg import Msgcmd

def callback(msg):
    print(f'Servo {msg.servo}, Grados: {msg.grados}')

def main():
    rclpy.init()
    node = rclpy.create_node('control')
    sub = node.create_subscription(Msgcmd,'conexion',callback,10)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()