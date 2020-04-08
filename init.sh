#!/bin/sh
pip install --target=src Alfred-Workflow --upgrade
rm -r src/*.dist-info
mkdir src/lib
pip install -r src/requirements.txt --target=src/lib --upgrade
