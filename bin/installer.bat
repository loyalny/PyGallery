pip3 install -r ../requirements.txt

pyinstaller --noconsole --onefile --name="PyGallery" --icon=..\src\gui\icons\pygallery.ico ..\src\python\main.py

pause
