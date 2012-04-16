
Name "ScanManager 0.4.1"
OutFile "scanmanager-setup-windows-x86-0.4.1.exe"
InstallDir "$PROGRAMFILES\ScanManager"
InstallDirRegKey HKLM "Software\ScanManager" "Install_Dir"
RequestExecutionLevel admin
Icon "scanmanager.ico"

Page components
Page directory
Page instfiles

UninstPage uninstConfirm
UninstPage instfiles

Section "ScanManager (required)"

    SectionIn RO

    ; Set output path to the installation directory.
    SetOutPath $INSTDIR

    File "/oname=API-MS-Win-Core-LocalRegistry-L1-1-0.dll" "dist\API-MS-Win-Core-LocalRegistry-L1-1-0.dll"
    File "/oname=API-MS-Win-Core-ProcessThreads-L1-1-0.dll" "dist\API-MS-Win-Core-ProcessThreads-L1-1-0.dll"
    File "/oname=API-MS-Win-Security-Base-L1-1-0.dll" "dist\API-MS-Win-Security-Base-L1-1-0.dll"
    File "/oname=AVICAP32.dll" "dist\AVICAP32.dll"
    File "/oname=AVIFIL32.dll" "dist\AVIFIL32.dll"
    File "/oname=MPR.dll" "dist\MPR.dll"
    File "/oname=MSACM32.dll" "dist\MSACM32.dll"
    File "/oname=MSVFW32.dll" "dist\MSVFW32.dll"
    File "/oname=POWRPROF.dll" "dist\POWRPROF.dll"
    File "/oname=PySide.QtCore.pyd" "dist\PySide.QtCore.pyd"
    File "/oname=PySide.QtGui.pyd" "dist\PySide.QtGui.pyd"
    File "/oname=PySide.QtNetwork.pyd" "dist\PySide.QtNetwork.pyd"
    File "/oname=QtCore4.dll" "dist\QtCore4.dll"
    File "/oname=QtGui4.dll" "dist\QtGui4.dll"
    File "/oname=QtNetwork4.dll" "dist\QtNetwork4.dll"
    File "/oname=_bsddb.pyd" "dist\_bsddb.pyd"
    File "/oname=_ctypes.pyd" "dist\_ctypes.pyd"
    File "/oname=_hashlib.pyd" "dist\_hashlib.pyd"
    File "/oname=_socket.pyd" "dist\_socket.pyd"
    File "/oname=_ssl.pyd" "dist\_ssl.pyd"
    File "/oname=_win32sysloader.pyd" "dist\_win32sysloader.pyd"
    File "/oname=bz2.pyd" "dist\bz2.pyd"
    File "/oname=cv2.pyd" "dist\cv2.pyd"
    CreateDirectory "$INSTDIR\imageformats"
    File "/oname=imageformats\qgif4.dll" "dist\imageformats\qgif4.dll"
    File "/oname=imageformats\qico4.dll" "dist\imageformats\qico4.dll"
    File "/oname=imageformats\qjpeg4.dll" "dist\imageformats\qjpeg4.dll"
    File "/oname=imageformats\qmng4.dll" "dist\imageformats\qmng4.dll"
    File "/oname=imageformats\qsvg4.dll" "dist\imageformats\qsvg4.dll"
    File "/oname=imageformats\qtiff4.dll" "dist\imageformats\qtiff4.dll"
    File "/oname=library.zip" "dist\library.zip"
    File "/oname=numpy.core._dotblas.pyd" "dist\numpy.core._dotblas.pyd"
    File "/oname=numpy.core._sort.pyd" "dist\numpy.core._sort.pyd"
    File "/oname=numpy.core.multiarray.pyd" "dist\numpy.core.multiarray.pyd"
    File "/oname=numpy.core.scalarmath.pyd" "dist\numpy.core.scalarmath.pyd"
    File "/oname=numpy.core.umath.pyd" "dist\numpy.core.umath.pyd"
    File "/oname=numpy.fft.fftpack_lite.pyd" "dist\numpy.fft.fftpack_lite.pyd"
    File "/oname=numpy.lib._compiled_base.pyd" "dist\numpy.lib._compiled_base.pyd"
    File "/oname=numpy.linalg.lapack_lite.pyd" "dist\numpy.linalg.lapack_lite.pyd"
    File "/oname=numpy.random.mtrand.pyd" "dist\numpy.random.mtrand.pyd"
    File "/oname=pyexpat.pyd" "dist\pyexpat.pyd"
    File "/oname=pyside-python2.7.dll" "dist\pyside-python2.7.dll"
    File "/oname=python27.dll" "dist\python27.dll"
    File "/oname=pythoncom27.dll" "dist\pythoncom27.dll"
    File "/oname=pywintypes27.dll" "dist\pywintypes27.dll"
    File "/oname=scanmanager.exe" "dist\scanmanager.exe"
    File "/oname=select.pyd" "dist\select.pyd"
    File "/oname=shiboken-python2.7.dll" "dist\shiboken-python2.7.dll"
    File "/oname=unicodedata.pyd" "dist\unicodedata.pyd"
    File "/oname=w9xpopen.exe" "dist\w9xpopen.exe"
    File "/oname=win32api.pyd" "dist\win32api.pyd"
    File "/oname=win32evtlog.pyd" "dist\win32evtlog.pyd"
    File "/oname=win32pdh.pyd" "dist\win32pdh.pyd"
    File "/oname=win32pipe.pyd" "dist\win32pipe.pyd"
    File "/oname=win32trace.pyd" "dist\win32trace.pyd"
    File "/oname=win32ui.pyd" "dist\win32ui.pyd"
    File "/oname=win32wnet.pyd" "dist\win32wnet.pyd"
    CreateDirectory "$INSTDIR\backend"
    CreateDirectory "$INSTDIR\backend\canonpsrec"
    File "/oname=backend\canonpsrec\PRLIB.dll" "dist\backend\canonpsrec\PRLIB.dll"
    File "/oname=backend\canonpsrec\PRSDK.dll" "dist\backend\canonpsrec\PRSDK.dll"
    CreateDirectory "$INSTDIR\backend\libgphoto2"
    File "/oname=backend\libgphoto2\__init__.py" "dist\backend\libgphoto2\__init__.py"
    File "/oname=backend\libgphoto2\api.py" "dist\backend\libgphoto2\api.py"
    File "/oname=backend\libgphoto2\constants.py" "dist\backend\libgphoto2\constants.py"
    File "/oname=backend\libgphoto2\ptp.py" "dist\backend\libgphoto2\ptp.py"
    CreateDirectory "$INSTDIR\backend\libgphoto2\remote"
    File "/oname=backend\libgphoto2\remote\__init__.py" "dist\backend\libgphoto2\remote\__init__.py"
    CreateDirectory "$INSTDIR\backend\libgphoto2\remote\bin"
    File "/oname=backend\libgphoto2\remote\bin\_bisect.dll" "dist\backend\libgphoto2\remote\bin\_bisect.dll"
    File "/oname=backend\libgphoto2\remote\bin\_bytesio.dll" "dist\backend\libgphoto2\remote\bin\_bytesio.dll"
    File "/oname=backend\libgphoto2\remote\bin\_codecs_cn.dll" "dist\backend\libgphoto2\remote\bin\_codecs_cn.dll"
    File "/oname=backend\libgphoto2\remote\bin\_codecs_hk.dll" "dist\backend\libgphoto2\remote\bin\_codecs_hk.dll"
    File "/oname=backend\libgphoto2\remote\bin\_codecs_iso2022.dll" "dist\backend\libgphoto2\remote\bin\_codecs_iso2022.dll"
    File "/oname=backend\libgphoto2\remote\bin\_codecs_jp.dll" "dist\backend\libgphoto2\remote\bin\_codecs_jp.dll"
    File "/oname=backend\libgphoto2\remote\bin\_codecs_kr.dll" "dist\backend\libgphoto2\remote\bin\_codecs_kr.dll"
    File "/oname=backend\libgphoto2\remote\bin\_codecs_tw.dll" "dist\backend\libgphoto2\remote\bin\_codecs_tw.dll"
    File "/oname=backend\libgphoto2\remote\bin\_collections.dll" "dist\backend\libgphoto2\remote\bin\_collections.dll"
    File "/oname=backend\libgphoto2\remote\bin\_ctypes.dll" "dist\backend\libgphoto2\remote\bin\_ctypes.dll"
    File "/oname=backend\libgphoto2\remote\bin\_fileio.dll" "dist\backend\libgphoto2\remote\bin\_fileio.dll"
    File "/oname=backend\libgphoto2\remote\bin\_functools.dll" "dist\backend\libgphoto2\remote\bin\_functools.dll"
    File "/oname=backend\libgphoto2\remote\bin\_hashlib.dll" "dist\backend\libgphoto2\remote\bin\_hashlib.dll"
    File "/oname=backend\libgphoto2\remote\bin\_heapq.dll" "dist\backend\libgphoto2\remote\bin\_heapq.dll"
    File "/oname=backend\libgphoto2\remote\bin\_locale.dll" "dist\backend\libgphoto2\remote\bin\_locale.dll"
    File "/oname=backend\libgphoto2\remote\bin\_multibytecodec.dll" "dist\backend\libgphoto2\remote\bin\_multibytecodec.dll"
    File "/oname=backend\libgphoto2\remote\bin\_random.dll" "dist\backend\libgphoto2\remote\bin\_random.dll"
    File "/oname=backend\libgphoto2\remote\bin\_socket.dll" "dist\backend\libgphoto2\remote\bin\_socket.dll"
    File "/oname=backend\libgphoto2\remote\bin\_ssl.dll" "dist\backend\libgphoto2\remote\bin\_ssl.dll"
    File "/oname=backend\libgphoto2\remote\bin\_struct.dll" "dist\backend\libgphoto2\remote\bin\_struct.dll"
    File "/oname=backend\libgphoto2\remote\bin\_weakref.dll" "dist\backend\libgphoto2\remote\bin\_weakref.dll"
    File "/oname=backend\libgphoto2\remote\bin\array.dll" "dist\backend\libgphoto2\remote\bin\array.dll"
    File "/oname=backend\libgphoto2\remote\bin\binascii.dll" "dist\backend\libgphoto2\remote\bin\binascii.dll"
    File "/oname=backend\libgphoto2\remote\bin\bz2.dll" "dist\backend\libgphoto2\remote\bin\bz2.dll"
    File "/oname=backend\libgphoto2\remote\bin\cPickle.dll" "dist\backend\libgphoto2\remote\bin\cPickle.dll"
    File "/oname=backend\libgphoto2\remote\bin\cStringIO.dll" "dist\backend\libgphoto2\remote\bin\cStringIO.dll"
    File "/oname=backend\libgphoto2\remote\bin\cygbz2-1.dll" "dist\backend\libgphoto2\remote\bin\cygbz2-1.dll"
    File "/oname=backend\libgphoto2\remote\bin\cygcrypto-0.9.8.dll" "dist\backend\libgphoto2\remote\bin\cygcrypto-0.9.8.dll"
    File "/oname=backend\libgphoto2\remote\bin\cygffi-4.dll" "dist\backend\libgphoto2\remote\bin\cygffi-4.dll"
    File "/oname=backend\libgphoto2\remote\bin\cyggcc_s-1.dll" "dist\backend\libgphoto2\remote\bin\cyggcc_s-1.dll"
    File "/oname=backend\libgphoto2\remote\bin\cygiconv-2.dll" "dist\backend\libgphoto2\remote\bin\cygiconv-2.dll"
    File "/oname=backend\libgphoto2\remote\bin\cygintl-8.dll" "dist\backend\libgphoto2\remote\bin\cygintl-8.dll"
    File "/oname=backend\libgphoto2\remote\bin\cygncursesw-10.dll" "dist\backend\libgphoto2\remote\bin\cygncursesw-10.dll"
    File "/oname=backend\libgphoto2\remote\bin\cygreadline7.dll" "dist\backend\libgphoto2\remote\bin\cygreadline7.dll"
    File "/oname=backend\libgphoto2\remote\bin\cygssl-0.9.8.dll" "dist\backend\libgphoto2\remote\bin\cygssl-0.9.8.dll"
    File "/oname=backend\libgphoto2\remote\bin\cygwin1.dll" "dist\backend\libgphoto2\remote\bin\cygwin1.dll"
    File "/oname=backend\libgphoto2\remote\bin\cygz.dll" "dist\backend\libgphoto2\remote\bin\cygz.dll"
    File "/oname=backend\libgphoto2\remote\bin\datetime.dll" "dist\backend\libgphoto2\remote\bin\datetime.dll"
    File "/oname=backend\libgphoto2\remote\bin\fcntl.dll" "dist\backend\libgphoto2\remote\bin\fcntl.dll"
    File "/oname=backend\libgphoto2\remote\bin\gphotoremote.exe" "dist\backend\libgphoto2\remote\bin\gphotoremote.exe"
    File "/oname=backend\libgphoto2\remote\bin\gphotoremote.exe.manifest" "dist\backend\libgphoto2\remote\bin\gphotoremote.exe.manifest"
    File "/oname=backend\libgphoto2\remote\bin\itertools.dll" "dist\backend\libgphoto2\remote\bin\itertools.dll"
    File "/oname=backend\libgphoto2\remote\bin\libpython2.6.dll" "dist\backend\libgphoto2\remote\bin\libpython2.6.dll"
    File "/oname=backend\libgphoto2\remote\bin\math.dll" "dist\backend\libgphoto2\remote\bin\math.dll"
    File "/oname=backend\libgphoto2\remote\bin\operator.dll" "dist\backend\libgphoto2\remote\bin\operator.dll"
    File "/oname=backend\libgphoto2\remote\bin\readline.dll" "dist\backend\libgphoto2\remote\bin\readline.dll"
    File "/oname=backend\libgphoto2\remote\bin\select.dll" "dist\backend\libgphoto2\remote\bin\select.dll"
    File "/oname=backend\libgphoto2\remote\bin\strop.dll" "dist\backend\libgphoto2\remote\bin\strop.dll"
    File "/oname=backend\libgphoto2\remote\bin\termios.dll" "dist\backend\libgphoto2\remote\bin\termios.dll"
    File "/oname=backend\libgphoto2\remote\bin\time.dll" "dist\backend\libgphoto2\remote\bin\time.dll"
    File "/oname=backend\libgphoto2\remote\bin\unicodedata.dll" "dist\backend\libgphoto2\remote\bin\unicodedata.dll"
    File "/oname=backend\libgphoto2\remote\bin\uri.txt" "dist\backend\libgphoto2\remote\bin\uri.txt"
    File "/oname=backend\libgphoto2\remote\bin\zlib.dll" "dist\backend\libgphoto2\remote\bin\zlib.dll"
    File "/oname=backend\libgphoto2\remote\client.py" "dist\backend\libgphoto2\remote\client.py"
    File "/oname=backend\libgphoto2\remote\server.py" "dist\backend\libgphoto2\remote\server.py"
    File "/oname=backend\libgphoto2\structures.py" "dist\backend\libgphoto2\structures.py"
    File "/oname=backend\libgphoto2\test-api.py" "dist\backend\libgphoto2\test-api.py"
    CreateDirectory "$INSTDIR\backend\libgphoto2\win32"
    File "/oname=backend\libgphoto2\win32\README.txt" "dist\backend\libgphoto2\win32\README.txt"
    CreateDirectory "$INSTDIR\backend\libgphoto2\win32\camlibs"
    File "/oname=backend\libgphoto2\win32\camlibs\adc65.dll" "dist\backend\libgphoto2\win32\camlibs\adc65.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\agfa_cl20.dll" "dist\backend\libgphoto2\win32\camlibs\agfa_cl20.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\aox.dll" "dist\backend\libgphoto2\win32\camlibs\aox.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\ax203.dll" "dist\backend\libgphoto2\win32\camlibs\ax203.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\barbie.dll" "dist\backend\libgphoto2\win32\camlibs\barbie.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\canon.dll" "dist\backend\libgphoto2\win32\camlibs\canon.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\casio_qv.dll" "dist\backend\libgphoto2\win32\camlibs\casio_qv.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\clicksmart310.dll" "dist\backend\libgphoto2\win32\camlibs\clicksmart310.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\digigr8.dll" "dist\backend\libgphoto2\win32\camlibs\digigr8.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\digita.dll" "dist\backend\libgphoto2\win32\camlibs\digita.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\dimagev.dll" "dist\backend\libgphoto2\win32\camlibs\dimagev.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\dimera3500.dll" "dist\backend\libgphoto2\win32\camlibs\dimera3500.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\directory.dll" "dist\backend\libgphoto2\win32\camlibs\directory.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\enigma13.dll" "dist\backend\libgphoto2\win32\camlibs\enigma13.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\fuji.dll" "dist\backend\libgphoto2\win32\camlibs\fuji.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\gsmart300.dll" "dist\backend\libgphoto2\win32\camlibs\gsmart300.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\hp215.dll" "dist\backend\libgphoto2\win32\camlibs\hp215.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\iclick.dll" "dist\backend\libgphoto2\win32\camlibs\iclick.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\jamcam.dll" "dist\backend\libgphoto2\win32\camlibs\jamcam.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\jd11.dll" "dist\backend\libgphoto2\win32\camlibs\jd11.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\jl2005a.dll" "dist\backend\libgphoto2\win32\camlibs\jl2005a.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\jl2005c.dll" "dist\backend\libgphoto2\win32\camlibs\jl2005c.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\kodak_dc120.dll" "dist\backend\libgphoto2\win32\camlibs\kodak_dc120.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\kodak_dc210.dll" "dist\backend\libgphoto2\win32\camlibs\kodak_dc210.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\kodak_dc240.dll" "dist\backend\libgphoto2\win32\camlibs\kodak_dc240.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\kodak_dc3200.dll" "dist\backend\libgphoto2\win32\camlibs\kodak_dc3200.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\kodak_ez200.dll" "dist\backend\libgphoto2\win32\camlibs\kodak_ez200.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\konica.dll" "dist\backend\libgphoto2\win32\camlibs\konica.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\konica_qm150.dll" "dist\backend\libgphoto2\win32\camlibs\konica_qm150.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\largan.dll" "dist\backend\libgphoto2\win32\camlibs\largan.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\lg_gsm.dll" "dist\backend\libgphoto2\win32\camlibs\lg_gsm.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\mars.dll" "dist\backend\libgphoto2\win32\camlibs\mars.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\mustek.dll" "dist\backend\libgphoto2\win32\camlibs\mustek.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\panasonic_coolshot.dll" "dist\backend\libgphoto2\win32\camlibs\panasonic_coolshot.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\panasonic_dc1000.dll" "dist\backend\libgphoto2\win32\camlibs\panasonic_dc1000.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\panasonic_dc1580.dll" "dist\backend\libgphoto2\win32\camlibs\panasonic_dc1580.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\panasonic_l859.dll" "dist\backend\libgphoto2\win32\camlibs\panasonic_l859.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\pccam300.dll" "dist\backend\libgphoto2\win32\camlibs\pccam300.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\pccam600.dll" "dist\backend\libgphoto2\win32\camlibs\pccam600.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\polaroid_pdc320.dll" "dist\backend\libgphoto2\win32\camlibs\polaroid_pdc320.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\polaroid_pdc640.dll" "dist\backend\libgphoto2\win32\camlibs\polaroid_pdc640.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\polaroid_pdc700.dll" "dist\backend\libgphoto2\win32\camlibs\polaroid_pdc700.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\ptp2.dll" "dist\backend\libgphoto2\win32\camlibs\ptp2.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\ricoh.dll" "dist\backend\libgphoto2\win32\camlibs\ricoh.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\ricoh_g3.dll" "dist\backend\libgphoto2\win32\camlibs\ricoh_g3.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\samsung.dll" "dist\backend\libgphoto2\win32\camlibs\samsung.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\sierra.dll" "dist\backend\libgphoto2\win32\camlibs\sierra.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\sipix_blink2.dll" "dist\backend\libgphoto2\win32\camlibs\sipix_blink2.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\sipix_web2.dll" "dist\backend\libgphoto2\win32\camlibs\sipix_web2.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\smal.dll" "dist\backend\libgphoto2\win32\camlibs\smal.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\sonix.dll" "dist\backend\libgphoto2\win32\camlibs\sonix.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\sony_dscf1.dll" "dist\backend\libgphoto2\win32\camlibs\sony_dscf1.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\sony_dscf55.dll" "dist\backend\libgphoto2\win32\camlibs\sony_dscf55.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\soundvision.dll" "dist\backend\libgphoto2\win32\camlibs\soundvision.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\spca50x.dll" "dist\backend\libgphoto2\win32\camlibs\spca50x.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\sq905.dll" "dist\backend\libgphoto2\win32\camlibs\sq905.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\st2205.dll" "dist\backend\libgphoto2\win32\camlibs\st2205.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\stv0674.dll" "dist\backend\libgphoto2\win32\camlibs\stv0674.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\stv0680.dll" "dist\backend\libgphoto2\win32\camlibs\stv0680.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\sx330z.dll" "dist\backend\libgphoto2\win32\camlibs\sx330z.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\topfield.dll" "dist\backend\libgphoto2\win32\camlibs\topfield.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\toshiba_pdrm11.dll" "dist\backend\libgphoto2\win32\camlibs\toshiba_pdrm11.dll"
    File "/oname=backend\libgphoto2\win32\camlibs\tp6801.dll" "dist\backend\libgphoto2\win32\camlibs\tp6801.dll"
    File "/oname=backend\libgphoto2\win32\cygexif-12.dll" "dist\backend\libgphoto2\win32\cygexif-12.dll"
    File "/oname=backend\libgphoto2\win32\cyggcc_s-1.dll" "dist\backend\libgphoto2\win32\cyggcc_s-1.dll"
    File "/oname=backend\libgphoto2\win32\cyggphoto2-2.dll" "dist\backend\libgphoto2\win32\cyggphoto2-2.dll"
    File "/oname=backend\libgphoto2\win32\cyggphoto2_port-0.dll" "dist\backend\libgphoto2\win32\cyggphoto2_port-0.dll"
    File "/oname=backend\libgphoto2\win32\cygiconv-2.dll" "dist\backend\libgphoto2\win32\cygiconv-2.dll"
    File "/oname=backend\libgphoto2\win32\cygintl-8.dll" "dist\backend\libgphoto2\win32\cygintl-8.dll"
    File "/oname=backend\libgphoto2\win32\cygltdl-7.dll" "dist\backend\libgphoto2\win32\cygltdl-7.dll"
    File "/oname=backend\libgphoto2\win32\cygpopt-0.dll" "dist\backend\libgphoto2\win32\cygpopt-0.dll"
    File "/oname=backend\libgphoto2\win32\cygusb0.dll" "dist\backend\libgphoto2\win32\cygusb0.dll"
    File "/oname=backend\libgphoto2\win32\cygwin1.dll" "dist\backend\libgphoto2\win32\cygwin1.dll"
    File "/oname=backend\libgphoto2\win32\gphoto2.bat" "dist\backend\libgphoto2\win32\gphoto2.bat"
    File "/oname=backend\libgphoto2\win32\gphoto2.exe" "dist\backend\libgphoto2\win32\gphoto2.exe"
    CreateDirectory "$INSTDIR\backend\libgphoto2\win32\iolibs"
    File "/oname=backend\libgphoto2\win32\iolibs\disk.dll" "dist\backend\libgphoto2\win32\iolibs\disk.dll"
    File "/oname=backend\libgphoto2\win32\iolibs\ptpip.dll" "dist\backend\libgphoto2\win32\iolibs\ptpip.dll"
    File "/oname=backend\libgphoto2\win32\iolibs\serial.dll" "dist\backend\libgphoto2\win32\iolibs\serial.dll"
    File "/oname=backend\libgphoto2\win32\iolibs\usb.dll" "dist\backend\libgphoto2\win32\iolibs\usb.dll"
    File "/oname=backend\libgphoto2\win32\iolibs\usb1.dll" "dist\backend\libgphoto2\win32\iolibs\usb1.dll"
    File "/oname=backend\libgphoto2\win32\iolibs\usbdiskdirect.dll" "dist\backend\libgphoto2\win32\iolibs\usbdiskdirect.dll"
    File "/oname=backend\libgphoto2\win32\iolibs\usbscsi.dll" "dist\backend\libgphoto2\win32\iolibs\usbscsi.dll"
    File "/oname=backend\libgphoto2\wrapper.py" "dist\backend\libgphoto2\wrapper.py"
    CreateDirectory "$INSTDIR\backend\nikonsdk"
    File "/oname=backend\nikonsdk\D80_Mod.md3" "dist\backend\nikonsdk\D80_Mod.md3"
    File "/oname=backend\nikonsdk\NkdPTP.dll" "dist\backend\nikonsdk\NkdPTP.dll"
    File "/oname=backend\nikonsdk\NkdPTPDi.dll" "dist\backend\nikonsdk\NkdPTPDi.dll"

    
    CreateDirectory "$SMPROGRAMS\ScanManager"
    CreateShortCut "$SMPROGRAMS\ScanManager\ScanManager.lnk" "$INSTDIR\scanmanager.exe" "" "$INSTDIR\scanmanager.exe" 0
    CreateShortCut "$SMPROGRAMS\ScanManager\Uninstall.lnk" "$INSTDIR\uninstall.exe" "" "$INSTDIR\uninstall.exe" 0

    ; Create an uninstaller
    WriteUninstaller "uninstall.exe"

    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\ScanManager" "DisplayName" "ScanManager Camera Control 0.4.1"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\ScanManager" "UninstallString" "$\"$INSTDIR\uninstall.exe$\""    
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\ScanManager" "QuietUninstallString" "$\"$INSTDIR\uninstall.exe$\" /S"
    
SectionEnd


Section "Uninstall"
  
    Delete "$SMPROGRAMS\ScanManager\ScanManager.lnk"
    Delete "$SMPROGRAMS\ScanManager\Uninstall.lnk"
    RMDir "$SMPROGRAMS\ScanManager"

    ; Remove installed files
    Delete "$INSTDIR\API-MS-Win-Core-LocalRegistry-L1-1-0.dll"
    Delete "$INSTDIR\API-MS-Win-Core-ProcessThreads-L1-1-0.dll"
    Delete "$INSTDIR\API-MS-Win-Security-Base-L1-1-0.dll"
    Delete "$INSTDIR\AVICAP32.dll"
    Delete "$INSTDIR\AVIFIL32.dll"
    Delete "$INSTDIR\MPR.dll"
    Delete "$INSTDIR\MSACM32.dll"
    Delete "$INSTDIR\MSVFW32.dll"
    Delete "$INSTDIR\POWRPROF.dll"
    Delete "$INSTDIR\PySide.QtCore.pyd"
    Delete "$INSTDIR\PySide.QtGui.pyd"
    Delete "$INSTDIR\PySide.QtNetwork.pyd"
    Delete "$INSTDIR\QtCore4.dll"
    Delete "$INSTDIR\QtGui4.dll"
    Delete "$INSTDIR\QtNetwork4.dll"
    Delete "$INSTDIR\_bsddb.pyd"
    Delete "$INSTDIR\_ctypes.pyd"
    Delete "$INSTDIR\_hashlib.pyd"
    Delete "$INSTDIR\_socket.pyd"
    Delete "$INSTDIR\_ssl.pyd"
    Delete "$INSTDIR\_win32sysloader.pyd"
    Delete "$INSTDIR\bz2.pyd"
    Delete "$INSTDIR\cv2.pyd"
    Delete "$INSTDIR\imageformats\qgif4.dll"
    Delete "$INSTDIR\imageformats\qico4.dll"
    Delete "$INSTDIR\imageformats\qjpeg4.dll"
    Delete "$INSTDIR\imageformats\qmng4.dll"
    Delete "$INSTDIR\imageformats\qsvg4.dll"
    Delete "$INSTDIR\imageformats\qtiff4.dll"
    Delete "$INSTDIR\library.zip"
    Delete "$INSTDIR\numpy.core._dotblas.pyd"
    Delete "$INSTDIR\numpy.core._sort.pyd"
    Delete "$INSTDIR\numpy.core.multiarray.pyd"
    Delete "$INSTDIR\numpy.core.scalarmath.pyd"
    Delete "$INSTDIR\numpy.core.umath.pyd"
    Delete "$INSTDIR\numpy.fft.fftpack_lite.pyd"
    Delete "$INSTDIR\numpy.lib._compiled_base.pyd"
    Delete "$INSTDIR\numpy.linalg.lapack_lite.pyd"
    Delete "$INSTDIR\numpy.random.mtrand.pyd"
    Delete "$INSTDIR\pyexpat.pyd"
    Delete "$INSTDIR\pyside-python2.7.dll"
    Delete "$INSTDIR\python27.dll"
    Delete "$INSTDIR\pythoncom27.dll"
    Delete "$INSTDIR\pywintypes27.dll"
    Delete "$INSTDIR\scanmanager.exe"
    Delete "$INSTDIR\select.pyd"
    Delete "$INSTDIR\shiboken-python2.7.dll"
    Delete "$INSTDIR\unicodedata.pyd"
    Delete "$INSTDIR\w9xpopen.exe"
    Delete "$INSTDIR\win32api.pyd"
    Delete "$INSTDIR\win32evtlog.pyd"
    Delete "$INSTDIR\win32pdh.pyd"
    Delete "$INSTDIR\win32pipe.pyd"
    Delete "$INSTDIR\win32trace.pyd"
    Delete "$INSTDIR\win32ui.pyd"
    Delete "$INSTDIR\win32wnet.pyd"
    Delete "$INSTDIR\backend\canonpsrec\PRLIB.dll"
    Delete "$INSTDIR\backend\canonpsrec\PRSDK.dll"
    Delete "$INSTDIR\backend\libgphoto2\__init__.py"
    Delete "$INSTDIR\backend\libgphoto2\api.py"
    Delete "$INSTDIR\backend\libgphoto2\constants.py"
    Delete "$INSTDIR\backend\libgphoto2\ptp.py"
    Delete "$INSTDIR\backend\libgphoto2\remote\__init__.py"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\_bisect.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\_bytesio.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\_codecs_cn.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\_codecs_hk.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\_codecs_iso2022.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\_codecs_jp.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\_codecs_kr.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\_codecs_tw.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\_collections.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\_ctypes.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\_fileio.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\_functools.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\_hashlib.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\_heapq.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\_locale.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\_multibytecodec.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\_random.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\_socket.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\_ssl.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\_struct.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\_weakref.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\array.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\binascii.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\bz2.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\cPickle.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\cStringIO.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\cygbz2-1.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\cygcrypto-0.9.8.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\cygffi-4.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\cyggcc_s-1.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\cygiconv-2.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\cygintl-8.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\cygncursesw-10.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\cygreadline7.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\cygssl-0.9.8.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\cygwin1.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\cygz.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\datetime.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\fcntl.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\gphotoremote.exe"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\gphotoremote.exe.manifest"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\itertools.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\libpython2.6.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\math.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\operator.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\readline.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\select.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\strop.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\termios.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\time.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\unicodedata.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\uri.txt"
    Delete "$INSTDIR\backend\libgphoto2\remote\bin\zlib.dll"
    Delete "$INSTDIR\backend\libgphoto2\remote\client.py"
    Delete "$INSTDIR\backend\libgphoto2\remote\server.py"
    Delete "$INSTDIR\backend\libgphoto2\structures.py"
    Delete "$INSTDIR\backend\libgphoto2\test-api.py"
    Delete "$INSTDIR\backend\libgphoto2\win32\README.txt"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\adc65.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\agfa_cl20.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\aox.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\ax203.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\barbie.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\canon.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\casio_qv.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\clicksmart310.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\digigr8.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\digita.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\dimagev.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\dimera3500.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\directory.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\enigma13.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\fuji.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\gsmart300.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\hp215.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\iclick.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\jamcam.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\jd11.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\jl2005a.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\jl2005c.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\kodak_dc120.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\kodak_dc210.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\kodak_dc240.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\kodak_dc3200.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\kodak_ez200.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\konica.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\konica_qm150.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\largan.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\lg_gsm.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\mars.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\mustek.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\panasonic_coolshot.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\panasonic_dc1000.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\panasonic_dc1580.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\panasonic_l859.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\pccam300.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\pccam600.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\polaroid_pdc320.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\polaroid_pdc640.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\polaroid_pdc700.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\ptp2.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\ricoh.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\ricoh_g3.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\samsung.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\sierra.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\sipix_blink2.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\sipix_web2.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\smal.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\sonix.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\sony_dscf1.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\sony_dscf55.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\soundvision.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\spca50x.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\sq905.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\st2205.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\stv0674.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\stv0680.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\sx330z.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\topfield.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\toshiba_pdrm11.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\camlibs\tp6801.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\cygexif-12.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\cyggcc_s-1.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\cyggphoto2-2.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\cyggphoto2_port-0.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\cygiconv-2.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\cygintl-8.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\cygltdl-7.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\cygpopt-0.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\cygusb0.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\cygwin1.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\gphoto2.bat"
    Delete "$INSTDIR\backend\libgphoto2\win32\gphoto2.exe"
    Delete "$INSTDIR\backend\libgphoto2\win32\iolibs\disk.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\iolibs\ptpip.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\iolibs\serial.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\iolibs\usb.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\iolibs\usb1.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\iolibs\usbdiskdirect.dll"
    Delete "$INSTDIR\backend\libgphoto2\win32\iolibs\usbscsi.dll"
    Delete "$INSTDIR\backend\libgphoto2\wrapper.py"
    Delete "$INSTDIR\backend\nikonsdk\D80_Mod.md3"
    Delete "$INSTDIR\backend\nikonsdk\NkdPTP.dll"
    Delete "$INSTDIR\backend\nikonsdk\NkdPTPDi.dll"

    
    ; Remove settings
    Delete "$INSTDIR\scanmanger.settings.*"
    
    ; Remove uninstaller
    Delete $INSTDIR\uninstall.exe

    ; Remove directories used

    RMDir "$INSTDIR\backend\nikonsdk"
    RMDir "$INSTDIR\backend\libgphoto2\win32\iolibs"
    RMDir "$INSTDIR\backend\libgphoto2\win32\camlibs"
    RMDir "$INSTDIR\backend\libgphoto2\win32"
    RMDir "$INSTDIR\backend\libgphoto2\remote\bin"
    RMDir "$INSTDIR\backend\libgphoto2\remote"
    RMDir "$INSTDIR\backend\libgphoto2"
    RMDir "$INSTDIR\backend\canonpsrec"
    RMDir "$INSTDIR\backend"
    RMDir "$INSTDIR\imageformats"
    RMDir "$INSTDIR"

    ; Remove registry keys
    DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\ScanManager"
    DeleteRegKey HKLM "Software\ScanManager"
    
SectionEnd
