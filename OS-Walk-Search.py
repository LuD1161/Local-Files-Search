import os , re
import sys, pprint
search = raw_input("Enter File Name to search For : ")
fileList = []
filecount=0
rx = re.compile(search,re.IGNORECASE)
rootdir = raw_input("Enter Directory to search in : (To search in present directory leave blank)")
if(rootdir==""):
	rootdir='.'
for root, dirs, files in os.walk(rootdir, topdown=True):
    for name in files:
	count=0	
	m = rx.search(name)
	if m:
		dest=os.path.join(root,name)
		count=1		
		print('Found at : '+dest[1:])
		filecount=filecount+1
	if count==0:
		for name in dirs:
			m = rx.search(name)
			if m:
				dest=os.path.join(root,name)
				count=1		
				print('Found at : '+dest[1:])
				filecount=filecount+1
print('Total Files found : '+str(filecount))

