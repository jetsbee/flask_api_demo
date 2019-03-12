#!/bin/sh

cd $(cd "$(dirname "$0")" && pwd)

# Create .env file
echo "proj_path=""$(pwd)" > .env

# Run docker-compose
docker-compose run --rm -p 5000:5000 api bash
