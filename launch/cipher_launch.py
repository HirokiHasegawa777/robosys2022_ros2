# SPDX-FileCopyrightText: 2022 Hiroki Hasegawa
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():
    sender = launch_ros.actions.Node(
        package='robosys2022_ros2',
        executable='sender',
        output='screen'
        )
    receiver = launch_ros.actions.Node(
        package='robosys2022_ros2',
        executable='receiver',
        output='screen'
        )

    return launch.LaunchDescription([sender, receiver])