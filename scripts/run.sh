#!/bin/bash
set -e

export PATH="$(pwd)/venv/bin:$PATH"

python app/index.py