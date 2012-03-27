"""
Scanner main
"""

# System import
import time
import signal
import sys
import os
import optparse
import cStringIO
import threading
import traceback

import canon
from canon.properties import properties
import threading

import wxw
import wx
import colorsys
from math import cos, sin, radians
	

USE_BUFFERED_DC = True

class BufferedWindow(wxw.Panel):

	"""
	A Buffered window class.

	Not currently used (we roll our own) but should replace custom code below with this one
	"""
	def __init__(self, *args, **kwargs):
		# make sure the NO_FULL_REPAINT_ON_RESIZE style flag is set.
		kwargs['style'] = kwargs.setdefault('style', wx.NO_FULL_REPAINT_ON_RESIZE) | wx.NO_FULL_REPAINT_ON_RESIZE
		wxw.Panel.__init__(self, *args, **kwargs)

		#wx.EVT_PAINT(self, self.OnPaint)
		#wx.EVT_SIZE(self, self.OnSize)

		# OnSize called to make sure the buffer is initialized.
		# This might result in OnSize getting called twice on some
		# platforms at initialization, but little harm done.
		self.OnSize(None)
		self.paint_count = 0

	def Draw(self, dc):
		## just here as a place holder.
		## This method should be over-ridden when subclassed
		pass

	def OnPaint(self, event):
		# All that is needed here is to draw the buffer to screen
		if USE_BUFFERED_DC:
			dc = wx.BufferedPaintDC(self, self._Buffer)
		else:
			dc = wx.PaintDC(self)
			dc.DrawBitmap(self._Buffer, 0, 0)

	def OnSize(self,event):
		# The Buffer init is done here, to make sure the buffer is always
		# the same size as the Window
		#Size  = self.GetClientSizeTuple()
		Size  = self.ClientSize

		# Make new offscreen bitmap: this bitmap will always have the
		# current drawing in it, so it can be used to save the image to
		# a file, or whatever.
		self._Buffer = wx.EmptyBitmap(*Size)
		self.UpdateDrawing()

	def SaveToFile(self, FileName, FileType=wx.BITMAP_TYPE_PNG):
		## This will save the contents of the buffer
		## to the specified file. See the wxWindows docs for 
		## wx.Bitmap::SaveFile for the details
		self._Buffer.SaveFile(FileName, FileType)

	def UpdateDrawing(self):
		"""
		This would get called if the drawing needed to change, for whatever reason.

		The idea here is that the drawing is based on some data generated
		elsewhere in the system. If that data changes, the drawing needs to
		be updated.

		This code re-draws the buffer, then calls Update, which forces a paint event.
		"""
		dc = wx.MemoryDC()
		dc.SelectObject(self._Buffer)
		self.Draw(dc)
		del dc # need to get rid of the MemoryDC before Update() is called.
		self.Refresh(eraseBackground=False)
		self.Update()


class ImagePanel(wxw.Panel):
	
	def writeImage(self,data):
		self.imageData = data
		self.redraw()

	
	def OnSize(self, evt):
		self.InitBuffer()
		self.Refresh()
		self.Update()
		evt.Skip()
		

	def OnPaint(self, evt):
		dc = wx.BufferedPaintDC(self, self._buffer)

		
	def redraw(self):
		dc = wx.MemoryDC(self._buffer)
		dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
		dc.Clear()
		gc = wx.GraphicsContext.Create(dc)
		self.Draw(gc)
		del dc # need to get rid of the MemoryDC before Update() is called.
		self.Refresh(eraseBackground=False)
		self.Update()


	def InitBuffer(self):
		sz = self.GetClientSize()
		sz.width = max(1, sz.width)
		sz.height = max(1, sz.height)
		self._buffer = wx.EmptyBitmap(sz.width, sz.height, 32)

		dc = wx.MemoryDC(self._buffer)
		dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
		dc.Clear()
		gc = wx.GraphicsContext.Create(dc)
		self.Draw(gc)
		

	def Draw(self, gc):
		
		if not getattr(self,'imageData',None):
			return
		
		gc.PushState()			 # save current translation/scale/other state
		
		f = cStringIO.StringIO(self.imageData)
		image = wx.ImageFromStream(f)
		bmp = wx.BitmapFromImage(image)
		self.image = image
		self.bmp = bmp
		
		# Size the bitmap to best fill the window while keeping the aspect ratio the same
		sz = self.GetClientSize()
		bsz = bmp.GetSize()
		ratio = float(bsz.width)/float(bsz.height)
		w = bsz.width
		h = bsz.height
		if w > sz.width:
			w = sz.width
			h = w / ratio
		if h > sz.height: 
			h = sz.height
			w = h * ratio
		gc.DrawBitmap(bmp,w,h,-w,-h)

		# Centre line
		gc.SetPen( wx.RED_PEN )
		p = gc.CreatePath()
		p.MoveToPoint(w/2,0)
		p.AddLineToPoint(w/2,h)
		gc.StrokePath(p)

		# Borders
		gc.SetPen( wx.GREEN_PEN )
		lBorder = self.frame.LBorder.GetValue()
		mlBorder = int((float(lBorder) / 3648.0) * w)
		if lBorder:
			p = gc.CreatePath()
			p.MoveToPoint(mlBorder,0)
			p.AddLineToPoint(mlBorder,h)
			gc.StrokePath(p)
		rBorder = self.frame.RBorder.GetValue()
		mrBorder = int((float(rBorder) / 3648.0) * w)
		if rBorder:
			p = gc.CreatePath()
			p.MoveToPoint(w-mrBorder,0)
			p.AddLineToPoint(w-mrBorder,h)
			gc.StrokePath(p)
		
		gc.PopState()
		
		

class CameraPropertyBase(object):
	"""
	Base for an on-screen field that is tied to a camera property
	"""
	cameraProperty = None

	@property
	def descriptor(self):
		if self.cameraProperty in canon.properties:
			return canon.properties[self.cameraProperty]
		else:
			return None
	
	@property
	def prop(self):
		return self.frame.camera.properties[self.cameraProperty]
	
	def _set_value(self,v):
		self.frame.camera[self.cameraProperty] = v
	def _get_value(self):
		return self.frame.camera[self.cameraProperty]
	cameraValue = property(_get_value,_set_value)
	
	def _set_valueString(self,v):
		if self.descriptor:
			self.cameraValue = self.descriptor[v]
		else:
			self.cameraValue = int(v)
	def _get_valueString(self):
		if self.descriptor:
			return self.descriptor[self.cameraValue]
		else:
			return unicode(self.cameraValue)
	cameraValueString = property(_get_valueString,_set_valueString)


class CameraPropertySlider(CameraPropertyBase,wxw.Slider):
	"""
	An on-screen slider control that is tied to a camera property
	"""
	size = (200,20)
	style = wx.SL_HORIZONTAL | wx.SL_AUTOTICKS
	firstTime = True
	
	def OnScrollChanged(self,event):
		self.cameraValue = self.GetValue()
		self.frame.updateCameraControls()

	def setValueFromCamera(self):
		if self.firstTime:
			self.SetRange(
				self.prop.min,
				self.prop.max
			)
			self.firstTime = False
		self.SetValue(self.cameraValue)

						
class CameraPropertyCombo(CameraPropertyBase,wxw.ComboBox):
	"""
	An on-screen combo control that is tied to a camera property
	"""
	style = wx.CB_DROPDOWN|wx.CB_READONLY
	firstTime = True
	updatePropertyBeforeSetting = False
	
	def setValueFromCamera(self):
		if self.firstTime:
			self.Clear()
			if getattr(self.prop,'values',None):
				for v in self.prop.values:
					self.Append(self.descriptor[v])
			else:
				for k,v in self.descriptor:
					self.Append(k)
			self.firstTime = False
		self.SetValue(self.cameraValueString)

	def OnCombobox(self,event):
		if self.updatePropertyBeforeSetting:
			self.frame.camera.updateSingleProperty(self.cameraProperty)
			#self.firstTime = True
		self.cameraValueString = self.GetValue()
		self.frame.updateCameraControls()
		
		

class CameraPropertyStatic(CameraPropertyBase,wxw.TextCtrl):
	"""
	An on-screen read-only text control that is tied to a camera property
	"""
	cameraProperty = None
	
	def init(self):
		self.SetEditable(False)
	
	def setValueFromCamera(self):
		self.SetValue(self.cameraValueString)
		
		

class MainFrame(wxw.Frame):
	
	size = (1160,800)
	title = 'Book Scanner'
	style = wx.DEFAULT_FRAME_STYLE|wx.WANTS_CHARS

	class Sizer(wxw.BoxSizer):
		orient = wx.HORIZONTAL


	def init(self):
		self.SetAcceleratorTable(
			wx.AcceleratorTable([
				(wx.ACCEL_NORMAL, 13, 2201),
				(wx.ACCEL_NORMAL, ord('='), 2202),	# doesn't work
				(wx.ACCEL_NORMAL, ord('-'), 2203),	# doesn't work
			])
		)

		self.pageCount = 100
		self.Centre()
		self.Show(True)
		self.setup()

		#self.j = Joystick(self)
		#self.j.SetCapture(self)


	def OnMenu2201(self,event):
		self.click()


	def OnMenu2202(self,event):
		"""
		This shortcut key doesn't work for some reason
		"""
		zp = self.camera['ZOOM_POS']
		if zp < 9:
			self.camera['ZOOM_POS'] = zp + 1

	def OnMenu2202(self,event):
		"""
		This shortcut key doesn't work for some reason
		"""
		zp = self.camera['ZOOM_POS']
		if zp > 0:
			self.camera['ZOOM_POS'] = zp - 1
		
		
	
	class MainSplitter(wxw.SplitterWindow):
		sizerFlag = wx.EXPAND|wx.ALL|wx.ALIGN_CENTER
		sizerProportion = 1

		def init(self):
			self.SplitVertically(self.Viewfinder,self.RightPanel,324)
	

		class Viewfinder(ImagePanel):
			style = wx.BORDER_SUNKEN
			pass
	
		
		class RightPanel(wxw.SplitterWindow):
					
			sizerFlag = wx.EXPAND|wx.ALL|wx.ALIGN_CENTER
			sizerProportion = 1
	
			def init(self):
				self.SplitHorizontally(self.Preview,self.CameraControls,-190)


			class Preview(ImagePanel):
				style = wx.BORDER_SUNKEN
		
		
			class CameraControls(wxw.Panel):
				style = wx.BORDER_SUNKEN
				sizerBorder = 10
				sizerPadding = 10
				
				class Sizer(wxw.GridBagSizer):
					hgap = 3
					vgap = 3
					def init(self):
						self.AddGrowableCol(1)
						self.AddGrowableCol(3)
						wxw.GridBagSizer.init(self)


				class ZoomLabel(wxw.StaticText):
					label = 'Zoom:'
					sizerPos = (0,0)
					
				class Zoom(CameraPropertySlider):
					sizerPos = (0,1)
					cameraProperty = 'ZOOM_POS'

				class ISOComboLabel(wxw.StaticText):
					label = 'ISO:'
					sizerPos = (1,0)
					sizerFlag = wx.ALIGN_CENTER_VERTICAL

				class ISO(CameraPropertyCombo):
					sizerPos = (1,1)
					cameraProperty = 'ISO'

				class ExposureModeLabel(wxw.StaticText):
					label = 'Exposure mode:'
					sizerPos = (2,0)
					sizerFlag = wx.ALIGN_CENTER_VERTICAL

				class ExposureMode(CameraPropertyCombo):
					sizerPos = (2,1)
					cameraProperty = 'EXPOSURE_MODE'

				class AVLabel(wxw.StaticText):
					label = 'Aperture:'
					sizerPos = (3,0)
					sizerFlag = wx.ALIGN_CENTER_VERTICAL

				class AV(CameraPropertyCombo):
					sizerPos = (3,1)
					cameraProperty = 'AV'
					updatePropertyBeforeSetting = True

					def setValueFromCamera(self):
						if self.firstTime:
							self.Clear()
							vmax = self.frame.camera['AV_MAX_APEX']
							vmin = self.frame.camera['AV_OPEN_APEX']
							oneThirdLevels = self.frame.camera['DISP_AV'] == 0
							for k,v in self.descriptor:
								#if v < vmin or v > vmax: continue
								self.Append(k)
							self.firstTime = False
						self.SetValue(self.cameraValueString)


					
				class TVLabel(wxw.StaticText):
					label = 'Shutter speed:'
					sizerPos = (4,0)
					sizerFlag = wx.ALIGN_CENTER_VERTICAL

				class TV(CameraPropertyCombo):
					sizerPos = (4,1)
					cameraProperty = 'TV'
					updatePropertyBeforeSetting = True
					
					def setValueFromCamera(self):
						if self.firstTime:
							self.Clear()
							for k,v in self.descriptor:
								self.Append(k)
							self.firstTime = False
						self.SetValue(self.cameraValueString)


					
				class FocusPointLabel(wxw.StaticText):
					label = 'Focus point:'
					sizerPos = (0,2)
					sizerFlag = wx.ALIGN_CENTER_VERTICAL

				class FocusPoint(CameraPropertyCombo):
					sizerPos = (0,3)
					cameraProperty = 'FOCUS_POINT_SETTING'
					
				class WhiteBalanceLabel(wxw.StaticText):
					label = 'White balance:'
					sizerPos = (1,2)
					sizerFlag = wx.ALIGN_CENTER_VERTICAL

				class WhiteBalance(CameraPropertyCombo):
					sizerPos = (1,3)
					cameraProperty = 'WB_SETTING'

				class CameraOutputLabel(wxw.StaticText):
					label = 'Camera output:'
					sizerPos = (2,2)
					sizerFlag = wx.ALIGN_CENTER_VERTICAL

				class CameraOutput(CameraPropertyCombo):
					sizerPos = (2,3)
					cameraProperty = 'CAMERA_OUTPUT'

				class CameraModelLabel(wxw.StaticText):
					label = 'Camera model:'
					sizerPos = (3,2)
					sizerFlag = wx.ALIGN_CENTER_VERTICAL

				class CameraModel(CameraPropertyStatic):
					sizerPos = (3,3)
					size = (200,-1)
					sizerFlags = wx.EXPAND
					cameraProperty = 'CAMERA_MODEL_NAME'


				class CaptureButton(wxw.Button):
					label = 'Capture'
					sizerPos = (6,2)
					sizerFlag = wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND
					sizerSpan = (1,2)
					
					def OnButton(self,event):
						self.frame.click()


				class SetButton(wxw.Button):
					label = 'Set AWB/AE/AF'
					sizerPos = (4,2)
					sizerFlag = wx.ALIGN_LEFT
					
					def OnButton(self,event):
						self.frame.camera.reset_AE_AF_AWB(AE=False,AF=False,AWB=False)
						
				class ResetButton(wxw.Button):
					label = 'Reset AWB/AE/AF'
					sizerPos = (4,3)
					sizerFlag = wx.ALIGN_LEFT
					
					def OnButton(self,event):
						self.frame.camera.reset_AE_AF_AWB(AE=True,AF=True,AWB=True)


				class LBorderLabel(wxw.StaticText):
					label = 'Left crop border:'
					sizerPos = (5,0)
					sizerFlag = wx.ALIGN_CENTER_VERTICAL

				class LBorder(wxw.SpinCtrl):
					sizerPos = (5,1)
					sizerFlag = wx.ALIGN_CENTER_VERTICAL
					min = 0
					max = 2000
					initial = 0
						
				class RBorderLabel(wxw.StaticText):
					label = 'Right crop border:'
					sizerPos = (6,0)
					sizerFlag = wx.ALIGN_CENTER_VERTICAL

				class RBorder(wxw.SpinCtrl):
					sizerPos = (6,1)
					sizerFlag = wx.ALIGN_CENTER_VERTICAL
					min = 0
					max = 2000
					initial = 0
						

				class FocusLockButton(wxw.Button):
					label = 'Lock Focus'
					sizerPos = (5,2)
					sizerFlag = wx.ALIGN_LEFT
					#sizerSpan = (1,2)
					
					def OnButton(self,event):
						self.frame.camera.lockFocus()

				class FocusUnockButton(wxw.Button):
					label = 'Unlock Focus'
					sizerPos = (5,3)
					sizerFlag = wx.ALIGN_LEFT
					#sizerSpan = (1,2)
					
					def OnButton(self,event):
						self.frame.camera.unlockFocus()
						
				

	def setup(self):
		if not sdk.cameras:
			mb = wx.MessageDialog(None, 'No camera found', 'Error', wx.OK|wx.ICON_EXCLAMATION)
			mb.ShowModal()
			self.Close()
			return
			
			
		self.camera = sdk.cameras[0]
		self.camera.startRemote()
		
		self.updateCameraControls()

		self.camera.startViewfinder(self.onViewfinder)


	def updateCameraControls(self):
		for i in [c for c in self.CameraControls.children if hasattr(c,'cameraProperty')]:
			i.setValueFromCamera()
			
			
	def onViewfinder(self,vfData):
		self.Viewfinder.writeImage(vfData)


	def click(self):

		self.camera.release(keepImageBuffer=True,imageCompleteCallback=self.onCaptureComplete)
		

	def onCaptureComplete(self,releaseInfo):
		self.Preview.writeImage(releaseInfo.imageBuffer)
		fileName = 'captured/page%04d.jpg'%self.pageCount
		image = self.Preview.image
		lBorder = self.LBorder.GetValue()
		rBorder = self.RBorder.GetValue()
		if lBorder or rBorder:
			h = image.GetHeight()
			w = image.GetWidth()
			image = image.GetSubImage((lBorder,0,(w-(rBorder+lBorder)),h))
		image.SaveFile(fileName,wx.BITMAP_TYPE_JPEG)
		self.pageCount += 1


	#def OnJoyButtonDown(self,event):
	#	self.click()
	
	def OnClose(self,event):
		if sdk.cameras:
			sdk.cameras[0].applicationVFCallback = lambda e: None
		self.Destroy()


class Joystick(wxw.ComponentBase,wx.Joystick):
	""" Used if we want to support a DIY pedal based on a USB joystick board """
	
	_initArgs = set()
	_wxBaseExpectsParent = False
	_wxBaseClass = wx.Joystick
	_bindToParent = False



if __name__ == '__main__':
	sdk = canon.SDK()
	app = wxw.App(False)
	m = MainFrame(None)
	app.MainLoop()
	sdk.close()

