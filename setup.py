"""
@Author: Rqk
@Date: 2021-05-22
@Description:
"""

from setuptools import setup, find_packages

version = "0.0.1"
setup(
    name="pyhuolala",
    version=version,
    keywords=[
        "huolala",
    ],
    description="",
    long_description="",
    license="MIT Licence",
    url="https://github.com/renqiukai/pyhuolala",
    author="Renqiukai",
    author_email="renqiukai@qq.com",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=["requests", "loguru"],
)
