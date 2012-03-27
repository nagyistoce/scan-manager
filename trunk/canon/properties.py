from defines import *
from collections import OrderedDict

__all__ = ['properties']

class PropertyDescriptions(object):

	def __init__(self):
		
		self.value2desc = {}
		self.name2desc = {}
	
	def __getitem__(self,k):
		if isinstance(k,basestring):
			return self.name2desc[k]
		else:
			return self.value2desc[k]

	def __getattr__(self,k):
		return self[k]
		
	def add(self,desc):
		self.value2desc[desc.code] = desc
		self.name2desc[desc.name] = desc
	
	def getValueName(self,k,v):
		if k in self:
			return self[k][v]

	def getDescription(self,k):
		if k in self:
			return self[k].description

	def getValue(self,k,v):
		if k in self:
			return self[k][v]
	
	def __contains__(self,k):
		if isinstance(k,basestring):
			return k in self.name2desc
		else:
			return k in self.value2desc
		
	def __iter__(self):
		for v in self.value2desc.values():
			yield v


		
properties = PropertyDescriptions()



class PropertyDescription(object):

	def __init__(self,**kargs):
		self.__dict__.update(kargs)
		self.name2value = {}
		for k,v in self.values.items():
			self.name2value[v] = k
		properties.add(self)
		
	def __getitem__(self,k):
		if isinstance(k,basestring):
			if k not in self.name2value: return None
			return self.name2value[k]
		else:
			if k not in self.values: return None
			return self.values[k]
			
	def __contains__(self,k):
		if isinstance(k,basestring):
			return k in self.name2value
		else:
			return k in self.values

	def __iter__(self):
		for v,k in self.values.items():
			yield (k,v)

		

PropertyDescription(
	code = DevicePropCode.PHOTO_EFFECT,
	name = u'PHOTO_EFFECT',
	description = u'Indicates the photo effect.',
	values = OrderedDict([
		(0x0000, u'Off'),
		(0x0001, u'Vivid'),
		(0x0002, u'Neutral'),
		(0x0003, u'Soft'),
		(0x0004, u'Sepia'),
		(0x0005, u'Monochrome'),
]))
PropertyDescription(
	code = DevicePropCode.AF_MODE,
	name = u'AF_MODE',
	description = u'Indicates the auto-focus mode set by a capture parameter.',
	values = OrderedDict([
		(0x00, u'Single Shot'),
		(0x01, u'AI Servo'),
		(0x02, u'AI Focus'),
		(0x03, u'Manual'),
		(0x04, u'Continuous'),
]))
PropertyDescription(
	code = DevicePropCode.PARAMETER_SET,
	name = u'PARAMETER_SET',
	description = u'Sets the selectable mode of development parameters.',
	values = OrderedDict([
		(0x0008, u'Standard Development Parameters'),
		(0x0010, u'Development Parameters 1'),
		(0x0020, u'Development Parameters 2'),
		(0x0040, u'Development Parameters 3'),
		(0xffff, u'Invalid or the setting is not changed.'),
]))
PropertyDescription(
	code = DevicePropCode.SELFTIMER,
	name = u'SELFTIMER',
	description = u'Indicates the self-timer setting.',
	values = OrderedDict([
		(0, u'Self-timer Not Used'),
		(0x0064, u'Self-timer: 10 Seconds'),
		(0x0014, u'Self-timer: 2 Seconds'),
		(0xFFFF, u'Invalid or the setting is not changed.'),
]))
PropertyDescription(
	code = DevicePropCode.BATTERY_KIND,
	name = u'BATTERY_KIND',
	description = u'Indicates the type of the battery installed in the device.',
	values = OrderedDict([
		(0x0000, u'Unknown'),
		(0x0001, u'AC power supply'),
		(0x0002, u'Lithium ion battery'),
		(0x0003, u'Nickel hydride battery'),
		(0x0004, u'Nickel cadmium battery'),
		(0x0005, u'Alkaline manganese battery'),
]))
PropertyDescription(
	code = DevicePropCode.BATTERY_STATUS,
	name = u'BATTERY_STATUS',
	description = u'Indicates the battery condition in the device.',
	values = OrderedDict([
		(0x00, u'Not defined.'),
		(0x01, u'Economy'),
		(0x02, u'Normal'),
		(0x03, u'Fine'),
		(0x04, u'Lossless'),
		(0x05, u'SuperFine'),
]))
PropertyDescription(
	code = DevicePropCode.WB_SETTING,
	name = u'WB_SETTING',
	description = u'Indicates the white balance set by a capture parameter.',
	values = OrderedDict([
		(0x0, u'Auto'),
		(0x1, u'Daylight'),
		(0x2, u'Cloudy'),
		(0x3, u'Tungsten'),
		(0x4, u'Fluorescent'),
		(0x6, u'Preset'),
		(0x7, u'Fluorescent H'),
		(0x9, u'Color Temperature'),
		(0x10, u'Custom White Balance PC-1'),
		(0x11, u'Custom White Balance PC-2'),
		(0x12, u'Custom White Balance PC-3'),
		(0x13, u'Missing number'),
		(0x14, u'Fluorescent H'),
		(0xff, u'Invalid or the setting is not changed.'),
]))
PropertyDescription(
	code = DevicePropCode.TV,
	name = u'TV',
	description = u'Indicates the exposure compensation value.',
	values = OrderedDict([
		(0x04, u'Bulb'),
		(0x10, u"30'"),
		(0x13, u"25'"),
		(0x14, u"20'"),
		(0x15, u"20' (1/3)"),
		(0x18, u"15'"),
		(0x1b, u"13'"),
		(0x1c, u"10'"),
		(0x1d, u"10' (1/3)"),
		(0x20, u"8'"),
		(0x23, u"6' (1/3)"),
		(0x24, u"6'"),
		(0x25, u"5'"),
		(0x28, u"4'"),
		(0x2b, u"3'2"),
		(0x2c, u"3'"),
		(0x2d, u"2'5"),
		(0x30, u"2'"),
		(0x33, u"1'6"),
		(0x34, u"1'5"),
		(0x35, u"1'3"),
		(0x38, u"1'"),
		(0x3b, u"0'8"),
		(0x3c, u"0'7"),
		(0x3d, u"0'6"),
		(0x40, u"0'5"),
		(0x43, u"0'4"),
		(0x44, u"0'3"),
		(0x45, u"0'3 (1/3)"),
		(0x48, u'1/4'),
		(0x4b, u'1/5'),
		(0x4c, u'1/6'),
		(0x4d, u'1/6 (1/3)'),
		(0x50, u'1/8'),
		(0x53, u'1/10 (1/3)'),
		(0x54, u'1/10'),
		(0x55, u'1/13'),
		(0x58, u'1/15'),
		(0x5b, u'1/20 (1/3)'),
		(0x5c, u'1/20'),
		(0x5d, u'1/25'),
		(0x60, u'1/30'),
		(0x63, u'1/40'),
		(0x64, u'1/45'),
		(0x65, u'1/50'),
		(0x68, u'1/60'),
		(0x6b, u'1/80'),
		(0x6c, u'1/90'),
		(0x6d, u'1/100'),
		(0x70, u'1/125'),
		(0x73, u'1/160'),
		(0x74, u'1/180'),
		(0x75, u'1/200'),
		(0x78, u'1/250'),
		(0x7b, u'1/320'),
		(0x7c, u'1/350'),
		(0x7d, u'1/400'),
		(0x80, u'1/500'),
		(0x83, u'1/640'),
		(0x84, u'1/750'),
		(0x85, u'1/800'),
		(0x88, u'1/1000'),
		(0x8b, u'1/1250'),
		(0x8c, u'1/1500'),
		(0x8d, u'1/1600'),
		(0x90, u'1/2000'),
		(0x93, u'1/2500'),
		(0x94, u'1/3000'),
		(0x95, u'1/3200'),
		(0x98, u'1/4000'),
]))
PropertyDescription(
	code = DevicePropCode.CAMERA_OUTPUT,
	name = u'CAMERA_OUTPUT',
	description = u'Indicates the destination of image signal output in the Viewfinder mode.',
	values = OrderedDict([
		(0x0000, u'Not defined.'),
		(0x0001, u'LCD'),
		(0x0002, u'Video OUT'),
		(0x0003, u'Off'),
]))
PropertyDescription(
	code = DevicePropCode.ML_SPOT_POS,
	name = u'ML_SPOT_POS',
	description = u'Indicates the spot metering position.',
	values = OrderedDict([
		(0x0, u'MlSpotPosCenter'),
		(0x1, u'MlSpotPosAfLink'),
]))
PropertyDescription(
	code = DevicePropCode.FOCUS_POINT_SETTING,
	name = u'FOCUS_POINT_SETTING',
	description = u'Set the selection mode for focusing point.',
	values = OrderedDict([
		(0x0000, u'Invalid or the setting is not changed.'),
		(0x1000, u'Focusing Point on Center Only, Manual'),
		(0x1001, u'Focusing Point on Center Only, Auto'),
		(0x3000, u'Multiple Focusing Points (No Specification), Manual'),
		(0x3001, u'Multiple Focusing Points, Auto'),
		(0x3002, u'Multiple Focusing Points (Right)'),
		(0x3003, u'Multiple Focusing Points (Center)'),
		(0x3004, u'Multiple Focusing Points (Left)'),
]))
PropertyDescription(
	code = DevicePropCode.ML_WEI_MODE,
	name = u'ML_WEI_MODE',
	description = u'Set the metering method.',
	values = OrderedDict([
		(0x00, u'Center-weighted Metering'),
		(0x01, u'Spot Metering'),
		(0x02, u'Average Metering'),
		(0x03, u'Evaluative Metering'),
		(0x04, u'Partial Metering'),
		(0x05, u'Center-weighted Average Metering'),
		(0x06, u'Spot Metering Interlocked with AF Frame'),
		(0x07, u'Multi-Spot Metering'),
		(0xFF, u'Invalid or the setting is not changed.'),
]))
PropertyDescription(
	code = DevicePropCode.ISO,
	name = u'ISO',
	description = u'Indicates the ISO value set by a capture parameter.',
	values = OrderedDict([
		(0x00, 'Auto'),
		(0x28, '6'),
		(0x30, '12'),
		(0x38, '25'),
		(0x40, '50'),
		(0x43, '64'),
		(0x45, '80'),
		(0x48, '100'),
		(0x50, '200'),
		(0x58, '400'),
		(0x60, '800'),
		(0x68, '1600'),
		(0x70, '3200'),
		(0x78, '6400'),
]))
PropertyDescription(
	code = DevicePropCode.IMAGE_SIZE,
	name = u'IMAGE_SIZE',
	description = u'Indicates the image size set by a capture parameter.',
	values = OrderedDict([
		(0x00, u'Large'),
		(0x01, u'Medium 1'),
		(0x02, u'Small'),
		(0x03, u'Medium 2'),
		(0x07, u'Medium 3'),
]))
PropertyDescription(
	code = DevicePropCode.DISP_AV,
	name = u'DISP_AV',
	description = u'Indicates how to display the Av value as described in &quot;Reference&quot;.',
	values = OrderedDict([
		(0x0000, u'1/3 Level'),
		(0x0001, u'A value corresponding to one-tenth the value retrieved by prPTP_DEV_PROP_AV_OPEN_APEX is displayed.'),
]))
PropertyDescription(
	code = DevicePropCode.BUZZER,
	name = u'BUZZER',
	description = u'Sets on/off of the device buzzer.',
	values = OrderedDict([
		(0x0000, u'On'),
		(0x0001, u'Off'),
]))
PropertyDescription(
	code = DevicePropCode.STROBE_SETTING,
	name = u'STROBE_SETTING',
	description = u'Indicates the flash set by a capture parameter.',
	values = OrderedDict([
		(0x00, u'Off'),
		(0x01, u'Auto'),
		(0x02, u'On'),
		(0x03, u'Red Eye Suppression'),
		(0x04, u'Low-speed Synchronization'),
		(0x05, u'Auto + Red Eye Suppression'),
		(0x06, u'On + Red Eye Suppression'),
]))
PropertyDescription(
	code = DevicePropCode.EZOOM,
	name = u'EZOOM',
	description = u'Indicates the starting position of electronic zoom set by a capture parameter.',
	values = OrderedDict([
		(0x00, u'Off'),
		(0x01, u'x2'),
		(0x02, u'x4'),
		(0x03, u'Smooth'),
]))
PropertyDescription(
	code = DevicePropCode.AV,
	name = u'AV',
	description = u'Indicates the aperture value.',
	values = OrderedDict([
		(0x08, u'1.0'),
		(0x0b, u'1.1'),
		(0x0c, u'1.2'),
		(0x0d, u'1.2 (1/3)'),
		(0x10, u'1.4'),
		(0x13, u'1.6'),
		(0x14, u'1.8'),
		(0x15, u'1.8 (1/3)'),
		(0x18, u'2.0'),
		(0x1b, u'2.2'),
		(0x1c, u'2.5'),
		(0x1d, u'2.5 (1/3)'),
		(0x20, u'2.8'),
		(0x23, u'3.2'),
		(0x24, u'3.5'),
		(0x25, u'3.5 (1/3)'),
		(0x28, u'4.0'),
		(0x2b, u'4.5 (1/3)'),
		(0x2c, u'4.5'),
		(0x2d, u'5.6 (1/3)'),
		(0x30, u'5.6'),
		(0x33, u'6.3'),
		(0x34, u'6.7'),
		(0x35, u'7.1'),
		(0x38, u'8.0'),
		(0x3b, u'9.0'),
		(0x3c, u'9.5'),
		(0x3d, u'10'),
		(0x40, u'11'),
		(0x43, u'13 (1/3)'),
		(0x44, u'13'),
		(0x45, u'14'),
		(0x48, u'16'),
		(0x4b, u'18'),
		(0x4c, u'19'),
		(0x4d, u'20'),
		(0x50, u'22'),
		(0x53, u'25'),
		(0x54, u'27'),
		(0x55, u'29'),
		(0x58, u'32'),
		(0x5b, u'36'),
		(0x5c, u'38'),
		(0x5d, u'40'),
		(0x60, u'45'),
		(0x63, u'51'),
		(0x64, u'54'),
		(0x65, u'57'),
		(0x68, u'64'),
		(0x6b, u'72'),
		(0x6c, u'76'),
		(0x6d, u'81'),
		(0x70, u'91'),
]))
PropertyDescription(
	code = DevicePropCode.EXPOSURE_MODE,
	name = u'EXPOSURE_MODE',
	description = u'Indicates the exposure mode selected.',
	values = OrderedDict([
		(0x00, 'Auto'),
		(0x01, 'P'),
		(0x02, 'Tv'),
		(0x03, 'Av'),
		(0x04, 'M'),
		(0x05, 'A_DEP'),
		(0x06, 'M_DEP'),
		(0x07, 'Bulb'),
		(0x80, 'CAMERAM'),
		(0x81, 'MYCOLOR'),
		(0x82, 'PORTRAIT'),
		(0x83, 'LANDSCAPE'),
		(0x84, 'NIGHTSCENE'),
		(0x85, 'FOREST'),
		(0x86, 'SNOW'),
		(0x87, 'BEACH'),
		(0x88, 'FIREWORKS'),
		(0x89, 'PARTY'),
		(0x8A, 'NIGHTSNAP'),
		(0x8B, 'STITCH'),
		(0x8C, 'MOVIE'),
		(0x8D, 'CUSTOM'),
		(0x8E, 'INTERVAL'),
		(0x8F, 'DIGITALMACRO'),
		(0x90, 'LONGSHUTTER'),
		(0x91, 'UNDERWATER'),
		(0x92, 'KIDSANDPETS'),
		(0x93, 'FASTSHUTTER'),
		(0x94, 'SLOWSHUTTER'),
		(0x95, 'CUSTOM1'),
		(0x96, 'CUSTOM2'),
		(0x97, 'NEUTRAL'),
		(0x98, 'GRAY'),
		(0x99, 'SEPIA'),
		(0x9A, 'VIVID'),
		(0x9B, 'SPORTS'),
		(0x9C, 'MACRO'),
		(0x9D, 'SUPERMACRO'),
		(0x9E, 'PANFOCUS'),
		(0x9F, 'BW'),
		(0xA0, 'FLASHINHIBIT'),
]))
PropertyDescription(
	code = DevicePropCode.SLOW_SHUTTER_SETTING,
	name = u'SLOW_SHUTTER_SETTING',
	description = u'Sets the low-speed shutter.',
	values = OrderedDict([
		(0x00, u'Off'),
		(0x01, u'Night View'),
		(0x02, u'On'),
		(0x03, u'Low-speed shutter function not available.'),
		(0xFF, u'Invalid or the setting is not changed.'),
]))
PropertyDescription(
	code = DevicePropCode.COMP_QUALITY,
	name = u'COMP_QUALITY',
	description = u'Indicates the image quality set by a capture parameter.',
	values = OrderedDict([
		(0x00, u'Not defined'),
		(0x01, u'Economy'),
		(0x02, u'Normal'),
		(0x03, u'Fine'),
		(0x04, u'Lossless'),
		(0x05, u'SuperFine'),
]))
PropertyDescription(
	code = DevicePropCode.ROTATION_ANGLE,
	name = u'ROTATION_ANGLE',
	description = u'Indicates the angle of rotation detected by the gravity sensor.',
	values = OrderedDict([
		(0x0000, u'0 Degree'),
		(0x0001, u'90 Degrees'),
		(0x0002, u'180 Degrees'),
		(0x0003, u'270 Degrees'),
		(0xffff, u'None'),
]))
PropertyDescription(
	code = DevicePropCode.ROTATION_SENSE,
	name = u'ROTATION_SENSE',
	description = u'Indicates the angle of rotation detected by the gravity sensor.',
	values = OrderedDict([
		(0x0000, u'Enable'),
		(0x0001, u'Disable'),
		(0xffff, u'None'),
]))
PropertyDescription(
	code = DevicePropCode.COLOR_GAIN,
	name = u'COLOR_GAIN',
	description = u'Indicates the color compensation set by a capture parameter.',
	values = OrderedDict([
		(-0x2, u'Low 2'),
		(-0x1, u'Low'),
		(0x0, u'Standard'),
		(0x1, u'High'),
		(0x2, u'High 2'),
]))
PropertyDescription(
	code = DevicePropCode.DISP_AV_MAX,
	name = u'DISP_AV_MAX',
	description = u'Indicates how to display the maximum Av value as described in &quot;Reference&quot;.',
	values = OrderedDict([
		(0x0000, u'1/3 Level'),
		(0x0001, u'A value corresponding to one-tenth the value retrieved by prPTP_DEV_PROP_AV_MAX_APEX is displayed.'),
]))
PropertyDescription(
	code = DevicePropCode.SENSITIVITY,
	name = u'SENSITIVITY',
	description = u'Sets the sensitivity.',
	values = OrderedDict([
		(0x0, u'Standard'),
		(0x1, u'Upper 1'),
		(0x2, u'Upper 2'),
		(0xFF, u'Invalid or not set.'),
]))
PropertyDescription(
	code = DevicePropCode.SHARPNESS,
	name = u'SHARPNESS',
	description = u'Indicates the sharpness set by a capture parameter.',
	values = OrderedDict([
		(-0x2, u'Low 2'),
		(-0x1, u'Low'),
		(0x0, u'Standard'),
		(0x1, u'High'),
		(0x2, u'High 2'),
]))
PropertyDescription(
	code = DevicePropCode.AF_LIGHT,
	name = u'AF_LIGHT',
	description = u'Indicates the on/off of AF-assist light.',
	values = OrderedDict([
		(0x0000, u'Off'),
		(0x0001, u'On'),
]))
PropertyDescription(
	code = DevicePropCode.BEEP,
	name = u'BEEP',
	description = u'Indicates the buzzer set by a capture parameter.',
	values = OrderedDict([
		(0x00, u'Off'),
		(0x01, u'On'),
]))
PropertyDescription(
	code = DevicePropCode.AF_DISTANCE,
	name = u'AF_DISTANCE',
	description = u'Indicates information relating to the search range in the AF mode.',
	values = OrderedDict([
		(0x0, u'Manual'),
		(0x01, u'Auto'),
		(0x02, u'Unknown'),
		(0x03, u'Zone Focus (Close-up)'),
		(0x04, u'Zone Focus (Very Close )'),
		(0x05, u'Zone Focus (Close)'),
		(0x06, u'Zone Focus (Medium)'),
		(0x07, u'Zone Focus (Far)'),
		(0x08, u'Zone Focus (Reserved 1)'),
		(0x09, u'Zone Focus (Reserved 2)'),
		(0x0A, u'Zone Focus (Reserved 3)'),
		(0x0B, u'Zone Focus (Reserved 4)'),
		(0xFF, u'Invalid or the setting is not changed.'),
]))
PropertyDescription(
	code = DevicePropCode.IMAGE_MODE,
	name = u'IMAGE_MODE',
	description = u'Indicates the image mode to be applied at capture.',
	values = OrderedDict([
		(0x00, u'Auto'),
		(0x01, u'Manual'),
		(0x02, u'Distant View'),
		(0x03, u'High-speed Shutter'),
		(0x04, u'Low-speed Shutter'),
		(0x05, u'Night View'),
		(0x06, u'Grayscale'),
		(0x07, u'Sepia'),
		(0x08, u'Portrait'),
		(0x09, u'Sports'),
		(0x0A, u'Macro'),
		(0x0B, u'Monochrome'),
		(0x0C, u'Pan Focus'),
		(0x0D, u'Neutral'),
		(0x0E, u'Soft'),
]))
PropertyDescription(
	code = DevicePropCode.CAPTURE_TRANSFER_MODE,
	name = u'CAPTURE_TRANSFER_MODE',
	description = u'Indicates the image transfer mode to be applied at capture.',
	values = OrderedDict([
		(0x0000, u'Not defined.'),
		(0x0002, u'Transfer Entire Image to PC'),
		(0x0004, u'Save Thumbnail Image to Device (A JPEG image will be saved as a normal JPEG file together with the entire image.)'),
		(0x0008, u'Save Entire Image to Device (A JPEG image will be saved as a normal JPEG file together with a thumbnail image.)'),
]))
PropertyDescription(
	code = DevicePropCode.FULLVIEW_FILE_FORMAT,
	name = u'FULLVIEW_FILE_FORMAT',
	description = u'Indicates the image type set by a capture parameter.',
	values = OrderedDict([
		(0x00, u'Not defined.'),
		(0x01, u'JPEG'),
		(0x02, u'CRW'),
]))
PropertyDescription(
	code = DevicePropCode.DRIVE_MODE,
	name = u'DRIVE_MODE',
	description = u'Sets the drive mode.',
	values = OrderedDict([
		(0x00, u'Single-frame Shooting'),
		(0x01, u'Continuous Shooting'),
		(0x02, u'Timer (Single) Shooting'),
		(0x04, u'Continuous Low-speed Shooting'),
		(0x05, u'Continuous High-speed Shooting'),
		(0xFF, u'Invalid or the setting is not changed.'),
]))
PropertyDescription(
	code = DevicePropCode.CONTRAST,
	name = u'CONTRAST',
	description = u'Indicates the contrast set by a capture parameter.',
	values = OrderedDict([
		(-0x2, u'Low 2'),
		(-0x1, u'Low'),
		(0x0, u'Standard'),
		(0x1, u'High'),
		(0x2, u'High 2'),
]))
PropertyDescription(
	code = DevicePropCode.EXPOSURE_COMP,
	name = u'EXPOSURE_COMP',
	description = u'Indicates exposure compensation.',
	values = OrderedDict([
		(0x00, '+3'),
		(0x03, '+2 (2/3)'),
		(0x04, '+2 (1/2)'),
		(0x05, '+2 (1/3)'),
		(0x08, '+2'),
		(0x0b, '+1 (2/3)'),
		(0x0c, '+1 (1/2)'),
		(0x0d, '+1 (1/3)'),
		(0x10, '+1'),
		(0x13, '+2/3'),
		(0x14, '+1/2'),
		(0x15, '+1/3'),
		(0x18, '0'),
		(0x1b, '-1/3'),
		(0x1c, '-1/2'),
		(0x1d, '-2/3'),
		(0x20, '-1'),
		(0x23, '-1 (1/3)'),
		(0x24, '-1 (1/2)'),
		(0x25, '-1 (2/3)'),
		(0x28, '-2'),
		(0x2b, '-2 (1/3)'),
		(0x2c, '-2 (1/2)'),
		(0x2d, '-2 (2/3)'),
		(0x30, '-3'),
]))
PropertyDescription(
	code = DevicePropCode.AEB_EXPOSURE_COMP,
	name = u'AEB_EXPOSURE_COMP',
	description = u'Indicates AEB exposure compensation.',
	values = OrderedDict([
		(0x00, '+3'),
		(0x03, '+2 (2/3)'),
		(0x04, '+2 (1/2)'),
		(0x05, '+2 (1/3)'),
		(0x08, '+2'),
		(0x0b, '+1 (2/3)'),
		(0x0c, '+1 (1/2)'),
		(0x0d, '+1 (1/3)'),
		(0x10, '+1'),
		(0x13, '+2/3'),
		(0x14, '+1/2'),
		(0x15, '+1/3'),
		(0x18, '0'),
		(0x1b, '-1/3'),
		(0x1c, '-1/2'),
		(0x1d, '-2/3'),
		(0x20, '-1'),
		(0x23, '-1 (1/3)'),
		(0x24, '-1 (1/2)'),
		(0x25, '-1 (2/3)'),
		(0x28, '-2'),
		(0x2b, '-2 (1/3)'),
		(0x2c, '-2 (1/2)'),
		(0x2d, '-2 (2/3)'),
		(0x30, '-3'),
]))
PropertyDescription(
	code = DevicePropCode.FLASH_COMP,
	name = u'FLASH_COMP',
	description = u'Indicates flash exposure compensation.',
	values = OrderedDict([
		(0x00, '+3'),
		(0x03, '+2 (2/3)'),
		(0x04, '+2 (1/2)'),
		(0x05, '+2 (1/3)'),
		(0x08, '+2'),
		(0x0b, '+1 (2/3)'),
		(0x0c, '+1 (1/2)'),
		(0x0d, '+1 (1/3)'),
		(0x10, '+1'),
		(0x13, '+2/3'),
		(0x14, '+1/2'),
		(0x15, '+1/3'),
		(0x18, '0'),
		(0x1b, '-1/3'),
		(0x1c, '-1/2'),
		(0x1d, '-2/3'),
		(0x20, '-1'),
		(0x23, '-1 (1/3)'),
		(0x24, '-1 (1/2)'),
		(0x25, '-1 (2/3)'),
		(0x28, '-2'),
		(0x2b, '-2 (1/3)'),
		(0x2c, '-2 (1/2)'),
		(0x2d, '-2 (2/3)'),
		(0x30, '-3'),
]))
