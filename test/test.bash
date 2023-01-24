#!/bin/bash
# SPDX-FileCopyrightText: 2022 Hiroki Hasegawa
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
ros2 launch robosys2022_ros2 cipher_launch.py > /tmp/robosys2022_ros2.log

cat /tmp/robosys2022_ros2.log | grep -e "暗号文：" -e "解読文："