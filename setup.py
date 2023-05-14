"""Copyright 2023-present stngularity

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

import re
from setuptools import setup, find_packages

def read_requirements(file):
    """List[:class:`str`]: Reads specified in :param:`file` requirements
    
    Parameters
    ----------
    file: :class:`str`
        The filename of any requirements.txt"""
    with open(file, "r", encoding="utf-8") as reader:
        return [l for l in reader.read().splitlines() if not l.startswith("#")]

VERSION = ""
with open("src/toapi/__init__.py", "r", encoding="utf-8") as reader:
    found = re.search(r"^__version__\s*=\s*\"([^\"]*)\"", reader.read(), re.M)
    if found is None:
        raise RuntimeError("__version__ of project is not specified")

    VERSION = found.group(1)

README = ""
with open("README.md", "r", encoding="utf-8") as reader:
    README = reader.read()

if __name__ == "__main__":
    setup(
        name="tankio_api",
        version=VERSION,
        author="stngularity",
        author_email="stngularity@gmail.com",
        keywords=["game", "api", "to", "tanki online"],
        license="MIT",
        packages=find_packages("src", include=["toapi*"]),

        description="A Python written wrapper for the Tanki Online game API",
        long_description=README,
        long_description_content_type="text/markdown",

        url="https://github.com/stngularity/tankioapi.py",
        project_urls={
            "Homepage": "https://github.com/stngularity/tankioapi.py",
            "Source Code": "https://github.com/stngularity/tankioapi.py",
            "Changelog": "https://github.com/stngularity/tankioapi.py/blob/main/CHANGELOG.md",
            "Bug Tracker": "https://github.com/stngularity/tankioapi.py/issues"
        },

        python_requires=">=3.8",
        install_requires=read_requirements("requirements.txt"),
        extras_require={
            "speedup": read_requirements("requirements/speedup.txt"),
            "dev": read_requirements("requirements/dev.txt")
        },

        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3 :: Only",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: Implementation :: CPython",
            "Topic :: Utilities",
            "Typing :: Typed"
        ]
    )
