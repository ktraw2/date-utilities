from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="date_utilities",
    version="1.0",
    description="Date subtraction, parsing, and random timestamp generation.",
    author="Kevin Traw",
    author_email="ktraw2@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ktraw2/date-utilities",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3.0",
        "Operating System :: OS Independent",
    ],
    requires=["pytz"],
)
