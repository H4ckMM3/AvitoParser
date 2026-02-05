@echo off
cd /d "C:\Users\a.v.kulakov\Desktop\avito_parser_bot"
call .venv\Scripts\activate.bat

:loop
python main.py
echo Следующая проверка через 6 часов...
timeout /t 21600 /nobreak

goto loop
chcp 65001