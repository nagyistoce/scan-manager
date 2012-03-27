;NSIS Script For SmallwxApp

;Background Colors
BGGradient 0000FF 000000 FFFFFF

;Title Of Your Application
Name "NSOnline Dropbox Application"

;Do A CRC Check
CRCCheck On

;Output File Name
OutFile "DropboxSetup.exe"

;The Default Installation Directory
InstallDir "$PROGRAMFILES\NSOnlineDropbox"

;The text to prompt the user to enter a directory
DirText "Please select the folder below"

Section "Install"
  ;Install Files
  SetOutPath $INSTDIR
  SetCompress Auto
  SetOverwrite IfNewer
  File /r "i:\usr\local\lib\dropbox2\guiclient\dist\*.*"

  ; Write the uninstall keys for Windows
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\NSOnlineDropbox" "DisplayName" "NSOnline Dropbox (remove only)"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\NSOnlineDropbox" "UninstallString" "$INSTDIR\Uninst.exe"
WriteUninstaller "Uninst.exe"
SectionEnd

Section "Shortcuts"
  ;Add Shortcuts
  CreateDirectory "$SMPROGRAMS\NSOnlineDropbox"
  CreateShortCut "$SMPROGRAMS\NSOnlineDropbox\NSOnline Dropbox.lnk" "$INSTDIR\wxwclient.exe" "" "$INSTDIR\wxwclient.exe" 0
  CreateShortCut "$DESKTOP\NSOnline Dropbox.lnk" "$INSTDIR\wxwclient.exe" "" "$INSTDIR\wxwclient.exe" 0
SectionEnd

UninstallText "This will uninstall NSOnline Dropbox from your system"

Section Uninstall
  ;Delete Files
  Delete /REBOOTOK "$INSTDIR\etc\*.*"
  RmDir "$INSTDIR\etc"
  Delete /REBOOTOK "$INSTDIR\*.*"

  ;Delete Start Menu Shortcuts
  Delete "$SMPROGRAMS\NSOnlineDropbox\*.*"
  RmDir "$SMPROGRAMS\NSOnlineDropbox"

  ;Delete Uninstaller And Unistall Registry Entries
  Delete "$INSTDIR\Uninst.exe"
  DeleteRegKey HKEY_LOCAL_MACHINE "SOFTWARE\NSOnlineDropbox"
  DeleteRegKey HKEY_LOCAL_MACHINE "SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\NSOnlineDropbox"
  RMDir "$INSTDIR"
SectionEnd