import os
import re

book = 'John Middleton Murry Bibliog'

base = r'C:\books'

f = open(r'%s\%s\%s.bkr'%(base,book,book),'rb')
s = f.read()
l = re.findall('\xff\x00\x00\x00\x00\x004(.*?\\.tmp.*?\\.tmp)',s,re.MULTILINE|re.DOTALL)

files = []

for i in l:
	t = i.split('\n')
	original = t[0][:-1]
	final = r'%s\%s\%s_EDITED\%s'%(base,book,book,t[1])
	preview = r'%s\%s\%s_PREVIEW\%s'%(base,book,book,t[2])
	
	files.append(
		(original,final,preview)
	)

files.sort()

for original,final,preview in files:
	orig = os.path.split(original)[-1]
	new = r'%s\%s\%s'%(
		base,
		book,
		orig.split('.')[0] + '.tif'
	)
	try:
		os.rename(final,new)
		print '       %s -> %s'%(final,new)
	except:
		print 'FAILED %s -> %s'%(final,new)
	