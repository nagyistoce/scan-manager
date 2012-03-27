"""
Scanner main
"""

# System import
import time
import signal
import sys
import os
import optparse
import Image, ImageDraw
import cStringIO
import threading

# Local imports
from base import *
import log as logmodule
from log import DEBUG,INFO,WARNING,ERROR
import config
import base

from etgeneric import ET # generic ElementTree implementation (tries to load the best available implementation)


def log(level,msg,*args,**kargs):
	msg = '%s-thread: %s'%(threading.currentThread().getName(),msg)
	logmodule.log(level,msg,*args,**kargs)
	
def debug(*args,**kargs): log(DEBUG,*args,**kargs)
def info(*args,**kargs): log(INFO,*args,**kargs)
def warning(*args,**kargs): log(WARNING,*args,**kargs)
def error(*args,**kargs): log(ERROR,*args,**kargs)
	

			
COMMAND_LINE_HELP = """Usage: python scanner.py [OPTIONS] [-c FILE]

  -cFILE, --config-file=FILE  use the specified XML config file instead of ./etc/config.xml
  
  Options
  -------
  -q, --quiet                 only log errors to stdout (i.e. not info/debug messages go to 
                              stdout, no matter what the settings are re. logging in the
                              configuration file)
"""

if __name__ == '__main__':

	class MyOptParser(optparse.OptionParser):
		def print_help(self):
			print 'Book Scan System'
			print COMMAND_LINE_HELP
			
	parser = MyOptParser()
	parser.add_option('-c','--config-file',default="etc/config.xml",dest='configFile')
	parser.add_option('-q','--quiet',action='store_true',dest='quiet')
	(options, args) = parser.parse_args()
	
	# Standard initialization
	config.load(options.configFile or 'etc/config.xml')
	
	if options.quiet:
		config.cfg.screenLogLevel = ERROR

	configureLogging()
		

	#
	# main
	#

	from nikon import *
	import threading
	
	import wxw
	import wx
	
	class MainFrame(wxw.Frame):
		
		size = (1160,800)
		title = 'Book Scanner'

		class Sizer(wxw.BoxSizer):
			orient = wx.VERTICAL
	
		def OnKeyDown(self,event):
			if event.GetKeyCode() == 13:
				self.click()
			
		def init(self):
			self.pageCount = 1
			self.Centre()
			self.Show(True)
			self.setup()
			self.j = Joystick(self)
			self.j.SetCapture(self)
			print 'done init'
			#self.preview(r'page0272.jpg')


		class Panel(wxw.Panel):
			sizerProportion = 1
			sizerFlag = wx.ALL|wx.EXPAND

			class Image(wxw.StaticBitmap):
				size = (1100,800)


		def OnJoyButtonDown(self,event):
			self.click()
			

		def setup(self):
			
			global camera
			
			self.module = Object()
	
			childIds = self.module.caps.children.items
			if not childIds:
				print 'No camera connected'
				#sys.exit(2)
			else:
				self.camera = Object(parent=self.module,childId=childIds[0])
				#camera = self.camera 
				#self.camera.caps.AutoFocus()
				#self.camera.idleLoop()
				#self.camera.caps.lockcameraoperation = 1
			
		
		def preview(self,fileName):

			i = Image.open(fileName)
			cSize = self.Image.GetClientSize()
			iSize = i.size
			iRatio = float(iSize[1])/float(iSize[0])
			newSize = cSize[0],int(cSize[0]*iRatio)
			if newSize[1] > cSize[1]:
				newSize = (cSize[1]/iRatio,cSize[1])
			iPreview = i.resize(newSize,1)
			iPreview = iPreview.rotate(180)
			draw = ImageDraw.Draw(iPreview)
			draw.line((iPreview.size[0]/2,0,iPreview.size[0]/2,iPreview.size[1]), fill=0x00FF00)
			imageData = iPreview.tostring('jpeg','RGB')
			imageStream = cStringIO.StringIO(imageData)
			jpg = wx.BitmapFromImage( wx.ImageFromStream( imageStream ) )
			self.Image.Refresh()
			self.Image.SetSize(iPreview.size)
			self.Image.SetBitmap(jpg)
			#i.save(fileName[:-3] + 'png')
			
	
		def click(self):

			self.camera.caps.Capture()
			self.camera.idleLoop()
			
			for i in range(100):
				if self.camera.caps.children.items:
					break
				self.module.idleLoop()
				time.sleep(0.01)
			else:
				raise Exception('No image captured')
		
			childIds = self.camera.caps.children.items
			frame = Object(parent=self.camera,childId=childIds[0])
			
			childBitmask = self.camera.caps.dataTypes.value
			if not childBitmask | DataObjType.Image:
				print 'No image data'
				sys.exit(1)
			
			image = Object(parent=frame,childId=1)

			app = self
			class DH(DataHandler):
				
				def completed(self):

					self.previewThread = threading.Thread(target=app.preview,args=(self.fileName,))
					self.previewThread.start()
					return
					
			image.setProc(image.caps['dataProc'],DataProc(DH('page%04d'%self.pageCount)))
			self.pageCount += 1

			image.idleLoop()
			tStart = time.time()
			image.caps.acquire()
			print '-> Acquired in %.2f'%(time.time()-tStart)
			image.idleLoop()
			image.close()
			frame.idleLoop()
			frame.close()
			self.camera.idleLoop()
			self.module.idleLoop()
		
		def repr(self):
			print module
			print camera
			print camera.caps.__reprlong__()
			print repr(camera.caps.sharpness)
			
			
			

	class Joystick(wxw.ComponentBase,wx.Joystick):
		
		_initArgs = set()
		_wxBaseExpectsParent = False
		_wxBaseClass = wx.Joystick
		_bindToParent = False
		
		
	app = wxw.App(redirect=False)
	m = MainFrame(None)
	app.MainLoop()
	
	
