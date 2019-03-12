#!/bin/sh

cd $(cd "$(dirname "$0")" && pwd)

rm -rf $(pwd)/venv && \
python3 -m venv venv && \
. venv/bin/activate && \
python3 -m pip install --upgrade pip && \
python3 -m pip install --trusted-host pypi.python.org -r $(pwd)/requirements.txt
