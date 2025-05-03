from setuptools import setup

package_name = 'jetbot_mirea_teleop'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='firegrock and kostya',
    maintainer_email='firegrock@gmail.com',
    description='Teleoperation node using keyboard for Jetbot_MIREA.',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'listener = jetbot_mirea_teleop.teleop_keyboard:main',
        ],
    },
)
