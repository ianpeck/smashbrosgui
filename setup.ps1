Write-Host "================================================" -ForegroundColor Cyan
Write-Host "🎮 Super Smash Bros GUI - Setup Script (Windows)" -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python 3.7 or higher from python.org" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""

# Create virtual environment
Write-Host "📦 Creating virtual environment..." -ForegroundColor Yellow
python -m venv .venv

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Failed to create virtual environment" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "✓ Virtual environment created" -ForegroundColor Green
Write-Host ""

# Activate virtual environment
Write-Host "🔧 Activating virtual environment..." -ForegroundColor Yellow
& .\.venv\Scripts\Activate.ps1

# Upgrade pip
Write-Host "⬆️  Upgrading pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip

# Install requirements
Write-Host "📥 Installing dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Failed to install dependencies" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""
Write-Host "✅ Setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "To activate the virtual environment in the future, run:" -ForegroundColor Cyan
Write-Host "   .\.venv\Scripts\Activate.ps1" -ForegroundColor White
Write-Host ""
Write-Host "To run the application:" -ForegroundColor Cyan
Write-Host "   python gui.py" -ForegroundColor White
Write-Host ""
Write-Host "To deactivate the virtual environment:" -ForegroundColor Cyan
Write-Host "   deactivate" -ForegroundColor White
Write-Host ""
Read-Host "Press Enter to exit"
