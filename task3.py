book = open('/Home/Desktop/Fizzbuzz-ShukaiLiu/fizzbuzz/fizzbuzz/Book1.txt')
word = open('/Home/Desktop/Fizzbuzz-ShukaiLiu/fizzbuzz/fizzbuzz/20K.txt')
def func1():
	for line in book:
		for strs in  word.readlines():
			if line.strip() not in strs.strip():
				print(line.strip())
			else:
				continue
			with open("book1uniqu_list.txt","wt") as file:
				file.write(line.strip())

def func2():
        for line in book:
                for strs in  word.readlines():
                        if line.strip() in strs.strip():
                                print(line.strip())
                        else:
                                continue
			with open("rarewords_list.txt","wt") as file:
                                file.write(line.strip())
