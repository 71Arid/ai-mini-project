#!/bin/bash

# Create virtual environment
python3 -m venv venv

# Activate venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

echo "Setup complete. Run 'source venv/bin/activate' to activate the environment."