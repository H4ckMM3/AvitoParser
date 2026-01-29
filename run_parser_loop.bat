@echo off
cd /d "C:\Users\a.v.kulakov\Desktop\avito_parser_bot"
call .venv\Scripts\activate.bat

:loop
python main.py
echo Следующая проверка через 10 минут...
timeout /t 600 /nobreak

goto loop