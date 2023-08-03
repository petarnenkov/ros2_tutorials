from setuptools import find_packages, setup

package_name = 'py_actioncli'

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
    maintainer='user',
    maintainer_email='191wita14@o365.htl-leoben.at',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'server = py_actioncli.fibonacci_action_server:main',
            'client = py_actioncli.fibonacci_action_client:main',
        ],
    },
)
