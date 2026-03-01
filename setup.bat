@echo off
echo ================================================
echo 🎮 Super Smash Bros GUI - Setup Script (Windows)
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.7 or higher from python.org
    pause
    exit /b 1
)

echo ✓ Python found
python --version
echo.

REM Create virtual environment
echo 📦 Creating virtual environment...
python -m venv .venv

if errorlevel 1 (
    echo ❌ Failed to create virtual environment
    pause
    exit /b 1
)

echo ✓ Virtual environment created
echo.

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call .venv\Scripts\activate.bat

REM Upgrade pip
echo ⬆️  Upgrading pip...
python -m pip install --upgrade pip

REM Install requirements
echo 📥 Installing dependencies...
pip install -r requirements.txt

if errorlevel 1 (
    echo ❌ Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo ✅ Setup complete!
echo.
echo To activate the virtual environment in the future, run:
echo    .venv\Scripts\activate
echo.
echo To run the application:
echo    python gui.py
echo.
echo To deactivate the virtual environment:
echo    deactivate
echo.
pause
