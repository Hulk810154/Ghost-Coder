from setuptools import setup, find_packages

setup(
    name="code_generator",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "codegenerator=code_generator.main:main",
        ],
    },
)
