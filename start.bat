@echo off
setlocal

cd /d "%~dp0"

where py >nul 2>nul
if not errorlevel 1 (
    set "PY_CMD=py -3"
) else (
    set "PY_CMD=python"
)

if not exist venv (
    echo Creation de l'environnement virtuel...
    %PY_CMD% -m venv venv
)

call venv\Scripts\activate.bat

python -m pip install --upgrade pip

if exist requirements.txt (
    echo Installation des dependances du projet...
    pip install -r requirements.txt
)

if exist Documentation\requirements.txt (
    echo Installation des dependances de documentation...
    pip install -r Documentation\requirements.txt
)

echo.
echo Lancement de l'API FastAPI...
python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload

endlocal
