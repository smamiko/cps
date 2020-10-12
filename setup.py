import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cps", # Replace with your own username
    version="0.0.1",
    author="Paul Chi-Yan Law",
    author_email="a252461@gmail.com",
    description="Combined Photometric-Spectra python analysis tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CPSAstro/cps",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPLv3 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
