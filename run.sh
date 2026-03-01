#!/bin/bash

# Activate virtual environment and run the GUI

if [ ! -d ".venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "Please run setup.sh first"
    exit 1
fi

echo "🎮 Starting Super Smash Bros GUI..."
source .venv/bin/activate
python gui.py
