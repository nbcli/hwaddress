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
    license="GPLv3",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
