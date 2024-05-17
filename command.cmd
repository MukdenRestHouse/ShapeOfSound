python audios/handling.py
python upload.py
echo. > output.txt
echo. > scores.txt
echo. > final.txt
del /Q /F splited\*.*
python alibabacloud-nls-python-sdk-dev\transciption.py
python split.py
python emotion2vec\scripts\test.py
python emoji.py