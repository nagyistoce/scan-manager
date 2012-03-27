"""
Declarative (nested-class style) wrapper for wxPython classes

Allows creating wxPython applications using a more declarative syntax based on nested classes and introspection. Allows
code such as::

	class MainFrame(Frame):
		
		size = (400,600)
		title = 'test frame'

		def init(self):
			self.Centre()
			self.Show(True)
			
		class MainPanel(Panel):

			class MyText1(StaticText):
				label = 'hello'
				
				def OnLeftDown(self,e):
					print 'ld1'

"""

import wx
import wx.html
import  wx.lib.scrolledpanel

import types
import re

_allIds = dir(wx)

def _wxSubclasses(klass):
	return set([i for i in _allIds if type(getattr(wx,i)) is type and issubclass(getattr(wx,i),klass)])

def _wxInstances(klass):
	return set([i for i in _allIds if isinstance(getattr(wx,i),klass)])

_unsizedIds = set(['MenuBar','StatusBar','Menu'])
_bindToParentIds = _unsizedIds
_eventIds = _wxInstances(wx._core.PyEventBinder)
_controlIds = _wxSubclasses(wx._core.Control)
_topLevelIds = _wxSubclasses(wx._windows.Dialog).union(_wxSubclasses(wx._windows.Frame))
_windowIds = _wxSubclasses(wx._core.Window) - _controlIds.union(_topLevelIds)
_sizerIds = _wxSubclasses(wx._core.Sizer)

__all__ = ['OrderableMetaclass','ComponentBase','App','TopLevelBase','WindowBase','ControlBase','SizerBase','Spacer']

class DuplicateUIDError(Exception):
	pass


class OrderableMetaclass(type):
	"""
	This makes it easier to work with nested classes by giving each nested class an C{_order} attribute automatically
	representing the order in which the class was declared
	"""
	
	orderCounter = 1
	
	def __new__(meta,classname,bases,classDict):
		# Add an order attribute
		classDict['_order'] = meta.orderCounter
		meta.orderCounter += 1
		
		# Create the class
		klass = type.__new__(meta,classname,bases,classDict)
		
		return klass


class ComponentBase(object):
	"""
	Base for all wx components including panels, fields, etc.

	Knows how to allocate a uid to instances automatically (if none is present) and store it in the C{uid} attribute of the instance.
	"""
	
	__metaclass__ = OrderableMetaclass
	
	_autoInstantiable = True
	
	_useAutoInstantiate = True
	
	_collapseNamespace = True
	
	_wxBaseExpectsParent = True
	
	_bindToParent = False


	def __init__(self,parent,**kargs):
		self.children = []
		self.ancestors = []
		self.instantiated = [] # all instantiated items, incl. those with _nonChild set (so as to keep a ref to them, lest they get deleted)
		self.parent = parent
		if getattr(self,'uid',None) is None:
			self.uid = self.__class__.__name__
			
		# Check for args supplied to the constructor and not valid for underlying wx type:
		extraArgs = set(kargs.keys()) - self._initArgs
		if extraArgs:
			raise TypeError('%s are not valid constructor arguments'%extraArgs)
		
		# Check for class attributes that should be supplied to the constructor:
		for k in set(dir(self)).intersection(self._initArgs):
			if k in ('parent','self'):
				continue
			kargs[k] = getattr(self,k)
		
		if self._wxBaseClass:
			if self._wxBaseExpectsParent:
				self._wxBaseClass.__init__(self,parent,**kargs)
			else:
				self._wxBaseClass.__init__(self,**kargs)

		if self._useAutoInstantiate:
			self.autoInstantiate()
			
		self.attach()
		

	@property
	def frame(self):
		if isinstance(self,wx.Frame) or isinstance(self,wx.Dialog):
			return self
		elif self.parent:
			return self.parent.frame
		else:
			return None


	def init(self):
		pass


	def attach(self):
		global x,y
		
		ids = set(dir(self)) #- set(dir(self._wxBaseClass))
		
		# We'll want to check for the longer event names first 
		l = [i for i in _eventIds]
		l.sort(lambda a,b:cmp(len(b),len(a)))
		
		for eventId in l:
			baseName = 'On' + ''.join([i.capitalize() for i in eventId.split('_')[1:]])
			for id in ids:
				if id.startswith(baseName):
					if getattr(self._wxBaseClass,id,None) and (getattr(self,id).im_func is getattr(self._wxBaseClass,id).im_func):
						continue
					break
			else:
				continue
			
			event = getattr(wx,eventId)
			function = getattr(self,id)

			bindSource = None

			bindTarget = self
			while bindTarget._bindToParent:
				bindTarget = bindTarget.parent
			
			args = (event,function,bindSource)
			
			tail = id[len(baseName):]
			if tail:
				bindIds = []
				bindIdsS = tail.split('_')
				for bindId in bindIdsS:
					if bindId.isdigit():
						bindIds.append(int(bindId))
					else:
						bindIds.append(getattr(wx,bindId))
				
				args += tuple(bindIds)
			
			#print '%r -> Bind %r %r'%(bindTarget,eventId,args[1:])
			bindTarget.Bind(*args)
			
			ids.remove(id)


	def addChild(self,c):
		self.children.append(c)
		self.addAncestor(c)
	
	
	def addAncestor(self,c):
		self.ancestors.append(c)
		if self.parent is not None:
			self.parent.addAncestor(c)
		if self._collapseNamespace:
			if not hasattr(self,c.uid):
				setattr(self,c.uid,c)


	def autoInstantiate(self,parent=None):
		"""
			Instantiate any wx classes that are attributes of this class
			
			N.B. all components, not just containers, need to have an auto-instantiate step to support clases as attributes
			
			Looks for any attributes of this B{class} which are sub-classes of C{ComponentBase} classes,
			when one is found it is instantiated and the attribute of the B{instance} is replaced
			with the instantiated C{ComponentBase} sub-class.
			
			Used when you have something like::
			
				class MyScreen(Screen):
					...
					class MyField(Input):
						...
				win = MyScreen(...)
			
			C{win.autoInstantiate()} will replace C{win.MyField} with an instance of C{win.MyField}. Classes are passed 
			the parent class as the only parameter when instantiated, equivalent to::

				win.MyField = win.MyField(parent=win)
			
			If C{screen._useAutoInstantiate} is C{True} this method will be called automatically during C{__init__}
			
			This method will also call C{self.addChild} or any instance it creates <b>unless</b> that instances
			has an '_nonChild' attribute (used by L{ComponentList}).

		"""
		if parent is None:
			parent = self
		if getattr(self,'aiDone',False):
			raise Exception('re-auto-instantiating %r'%self)
		self.aiDone = True
		todo = []
		
		# Find all matching classes
		for k in dir(self.__class__):
			if k.startswith('_'):
				continue
			v = getattr(self.__class__,k)
			if getattr(v,'_autoInstantiable',False):
				todo.append((k,v))
				
		# Sort by declartion order
		todo.sort(lambda a,b: cmp(a[1]._order,b[1]._order))
				
		# Instantiate
		for k,v in todo:
			o = v(parent=parent)
			setattr(self,k,o)
			if not hasattr(o,'_nonChild'):
				self.addChild(o)
			self.instantiated.append(o)


	def __repr__(self):
		if self.__class__.__name__ == self.uid:
			return '<%s %s>'%(','.join([i.__name__ for i in self.__class__.__bases__]),self.uid)
		else:
			return '<%s %s>'%(self.__class__.__name__,self.uid)



_initPat = re.compile(r'__init__\((.*?)\)',re.DOTALL)
def _calcInitArgs(klass):
	s = klass.__init__.im_func.func_doc
	if not s:
		return set(['parent','id'])
	m = _initPat.search(s)
	if not m:
		return set(['parent','id'])
	args = m.group(1)
	argL = args.split(',')
	out = []
	for arg in argL:
		parts = arg.strip().split()
		if len(parts) > 1:
			argName = parts[1]
		else:
			argName = parts[0]
		if '=' in argName:
			default = argName.split('=')[1]
			argName = argName.split('=')[0]
			out.append((argName,default))
		else:
			out.append((argName,None))
		
	return set([i[0] for i in out])
	
	

#
# Set up top-level classes
#

class App(wx.App):
	pass

class TopLevelBase(ComponentBase):
	
	def __init__(self,parent):
		
		ComponentBase.__init__(self,parent)
		
		l = self.ancestors[:]
		for i in l:
			i.init()
		self.init()

for id in _topLevelIds:
	wxClass = getattr(wx,id)
	initArgs = _calcInitArgs(wxClass)
	cd = {}
	cd['_initArgs'] = initArgs
	cd['_wxBaseClass'] = wxClass
	wxwClass = type(id,(TopLevelBase,wxClass),cd)
	globals()[id] = wxwClass
	__all__.append(id)


#
# Set up controls
#

class ControlBase(ComponentBase):
	pass
			

for id in _controlIds:
	wxClass = getattr(wx,id)
	initArgs = _calcInitArgs(wxClass)
	cd = {}
	cd['_initArgs'] = initArgs
	cd['_wxBaseClass'] = wxClass
	wxwClass = type(id,(ControlBase,wxClass),cd)
	globals()[id] = wxwClass
	__all__.append(id)
	
	
#
# Set up window classes
#

class WindowBase(ComponentBase):
	pass
		

for id in _windowIds:
	wxClass = getattr(wx,id)
	initArgs = _calcInitArgs(wxClass)
	cd = {}
	cd['_initArgs'] = initArgs
	cd['_wxBaseClass'] = wxClass
	if id in set(['MenuBar']):
		cd['_wxBaseExpectsParent'] = False
	if id in _bindToParentIds:
		cd['_bindToParent'] = True
	wxwClass = type(id,(WindowBase,wxClass),cd)
	globals()[id] = wxwClass
	__all__.append(id)
	

#
# Set up sizer classes
#

class SizerBase(ComponentBase):

	_wxBaseExpectsParent = False

	def __init__(self,parent=None):
		# This hack stops parent being passed to the wx class
		super(SizerBase,self).__init__(parent=parent)
		
	
	def init(self):
		if self.children:
			children = self.children
		else:
			children = [i for i in self.parent.children if i is not self]
		
		for child in children:
			if set(child.__class__.__bases__).intersection(_unsizedIds):
				continue
			kargs = {}
			for attribute,karg in [('sizerFlag','flag'),('sizerBorder','border'),('sizerProportion','proportion'),('sizerUserData','userData'),('sizerPos','pos'),('sizerSpan','span'),('sizerWidth','width'),('sizerHeight','height')]:
				if hasattr(child,attribute):
					kargs[karg] = getattr(child,attribute)
			if isinstance(child,Spacer):
				self.Add((child.width,child.height),**kargs)
			else:
				self.Add(child,**kargs)
		
		if isinstance(self.parent,Sizer):
			pass
		else:
			self.parent.SetSizer(self)
			self.parent.SetAutoLayout(True)
		

	def autoInstantiate(self,parent=None):
		if parent is None:
			ComponentBase.autoInstantiate(self,self.parent)
		else:
			ComponentBase.autoInstantiate(self,parent)

	def addChild(self,c):
		self.children.append(c)
		self.parent.addChild(c)
		self.addAncestor(c)
	


class Spacer(object):
	__metaclass__ = OrderableMetaclass
	_wxBaseClass = None
	_autoInstantiable = True
	_useAutoInstantiate = False
	width = 0
	height = 0
	
	def __init__(self,parent):
		self.parent = parent
		if getattr(self,'uid',None) is None:
			self.uid = self.__class__.__name__
		
	def init(self):
		pass
	

for id in _sizerIds:
	wxClass = getattr(wx,id)
	initArgs = _calcInitArgs(wxClass)
	cd = {}
	cd['_initArgs'] = initArgs
	cd['_wxBaseClass'] = wxClass
	wxwClass = type(id,(SizerBase,wxClass),cd)
	globals()[id] = wxwClass
	__all__.append(id)



class HtmlWindow(ControlBase,wx.html.HtmlWindow):
	
	_initArgs = _calcInitArgs(wx.html.HtmlWindow)
	_wxBaseClass = wx.html.HtmlWindow

__all__.append('HtmlWindow')


class ScrolledPanel(ControlBase,wx.lib.scrolledpanel.ScrolledPanel):

	_initArgs = set(['parent','id','pos','size','style','name'])
	_wxBaseClass = wx.lib.scrolledpanel.ScrolledPanel

__all__.append('ScrolledPanel')

class Menu(ControlBase,wx.Menu):
	
	_initArgs = _calcInitArgs(wx.Menu)
	_wxBaseClass = wx.Menu
	_wxBaseExpectsParent = False
	_bindToParent = True

__all__.append('Menu')

