c:\python25\python wxwsetup.py py2exe
copy wxwclient.exe.manifest dist
copy c:\windows\system32\msvcp71.dll dist
del /Q dist\etc\config-updated.xml
"c:\Program Files\NSIS\makensis.exe" wxwclient.nsi

