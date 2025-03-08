# Define the virtual environment name
$venvName = ".venv"
$requirements = ".binder/requirements.txt"

# Check if Python is installed
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python is not installed. Please install Python first." -ForegroundColor Red
    exit
}

# Create the virtual environment if it does not exist
if (-not (Test-Path $venvName)) {
    Write-Host "Creating virtual environment..."
    python -m venv $venvName
}

# Activate the virtual environment
Write-Host "Activating virtual environment..."
$venvActivate = ".\$venvName\Scripts\Activate.ps1"
if (Test-Path $venvActivate) {
    & $venvActivate
} else {
    Write-Host "Error: Activation script not found!" -ForegroundColor Red
    exit
}

# Upgrade pip
Write-Host "Upgrading pip..."
python -m pip install --upgrade pip

# Install dependencies from requirements.txt if available
if (Test-Path $requirements) {
    Write-Host "Installing dependencies from requirements.txt..."
    pip install -r $requirements
} else {
    Write-Host "No requirements.txt found. Installing Jupyter only..."
    pip install jupyter
}

# Ensure the script runs from its own directory
Set-Location -Path $PSScriptRoot

# Define the path to the notebook (adjust if needed)
$NotebookPath = "$PSScriptRoot\..\..\main.ipynb"

# Start Jupyter Notebook with the specific file
Write-Host "Starting Jupyter Notebook with main.ipynb..."
Start-Process "jupyter" -ArgumentList "notebook `"$NotebookPath`"" -NoNewWindow

