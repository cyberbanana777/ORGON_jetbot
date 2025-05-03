from setuptools import setup

package_name = 'esp_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='cyberbanana',
    maintainer_email='sasha_grachev2005@mail.ru',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'serial_reader = esp_package.serial_reader:main',
            'serial_sender = esp_package.serial_sender:main',
        ],
    },
)
