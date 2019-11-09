from setuptools import setup, find_packages  # noqa: H301

NAME = "DroneDelivery"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install

setup(
    name=NAME,
    version=VERSION,
    description="Drone delivery demo project",
    author_email="",
    url="",
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'sphinx'
      ],
    include_package_data=True,
)