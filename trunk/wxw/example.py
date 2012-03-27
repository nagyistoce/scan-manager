import wxwrap as wxw
import wx


class MainFrame(wxw.Frame):
	
	size = (400,600)
	title = 'test frame'

	def init(self):
		self.Centre()
		self.Show(True)
		
	class Sizer(wxw.BoxSizer):
		orient = wx.VERTICAL

	class MainPanel(wxw.Panel):
		sizerProportion = 1
		sizerFlag = wx.EXPAND
		
		class Sizer(wxw.BoxSizer):
			orient = wx.VERTICAL
		
		class MyText1(wxw.StaticText):
			sizerProportion = 1
			label = 'hello'
			
			def OnLeftDown(self,e):
				print 'ld1'

		class MyText2(wxw.StaticText):
			sizerProportion = 0
			label = 'goodbye'

		def OnLeftDown(self,e):
			print 'ld2'
	
app = wxw.App(redirect=False)
m = MainFrame(None)
app.MainLoop()

