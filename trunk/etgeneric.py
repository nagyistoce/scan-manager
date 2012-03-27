"""
Tries to import the best available ElementTree implementation as ET

Use e.g. as follows::

	from etgeneric import ET
	
"""

try:
	# for python 2.5
	from xml.etree import cElementTree as ET
except ImportError:
	try:
		# for python 2.5
		from xml.etree import ElementTree as ET
	except ImportError:
		try:
			# use etree from lxml if it is installed
			from lxml import etree as ET
		except ImportError:
			try:
				# use cElementTree if available
				import cElementTree as ET
			except ImportError:
				try:
					from elementtree import ElementTree as ET
				except ImportError:
					raise ImportError("No suitable ElementTree implementation was found.")

