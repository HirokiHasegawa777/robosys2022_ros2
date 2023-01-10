# SPDX-FileCopyrightText: 2022 Hiroki Hasegawa
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Receiver():
    def __init__(self, node):
        self.pub = node.create_subscription(String, "cryptogram", self.cb, 10)
    def cb(self, msg):
        str = msg.data
        for char in list(str):
            ascii = ord(char)
            num = ascii - 32
            num = (num + self.key) % 96
            ascii = num + 32
            str += chr(ascii)
        print("解読文：", str) 

def main():
    rclpy.init()
    node = Node("receiver")
    receiver = Receiver(node)
    rclpy.spin_once(node)

if __name__ == '__main__':
    main()