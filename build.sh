#!/usr/bin/env bash

# Use python 3.10 if it's available (Render often ignores runtime.txt)
python3.10 -m venv venv
source venv/bin/activate

# Upgrade pip and install packages
pip install --upgrade pip
pip install -r requirements.txt
