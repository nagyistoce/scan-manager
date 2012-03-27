"""
Defines the structure of the configuration XML file using our xmlconfig library
"""

from xmlconfig import *


class Configuration(object):
	"""
	Simple container to hold the top-level configuration
	"""
	def __init__(self,**kargs):
		"""
		This constructor just converts keyword arguments to instance attributes so that you can do e.g.::
		
			>>> Configuration(a=1,b=2)
			>>> Configuration.b
			2
			>>>

		"""
		self.__dict__.update(kargs)


"""
STANDARD_FORM = Instance(id='form',help='Generic form type',klass=fields.Form,properties=[
	Scalar(id='hgap',dataType='int',optional=False,default=4,help='Horizontal gap between fields'),
	Scalar(id='vgap',dataType='int',optional=False,default=4,help='Vertical gap between fields'),
	Scalar(id='cols',dataType='int',optional=False,default=1,help='Number of field columns'),
	Array(id='fieldSpecs',tag='fields',optional=False,help='Specifications for handling different file packages for upload',subSchemas=[
		Instance(id='input',klass=fields.Input,help='Input field',properties=[
			Scalar(id='id',dataType='str',optional=False,help='Identifier for the field'),
			Scalar(id='label',dataType='str',help='The label for the field'),
			Scalar(id='dataType',dataType='str',optional=False,default='unicode',help='Data type for the field (e.g. int, float, unicode, etc.)'),
			Scalar(id='required',dataType='bool',optional=False,default=False,help='True if this field must be filled in'),
			Scalar(id='width',dataType='int',help='Field width'),
			Scalar(id='height',dataType='int',help='Field height'),
			Scalar(id='multiline',dataType='bool',optional=False,default=False,help='If True this is a mult-line text field'),
			Scalar(id='growVertically',dataType='bool',optional=False,default=False,help='If True this is field should grow vertically when the form expands'),
			Scalar(id='style',dataType='expression',help='wxWindows style flags for the field (use wx.XXX)'),
			Scalar(id='validate',dataType='function',help='Python function body that takes the field value (as C{value}) and returns an error if the value is incorrect')
		]),
		Instance(id='droplist',klass=fields.Droplist,help='Dropdown list/combo box',properties=[
			Scalar(id='id',dataType='str',optional=False,help='Identifier for the field'),
			Scalar(id='label',dataType='str',help='The label for the field'),
			Scalar(id='dataType',dataType='str',optional=False,default='unicode',help='Data type for the field (e.g. int, float, unicode, etc.)'),
			Scalar(id='required',dataType='bool',optional=False,default=False,help='True if this field must be filled in'),
			Scalar(id='width',dataType='int',help='Field width'),
			Scalar(id='height',dataType='int',help='Field height'),
			Scalar(id='combo',dataType='bool',default=False,optional=False,help='If true, this is a combo rather than a droplist (i.e. user can enter their own values'),
			Scalar(id='growVertically',dataType='bool',optional=False,default=False,help='If True this is field should grow vertically when the form expands'),
			Array(id='options',help='List of option values for the drop list',subSchemas=[
				Instance(id='option',klass=Option,help='A value for a dropdown-list option',properties=[
					Scalar(id='label',dataType='str',optional=False,help='The label to show on the list'),
					Scalar(id='value',dataType='str',optional=False,help='The value to store (this is checked and transformed using the field\'s dataType setting'),
				]),
			]),
			Scalar(id='validate',dataType='function',help='Python function body that takes the field value (as C{value}) and returns an error if the value is incorrect')
		]),
		Instance(id='date',klass=fields.Date,help='Date control',properties=[
			Scalar(id='id',dataType='str',optional=False,help='Identifier for the field'),
			Scalar(id='label',dataType='str',help='The label for the field'),
			Scalar(id='required',dataType='bool',optional=False,default=False,help='True if this field must be filled in'),
			Scalar(id='width',dataType='int',help='Field width'),
			Scalar(id='height',dataType='int',help='Field height'),
			Scalar(id='validate',dataType='function',help='Python function body that takes the field value (as C{value}) and returns an error if the value is incorrect')
		]),
	]),
])

schema = ConfigurationSchema(
	id = 'configuration',
	klass = Configuration,
	optional = False,
	help = 'Top-level element to hold all the configuration options', 
	properties = [
		Scalar(id='logToScreen',dataType='bool',help='If true, log entries will be printed to stdout as well as to the log file'),
		Scalar(id='logFile',dataType='str',optional=False,default='/var/log/dropbox2.log',help='Full path to the log file'),
		Scalar(id='screenLogLevel',dataType='expression',optional=False,default=50,help='Level of detail for stdout logging; one of DEBUG,INFO,WARNING,ERROR'),
		Scalar(id='fileLogLevel',dataType='expression',optional=False,default=50,help='Level of detail for file logging; one of DEBUG,INFO,WARNING,ERROR'),
		Scalar(id='pollInterval',dataType='float',optional=False,default=2.0,help='Interval at which to poll the directory for changes'),
		Scalar(id='sourceDirectory',dataType='str',optional=False,default='/var/dropbox/incoming',help='Directory that will be polled for new zip files with manifests'),
		Scalar(id='tempDir',dataType='str',optional=False,default='/tmp',help='Directory for temporary files'),
		Scalar(id='listenAddress',dataType='str',optional=False,default='localhost',help='IP address/hostname on which the dropbox HTTP/XMLRPC server should listen'),
		Scalar(id='listenPort',dataType='int',optional=False,default=80,help='Port number on which the dropbox HTTP/XMLRPC server should listen'),
		Scalar(id='publicAddress',dataType='str',optional=False,default='localhost',help='Public address/hostname through which clients will connect to this server'),
		Scalar(id='publicPort',dataType='int',optional=False,default=80,help='Public port number through which clients will connect to this server'),
		Scalar(id='globalSocketTimeout',dataType='int',optional=False,default=None,help='The timeout (in seconds) for all sockets in the system (be careful setting this as some long running operations, such as S3 upload, may break); leave blank to have an unlimited timeout'),
		Scalar(id='solrURL',default='http://localhost:8080/solr/',optional=False,dataType='str',help='The URL to Solr (with the trailing "/solr/")'),
		Scalar(id='md5sumPath',dataType='str',optional=False,default='/usr/bin/md5sum',help='Path to the md5sum programme'),
		Scalar(id='unzipPath',dataType='str',optional=False,default='/usr/bin/unzip',help='Path to the unzip programme'),
		Scalar(id='stateDB',dataType='str',optional=False,default='dropbox.shelve',help='File to use as the dropbox daemon state database'),
		Array(id='packageTypes',optional=False,help='Specifications for handling different file packages for upload',subSchemas=[
			Instance(id='packageType',help='Configuration for handing a particular kind of uploaded file package',klass=PackageType,properties=[
				Scalar(id='name',dataType='str',optional=False,help='The name of this package type; used in the dropdown in the client, etc.'),
				STANDARD_FORM,
				Array(id='fileTypes',optional=False,help='Specifications for handling different types of file within this package',subSchemas=[
					Instance(id='fileType',help='Definition of the manifest (form) fields',klass=FileType,properties=[
						Scalar(id='name',dataType='str',optional=False,help='Name of the file type (should be a valid python id)'),
						Scalar(id='description',dataType='str',optional=False,help='Description of the file type'),
						Scalar(id='extension',dataType='str',optional=False,help='File extension for files of this type (used to detect the type of file)'),
						STANDARD_FORM,
					]),
				]),
				Array(id='process',optional=False,subSchemas=[i.schema for i in processors.ProcesssorRegistry.processors]),
			]),
		]),
	],
)
"""

schema = ConfigurationSchema(
	id = 'configuration',
	klass = Configuration,
	optional = False,
	help = 'Top-level element to hold all the configuration options', 
	properties = [
		Scalar(id='logToScreen',dataType='bool',help='If true, log entries will be printed to stdout as well as to the log file'),
		Scalar(id='logFile',dataType='str',optional=False,default='bookscan.log',help='Full path to the log file'),
		Scalar(id='screenLogLevel',dataType='expression',optional=False,default=50,help='Level of detail for stdout logging; one of DEBUG,INFO,WARNING,ERROR'),
		Scalar(id='fileLogLevel',dataType='expression',optional=False,default=50,help='Level of detail for file logging; one of DEBUG,INFO,WARNING,ERROR'),
	],
)

if __name__ == '__main__':
	print schema.htmldoc() 
