# CPS (Combined Photometric-Spectra python analysis tool)

## Installation
To install the tool
```
$ git clone https://github.com/CPSAstro/cps
$ cd cps
$ pip install .
```

For development, run
```
$ poetry install
```
to install the dependencies

For testing, run 
```
$ poetry run pytest -s test/
```

## Usage
Currently, you have to assign the interested `DataSet` and `Survey` supported by <span style="color:red">*`astroquery`*</span> when you using the package.

