from pathlib import Path
from setuptools import find_packages, setup

CURRENT_DIR = Path(__file__).parent
NAME = "invocations"
DESCRIPTION = ""
URL = "https://github.com/ohjeah/cartesian"
EMAIL = "info@markusqua.de"
AUTHOR = "Markus Quade"
PYTHON = ">=3.6"
LICENSE = "MIT"
with open(CURRENT_DIR / "requirements.txt", "r") as f:
    REQUIRED = f.readlines()
with open(CURRENT_DIR / "README.md", "r", encoding="utf8") as f:
    LONG_DESCRIPTION = f.read()
setup(
    name=NAME,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=["test", "example"]),
    install_requires=REQUIRED,
    python_requires=PYTHON,
    license=LICENSE,
)
