#!/bin/sh

cd $(cd "$(dirname "$0")" && pwd)

. venv/bin/activate
export FLASK_ENV=testing
pytest -s -v --tb=short
