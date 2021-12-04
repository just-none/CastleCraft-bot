@echo off
cls
title converting py to exe
pyinstaller --onefile castlecraft.py --i ico.ico
title conversion completed
pause