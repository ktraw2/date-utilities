from distutils.core import setup

setup(
    name="date_utilities",
    version="1.0",
    description="Date subtraction, parsing, and random timestamp generation.",
    author="Kevin Traw",
    author_email="ktraw2@gmail.com",
    url="https://github.com/ktraw2/date_utilities",
    packages=[".", ".tests"],
    requires=["pytz"],
)
