import sys

class FileInfo:
	"""Class to hold information about a file"""
	
	def __init__(self, fileUrl, fileName, infoUrl, output=sys.stdout):
		"""Constructor for a fileInfo object"""
		self.fileUrl = fileUrl
		self.fileName = fileName
		self.infoUrl = infoUrl
		self.output = output

		self.description = ""
		self.repository = ""
		self.category = ""
		self.fileSize = ""
		self.fileDate = ""
		self.sourceCode = ""
		self.author = ""
		self.downloads = ""
		self.documentation = ""

		self.fileinfo = ""

	def __str__(self):
		return self.fileName + " located at " + self.fileUrl
		
	def __repr__(self):
		return self.fileName + " located at " + self.fileUrl

	def printDatum(self, text, datum, stdout = None):
		if stdout == None:
			stdout = self.output
		if datum != "":
			result = text + datum
			# Enforce 80 characters per line to make this friendly.
			index = 0
			actual = ""
			strings = result.split(" ")
			for separated in strings:
				if (index + len(separated) < 80) and not "\n" in separated:
					index += len(separated)
					actual += separated + " "
				elif "\n" in separated:
					end, newline, beginning = separated.partition("\n")
					while "\n" in beginning:
						actual += end + "\n" + (" " * (len(text) - 2)) + ": "
						index = len(beginning) + len(text)
						end, newline, beginning = beginning.partition("\n")
					actual += end + "\n" + (" " * (len(text) - 2)) + ": " + beginning + " "
					index = len(beginning) + len(text)
				else:
					actual += "\n" + (" " * (len(text) - 2)) + ": " + separated + " "
					index = len(text)
			print >> stdout, actual
#			print(actual, stdout)

	def printData(self, output = sys.stdout):
		"""Output all the file data to be written to any writable output"""
		self.printDatum("Name          : ", self.fileName, output)
		self.printDatum("Author        : ", self.author, output)
		self.printDatum("Repository    : ", self.repository, output)
		self.printDatum("Category      : ", self.category, output)
		self.printDatum("Downloads     : ", self.downloads, output)
		self.printDatum("Date Uploaded : ", self.fileDate, output)
		self.printDatum("File Size     : ", self.fileSize, output)
		self.printDatum("Documentation : ", self.documentation, output)
		self.printDatum("Source Code   : ", self.sourceCode, output)
		self.printDatum("Description   : ", self.description, output)
#		print("\n", output)
		print >> output, "\n\n"
