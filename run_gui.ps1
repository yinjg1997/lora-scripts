$Env:HF_HOME = "huggingface"
$Env:PYTHONUTF8 = "1"

if (Test-Path -Path "venv\Scripts\activate") {
    Write-Host -ForegroundColor green "Activating virtual environment..."
    .\venv\Scripts\activate
}
elseif (Test-Path -Path "python\python.exe") {
    Write-Host -ForegroundColor green "Using python from python folder..."
}
else {
    Write-Host -ForegroundColor Blue "No virtual environment found, using system python..."
}

python gui.py