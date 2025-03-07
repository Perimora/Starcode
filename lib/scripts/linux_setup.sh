#!/bin/bash

# Define the virtual environment name
VENV_DIR=".venv"
REQUIREMENTS=".binder/requirements.txt"
NOTEBOOK="main.ipynb"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python is not installed. Please install Python first."
    exit 1
fi

# Create the virtual environment if it does not exist
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies from .binder/requirements.txt if available
if [ -f "$REQUIREMENTS" ]; then
    echo "Installing dependencies from $REQUIREMENTS..."
    pip install -r "$REQUIREMENTS"
else
    echo "No $REQUIREMENTS found. Installing Jupyter only..."
    pip install jupyter
fi

# Check if the notebook exists
if [ -f "$NOTEBOOK" ]; then
    echo "Starting Jupyter Notebook with $NOTEBOOK..."
    jupyter notebook "$NOTEBOOK"
else
    echo "Warning: $NOTEBOOK not found. Starting Jupyter without a specific notebook."
    jupyter notebook
fi
