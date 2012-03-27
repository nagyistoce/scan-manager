import Image
import os
import glob

base = r'C:\systems\bookscan\hidden huxley'
base += '\\'

files = glob.glob(base+'*.jpg')

for index,fn in enumerate(files):
	i = Image.open(fn)
	i.save(fn[:-3] + 'png')
	print 'done %d/%d'%(index+1,len(files))
	