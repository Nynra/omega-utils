from setuptools import setup

setup(
    name="omega_utils",
    version="0.0.2",
    author="Nynra",
    description="A Python package for common tasks in the OmegaBlockchain project",
    py_modules=["omega_utils"],
    package_dir={"": "src"},
    install_requires=["django", "djangorestframework"],
)