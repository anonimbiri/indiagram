@echo off

rem This script installs multiple Python modules using pip

set modules=requests colorama msvcrt random2 pywin32 beautifulsoup4

for %%i in (%modules%) do (
    echo Installing %%i...
    pip install %%i
)

echo All modules have been installed.
pause
