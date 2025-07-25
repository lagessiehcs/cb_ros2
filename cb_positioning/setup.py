from setuptools import setup
from setuptools import find_packages

package_name = 'cb_positioning'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(include=[package_name, package_name + '.*']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='quan',
    maintainer_email='quan.pham@tum.de',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'vision_tasks = cb_positioning.vision_tasks:main',
            'publish_fusion = cb_positioning.publish_fusion:main',
        ],
    },
)
