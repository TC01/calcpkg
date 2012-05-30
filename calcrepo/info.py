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
		return self.fileName + " located at " + fileUrl
		
	def __repr__(self):
		return self.fileName + " located at " + fileUrl

	def printDatum(self, text, datum, stdout = None):
		if stdout == None:
			stdout = self.output
		if datum != "":
			print >> stdout, text + datum

	def printData(self, output = sys.stdout):
		"""Output all the file data to be written to any writable output"""
		self.printDatum("Name          : ", self.fileName)
		self.printDatum("Author        : ", self.author)
		self.printDatum("Repository    : ", self.repository)
		self.printDatum("Category      : ", self.category)
		self.printDatum("Downloads     : ", self.downloads)
		self.printDatum("Date Uploaded : ", self.fileDate)
		self.printDatum("File Size     : ", self.fileSize)
		self.printDatum("Documentation : ", self.documentation)
		self.printDatum("Source Code   : ", self.sourceCode)
		self.printDatum("Description   : ", self.description + "\n")
