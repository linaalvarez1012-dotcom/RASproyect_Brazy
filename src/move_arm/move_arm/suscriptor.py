import rclpy
import socket
from brazy.msg import Msgcmd

def callback(msg):
    global wifi_config
    datos = f'{msg.servo},{msg.grados}\n'
    wifi_config.sendall(datos.encode('utf-8'))

def wifi_setup(ip = '172.20.10.2', port=8080):
    global wifi_config
    wifi_config = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    wifi_config.connect((ip, port))
    print("Wife setup complete")

def main():
    rclpy.init()
    node = rclpy.create_node('control')
    node.declare_parameter('ip', '172.20.10.2')
    node.declare_parameter('port', 8080)
    ip = node.get_parameter('ip').get_parameter_value().string_value
    port = node.get_parameter('port').get_parameter_value().integer_value
    wifi_setup(ip,port)
    sub = node.create_subscription(Msgcmd,'conexion',callback,10)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()