import os

def listFilestotext(dir, file, wildcard, recursion):
	exts = wildcard.split(' ')
	for root, subdirs, files in os.walk(dir):
		for name in files:
			for ext in exts:
				if name.endwith(ext):
					file.write(name + "\n")
					break
		if not recursion:
			break
def test():
	dir = "/Desktop/Fizzbuzz-ShukaiLiu/fizzbuzz/fizzbuzz"
	outfile = 'binaries.txt'
	wildcard = '.txt .exe .dll .lib'
	file = open(outfile, 'w')
	if not file:
		print('cannot open the file %s for writing' % outfile)
	listFilestotxt(dir, file, wildcard, 0)
	file.close()

test()
