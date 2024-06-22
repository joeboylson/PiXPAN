#!/bin/sh
set -e

export PATH="$(pwd)/venv/bin:$PATH"

sudo apt update
sudo apt upgrade -y
sudo apt install -y python3-libcamera python3-kms++ libcap-dev python3-picamera2
sudo apt autoremove -y

pip install -r requirements.txt