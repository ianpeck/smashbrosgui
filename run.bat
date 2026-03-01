@echo off

REM Activate virtual environment and run the GUI

if not exist ".venv\" (
    echo ❌ Virtual environment not found!
    echo Please run setup.bat first
    pause
    exit /b 1
)

echo 🎮 Starting Super Smash Bros GUI...
call .venv\Scripts\activate.bat
python gui.py
