# Smash Bros GUI

![alt text](https://user-images.githubusercontent.com/52896859/138405581-1d14a96c-fdec-4867-9b0e-ae5544c6ebc5.png)

A PyQt5 desktop app for viewing head-to-head statistics from a Super Smash Bros database hosted on Amazon RDS. It is filled with data from a WWE-style franchise my brother and I made with SSB characters when we were younger! Some of the data has been manually loaded into my database from a hand written notebook.

The app displays win-loss records across different criteria -- by stage, opponent, match type, season, PPV, brand, and more -- alongside fighter and stage images.

Future plans include an advanced stats tab, statistical graphs, and an ETL tab for loading data directly into Amazon RDS.

## Project Structure

```
smashbrosgui/
├── gui.py                 # PyQt5 UI, database worker thread, app entry point
├── sql.py                 # Database connection and query functions
├── assets/
│   ├── fighters/          # Fighter portrait images
│   ├── stages/            # Stage images
│   └── theme/             # QSS stylesheet (darkeum.qss)
├── requirements.txt       # Python dependencies
├── secrets.env.example    # Template for database credentials
├── setup.bat / .ps1 / .sh # Setup scripts (Windows/Mac/Linux)
├── run.bat / .sh          # Run scripts
└── README.md
```

## Performance

Database queries run in parallel using `ThreadPoolExecutor` -- all 23 stat queries fire simultaneously on separate threads, so results load in roughly the time of one query instead of 23 sequential round-trips.

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- Database access credentials in `secrets.env` file

### Quick Setup

#### On Mac/Linux:
```bash
# 1. Clone the repository
git clone <repo-url>
cd smashbrosgui

# 2. Make setup script executable and run it
chmod +x setup.sh
./setup.sh

# 3. Create secrets.env file with your database credentials
# (see secrets.env.example)

# 4. Run the application
./run.sh
```

#### On Windows:
```batch
REM 1. Clone the repository
git clone <repo-url>
cd smashbrosgui

REM 2. Run setup script (creates venv and installs dependencies)
setup.bat

REM 3. Create secrets.env file with your database credentials
REM (see secrets.env.example)

REM 4. Run the application
run.bat
```

Or use PowerShell:
```powershell
.\setup.ps1
.\.venv\Scripts\Activate.ps1
python gui.py
```

### Manual Setup
```bash
python -m venv .venv

# Mac/Linux:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate

pip install -r requirements.txt
python gui.py
```

### Database Access
This repo's code is available to download but will not work unless your IP is granted SELECT access to the database. Please reach out to me at ianpeck22@gmail.com with your IP and I will add you.

![alt text](https://i.imgur.com/praoCaG.png?1)

https://user-images.githubusercontent.com/52896859/147822317-67d5a072-ad93-4859-a42c-fd1f520d72e9.mov

