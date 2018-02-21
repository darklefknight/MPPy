# BCO

This package is still in alpha phase, therefore please use with caution.
Furthermore it will only work with Python 3!


## News

The package is now installable via PIP.
See section "Installation" for more info.


## Installation

1. Download or clone this directory (green button upper right corner on github)
2. In a terminal navigate to the folder "BCO"
3. run:
```
  >>> python setup.py bdist_wheel
  >>> pip install dist/BCO-?.?.?-py3-none-any.whl 
```

   The ?`s needs to be replaced by the version number.
   
4. check with "pip list" or "conda list" if it worked.

## Documentation

The documentation is at the moment only available on linux machines.

To create the documentation:

1. In a terminal navigate to your downloaded folder "BCO"
2. cd into "docs"
3. run:
```
  >>> make html
```
   Please ignore all the warnings which occur under "checking consistency".
4. if it worked there should be a folder "generated" with some ".rst" files in it now.
    If not, you can remove the the files in generated again with running "make clean".
5. cd into "\_build/html" 
6. open "index.html" with any browser
