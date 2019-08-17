import os, platform

sdelete = 'sdelete64' if platform.machine().endswith('64') else 'sdelete'

file_list = 'list.txt'
try:
	with open(file_list) as f:
		files = f.readlines()
		for file in files:
			os.system("%s -s -r -nobanner -p 3 \"%s\"" % (sdelete, file))
	f.close()
except IOError:
	print("No file named list.txt found")
	

os.system("%s -s -r -nobanner -p 3 \"%s\"" % (sdelete, file_list))

print('All done have fun!')
os.system("rmdir /Q /S \"%s\"" % os.path.dirname(os.path.realpath(__file__)))
os.system("cls")