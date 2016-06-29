#!/bin/bash

python -m compileall .
zip -r /tmp/n-ary-v1.zip . -x /*.git* /*.py
