def replace():
	myfile = open("","wt")
	for line in myfile.readlines():
		for word in line:
		if word[-2:] == 'er':
			word = word[:-2] + word[-2:].replace('er','xor')
			print(word)
			for i in word:
				if i == 'o' or i == 'O':
					i = '0'
				elif i == 'a' or i == 'A':
					i = '4'
				elif i == 'e' or i == 'E':
					i = '3'
				elif i == 'i' or i == 'I':
					i = '1'
				print(i,end = '')
	myfile.close()
