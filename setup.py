import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hwaddress",
    version='0.0.1',
    author="Eric Geldmacher",
    author_email="egeldmacher@wustl.edu",
    description="Lightweight EUI-48, EUI-64 based hardware address library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ericgeldmacher/hwaddress",
    license="MIT",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
