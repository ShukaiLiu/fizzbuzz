import os
import os.path

class Traverse:
	def __init__(self, workdir):
		self.workdir = workdir

	def traversefile(self, workdir):
		count = 1
		for filename in os.listdir(workdir):
			file = os.path.join(workdir, filename)
			if os.path.isdir(file):
				print(file)
				count += self.traversefile(file)
			else:
				continue
		return count
