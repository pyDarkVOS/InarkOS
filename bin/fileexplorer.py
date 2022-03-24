import os
from msvcrt import *
import sys
w, h = os.get_terminal_size()
selidx = 0
newidx = selidx
done = 0
paths = ['MainDrive']

def update(path):
	os.system('cls')
	files = os.listdir(path)
	if len(paths) != 1:
		files.append('>back<')
	files.append('>quit<')
	for i in range(len(files)):
		if i == selidx:
			print('* ', end='')
		else:
			print('  ', end='')
		print(files[i])
	return len(files), files

if '--run' in sys.argv:
	try:
		usr = sys.argv[sys.argv.index('--user')+1]
		path = 'MainDrive/'
		while not done:
			length, items = update(paths[-1])
			key = ord(getch()) 
			if key == 224:
				keyc = ord(getch())
				if keyc == 80:
					if selidx != length-1:
						selidx += 1
						newidx = selidx
				if keyc == 72:
					if selidx != 0:
						selidx -= 1
						newidx = selidx
			if key == 13 and selidx == length-1:
				os.system('cls')
				done = 1
			elif key == 13:
				if items[selidx] != '>back<' and os.path.isdir(paths[-1] + '/' + items[selidx]):
					paths.append(paths[-1] + '/' + items[selidx])
					selidx = 0
				if items[selidx] == '>back<':
					del paths[-1]
					selidx = 0
				if items[selidx] != '>back<' and os.path.isfile(paths[-1] + '/' + items[selidx]):
					os.system(f'python3 bin/texteditor.py --run --user {usr} --file ' + paths[-1] + '/' + items[selidx])
	except Exception as e:
		print(e)