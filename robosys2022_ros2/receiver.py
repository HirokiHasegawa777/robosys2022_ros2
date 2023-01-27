#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2022 Hiroki Hasegawa
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Receiver():
    def __init__(self, node):
        self.pub = node.create_subscription(String, "chatter", self.cb, 10)
        self.result = ""
    def cb(self, msg):
        str = list(msg.data)
        key = int(str.pop(-1))
        print("秘密鍵：", key)
        for char in str:
            ascii = ord(char)
            num = ascii - 32
            num = (num + key) % 96
            ascii = num + 32
            self.result += chr(ascii)
        print("解読文：", self.result) 

def main():
    rclpy.init()
    node = Node("receiver")
    receiver = Receiver(node)
    rclpy.spin_once(node)

if __name__ == '__main__':
    main()