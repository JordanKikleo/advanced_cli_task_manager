from setuptools import setup, find_packages

setup(
    name="task_manager",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "argparse>=1.4.0",
    ],
    python_requires=">=3.6",
) 