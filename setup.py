from setuptools import find_packages, setup

def get_version():
    version = open("version").read()
    version = version.split("-")[0] if version.endswith("SNAPSHOT") else version
    return version

setup(
    name='wlv',
    version=get_version(),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)