from setuptools import find_packages, setup

package_name = 'move_arm'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sebastian',
    maintainer_email='sebastian@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
 entry_points={
        'console_scripts': [
            'ras_publisher = move_arm.publicador:main',
            'ras_subscriber = move_arm.suscriptor:main'
        ],
    },
)
