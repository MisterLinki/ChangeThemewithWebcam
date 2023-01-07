@echo off

python 2>NUL

if ERRORLEVEL 1 (
    curl "https://python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe" -o open-to-install-python.exe
    open-to-install-python.exe /quiet InstallAllUsers=1 PrependPath=1 
    
    del open-to-install-python.exe
)  

pip install -r requirements.txt

echo ready

pause

:: source for python: https://stackoverflow.com/questions/66913410/install-python-django-in-batch-script
