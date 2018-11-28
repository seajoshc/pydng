import re
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

VERSION = re.search(
    r'^__version__\s*=\s*"(.*)"',
    open('pydng/pydng.py').read(),
    re.M
).group(1)

setuptools.setup(
    name="pydng",
    version=VERSION,
    author="Josh Campbell",
    author_email="josh@userdel.com",
    description="Docker random name generator ported to Python. Just because.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/irlrobot/pydng",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': ['pydng=pydng.pydng:main'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
