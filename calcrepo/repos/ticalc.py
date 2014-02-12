import urllib

from calcrepo import info
from calcrepo import repo

name = "ticalc"
url = "http://www.ticalc.org/"
enabled = True

class TicalcRepository(repo.CalcRepository):
			
	def formatDownloadUrl(self, url):
		return "http://www.ticalc.org" + url
		
	def updateRepoIndexes(self, verbose=False):
		self.printd("Reading ticalc.org master index (this will take some time).")
		
		# First read in the text (the only network process involved)
		masterIndex = urllib.urlopen('http://www.ticalc.org/pub/master.index').read()
		self.printd("  Read in ticalc.org master index.")

		# Delete and open new indices
		files = self.openIndex(self.index.fileIndex, "files index")
		names = self.openIndex(self.index.nameIndex, "names index")
		if files is None or names is None:
			try:
				files.close()
			except:
				return

		# Now, parse the enormous data and write index files
		self.printd(" ")
		masterIndex = masterIndex[39:]
		directory = ""
		while len(masterIndex) > 2:
			line = masterIndex[:masterIndex.find('\n')]
			masterIndex = masterIndex[masterIndex.find('\n') + 1:]
			if line == "":
				continue
			if line[:9] == "Index of ":
				dirData = line[9:]
				directory = dirData[:dirData.find(" ")]
				if verbose:
					self.printd("  Caching " + line[9:])
			else:
				fileData = line[:line.find(" ")]
				files.write(directory + '/' + fileData + '\n')
				nameData = line[len(fileData)+1:].lstrip()
				names.write(nameData + '\n')
		
		# Close the indexes now
		files.close()
		names.close()
		self.printd("Finished updating ticalc.org repo.\n")

	def getFileInfo(self, fileUrl, fileName):
		#Get the category path for the file
		categoryPath = "http://www.ticalc.org/"
		splitUrls = fileUrl.split('/')
		for splitUrl in splitUrls:
			if splitUrl != "" and (not "." in splitUrl):
				categoryPath += splitUrl + '/'

		#Now open the category page and extract the URL for the file info page
		categoryPage = urllib.urlopen(categoryPath, "")
		categoryData = categoryPage.read()
		categoryPage.close()
		index = categoryData.find(fileUrl) - 7
		rIndex = categoryData.rfind('A HREF="', 0, index)
		infoUrl = categoryData[rIndex + 9:]
		infoUrl = "http://www.ticalc.org/" + infoUrl[:infoUrl.find('">')]
		
		#Create a file info object
		fileInfo = info.FileInfo(fileUrl, fileName, infoUrl, self.output)
		infoPage = urllib.urlopen(infoUrl)
		infoText = infoPage.read()
		infoPage.close()

		#Fill in all the data bits
		fileInfo.description = self.getBaseFileData(infoText, "Description")
		fileInfo.fileSize = self.getBaseFileData(infoText, "File Size")
		fileInfo.fileDate = self.getBaseFileData(infoText, "File Date and Time", 47, 2)
		fileInfo.documentation = self.getBaseFileData(infoText, "Documentation&nbsp;Included?")
		fileInfo.sourceCode = self.getBaseFileData(infoText, "Source Code")
		fileInfo.category = self.getFileCategory(infoText)
		fileInfo.author = self.getFileAuthor(infoText)
		fileInfo.downloads = self.getNumDownloads(infoText)
		fileInfo.repository = self.name
		
		#Print the file info object
		fileInfo.printData(self.output)
		return fileInfo
	
	def getBaseFileData(self, fileInfo, data, index1 = 47, index2 = 1):
		"""Function to initialize the simple data for file info"""
		result = fileInfo[fileInfo.find(data):]
		result = result[result.find("<FONT ") + index1:]
		result = result[:result.find("</FONT>") - index2]
		return result

	def getFileCategory(self, fileInfo):
		"""Function to get the file category for file info"""
		category = fileInfo[fileInfo.find("Category"):]
		category = category[category.find("<FONT ") + 47:]
		category = category[category.find('">') + 2:]
		category = category[:category.find("</A></B>") - 0]
		return category

	def getFileAuthor(self, fileInfo):
		"""Function to get the file's author for file info, note that we are pretending that multiple authors do not exist here"""
		author = fileInfo[fileInfo.find("Author"):]
		author = author[author.find("<FONT ") + 47:]
		author = author[author.find('<B>') + 3:]
		authormail = author[author.find("mailto:") + 7:]
		authormail = authormail[:authormail.find('"')]
		author = author[:author.find("</B></A>") - 0]
		author = author + " (" + authormail + ")"
		return author

	def getNumDownloads(self, fileInfo):
		"""Function to get the number of times a file has been downloaded"""
		downloads = fileInfo[fileInfo.find("FILE INFORMATION"):]
		if -1 != fileInfo.find("not included in ranking"):
			return "0"
		downloads = downloads[:downloads.find(".<BR>")]
		downloads = downloads[downloads.find("</A> with ") + len("</A> with "):]
		return downloads
		
def getRepository():
	"""Returns the relevant CalcRepository object for this repo file"""
	global name, url
	return TicalcRepository(name, url)
