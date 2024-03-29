import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="alsong",
    version="0.0.1",
    author="Jayden",
    author_email="cjjunk29@gmail.com",
    description="A Python wrapper for ALSong API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BayernMuller/alsong-time-synced-lyrics",
    install_requires=[
        'pydantic',
        'requests',
        'lxml'
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'alsong=alsong.cli:main',
        ],
    },
)