"""
py2exe and distutils setup script for the client
"""

from distutils.core import setup
import py2exe

setup(
	name='dropbox',
	windows=[{
		'script': 'wxwclient.py',
		'icon_resources': [(0x0004, '../assets/dropbox.ico')],
	}],
	data_files=[
		('./etc',['../etc/config.xml','../etc/config-local.xml']),
		('./assets',['../assets/dropbox128.png','../assets/dropbox.ico']),
	],
)
