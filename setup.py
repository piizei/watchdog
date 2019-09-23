import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='watchdog',
    version='0.1',
    scripts=['watchdog'],
    author="Petteri Johansson",
    description="Process watchdog",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/piizei/watchdog",
    install_requires=['psutil', 'python-daemon'],
    packages=['src'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
