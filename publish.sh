#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo "missing argument"
    exit 2
fi
sudo python3 setup.py clean --all
sudo rm -rf ./dist/
sudo python3 setup.py sdist
if [ $1 == "testpypi" ] 
then
    twine upload --repository-url https://test.pypi.org/legacy/ dist/*
elif [ $1 == "pypi" ] 
then
    twine upload dist/*
else
    echo "invalid destination"
fi
