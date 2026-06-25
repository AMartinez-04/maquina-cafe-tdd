@echo off
python -m unittest discover -s tests -v 2>nul
if %ERRORLEVEL% EQU 0 exit /b 0

py -m unittest discover -s tests -v 2>nul
if %ERRORLEVEL% EQU 0 exit /b 0

"C:\Users\aamb\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" -m unittest discover -s tests -v
