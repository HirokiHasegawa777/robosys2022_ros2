# SPDX-FileCopyrightText: 2022 Hiroki Hasegawa
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Sender():
    def __init__(self, node):
        self.pub = node.create_publisher(String, "chatter", 10)
        self.cryptogram = ""
        with open('/home/hiroki/ros2_ws/src/robosys2022_ros2/robosys2022_ros2/cryptogram.txt','r', encoding='UTF-8') as fp:
            str = fp.read()
        self.key = 9 #秘密鍵を必要に応じて変更（0~9）
        for char in list(str):
            ascii = ord(char)
            num = ascii - 32
            num = (num - self.key) % 96
            ascii = num + 32
            self.cryptogram += chr(ascii)
        print("  暗号文：", self.cryptogram) 
        node.create_timer(2, self.cb)
    def cb(self):
        msg = String()
        self.cryptogram += str(self.key)
        msg.data = self.cryptogram
        self.pub.publish(msg)
        #self.pub.publish(self.key)

def main():
    rclpy.init()
    node = Node("sender")
    sender = Sender(node)
    rclpy.spin_once(node)

if __name__ == '__main__':
    main()