from setuptools import setup, find_packages
import pathlib

# Read the README.md content for the PyPI description
here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="TrekPhysics",  
    version="0.1.0",
    description="A scientific computing module for high-altitude biomechanics and thermodynamics.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MDSAROSHALAM/TrekPhysics.git",  
    author="Sarosh",
    author_email="mdalamsarosh@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Physics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    keywords="physics, trekking, altitude, biomechanics, science",
    packages=find_packages(), 
    python_requires=">=3.6, <4",
    install_requires=["numpy", "matplotlib"], 
)

