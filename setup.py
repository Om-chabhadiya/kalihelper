from setuptools import setup, find_packages

setup(
    name="kalihelper",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "kalihelper=kalihelper.main:main"
        ]
    },
)
