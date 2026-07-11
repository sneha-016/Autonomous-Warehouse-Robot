import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():

    aws_world = get_package_share_directory(
        'aws_robomaker_small_warehouse_world'
    )

    gazebo_ros = get_package_share_directory(
        'gazebo_ros'
    )

    world = os.path.join(
        aws_world,
        'worlds',
        'no_roof_small_warehouse',
        'no_roof_small_warehouse.world'
    )

    return LaunchDescription([

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(
                    gazebo_ros,
                    'launch',
                    'gazebo.launch.py'
                )
            ),
            launch_arguments={
                'world': world
            }.items()
        ),

    ])
