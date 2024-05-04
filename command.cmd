
echo. > scores.txt
echo. > final.txt
del /Q /F splited\*.*
python emotion2vec\scripts\test.py
python split.py
python emoji.py