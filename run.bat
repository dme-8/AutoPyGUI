@echo off
if not exist venv (
    python -m venv venv
    call venv\Scripts\activate.bat
    pip install pyautogui
    pip install pynput
) else (
    call venv\Scripts\activate.bat
)

python main.py
rundll32.exe user32.dll,LockWorkStation
pause