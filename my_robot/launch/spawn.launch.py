import os

from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    pkg = get_package_share_directory('my_robot')

    urdf_file = os.path.join(
        pkg,
        'urdf',
        'warehouse_bot.urdf'
    )


    robot_description = open(urdf_file).read()


    return LaunchDescription([


        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[
                {
                    'robot_description': robot_description
                }
            ],
            output='screen'
        ),


        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-entity',
                'warehouse_bot',
                '-file',
                urdf_file,
                '-x',
                '2',
                '-y',
                '2',
                '-z',
                '0.5'
            ],
            output='screen'
        )

    ])

