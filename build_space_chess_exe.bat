@echo off
echo ================================================
echo    Building 5x5x5 Space Chess .exe
echo ================================================

pip install pyinstaller --upgrade

pyinstaller --onefile --name "5x5x5_Space_Chess" --icon NONE \
    --add-data "README.md;." space_chess_5x5x5.py

echo.
echo Build finished!
echo Look in the 'dist' folder for 5x5x5_Space_Chess.exe
pause