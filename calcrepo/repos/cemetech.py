import urllib

from calcrepo import info
from calcrepo import repo

name = "cemetech"
url = "http://www.cemetech.net/"
enabled = True

class CemetechRepository(repo.CalcRepository):
	
	def formatDownloadUrl(self, url):
		return "http://www.cemetech.net/scripts/countdown.php?" + url

	def updateRepoIndexes(self, verbose=False):
		archiveRoot = "http://www.cemetech.net/programs/index.php?mode=folder&path="
		self.printd("Recursively stepping through Cemetech file categories.")
		
		# Delete and open new indices
		files = self.openIndex(self.index.fileIndex, "files index")
		names = self.openIndex(self.index.nameIndex, "names index")
		if files is None or names is None:
			try:
				files.close()
			except:
				return
		
		# Recursively list all files
		self.updateFromArchivePage(archiveRoot, names, files, verbose=verbose)
		
		# Close the indexes now
		files.close()
		names.close()
		self.printd("Finished updating cemetech repo.\n")

	def updateFromArchivePage(self, archiveRoot, names, files, parent = "/", verbose=False):
		"""Helper function that works recursively over Cemetech file category/directory pages."""
		root = archiveRoot + parent
		archive = urllib.urlopen(root)
		archiveText = archive.read()
		archive.close()
				
		# Recursively call this function on all subdirectories
		working = archiveText
		folderString = 'solid #aaa;"><a href="index.php?mode=folder&path='
		while folderString in working:
			index = working.find(folderString) + len(folderString)
			folder = working[index:]
			folder = folder[:folder.find('>') - 1]
			working = working[index + len(folder):]
			if folder != "" and folder.count("/") > parent.count("/"):
				if verbose:
					self.printd("  Caching " + folder)
				self.updateFromArchivePage(archiveRoot, names, files, folder, verbose)
				
		# Now, step through all files and write them to the names and files objects
		working = archiveText
		fileString = "../scripts/countdown.php?" #/73/basic/games/aod73.zip&path=archives"
		while fileString in working:
			# Get the filename and path of the file
			index = working.find(fileString) + len(fileString)
			fileData = working[index:]
			fileData = fileData[:fileData.find("&path=archives")]
			
			# Get the proper name (title) of the file
			working = working[index:]
			nameData = working[working.find('1.25em;"><b>') + len('1.25em;"><b>'):]
			nameData = nameData[:nameData.find('</B>')]
			
			# Write files to index objects
			files.write(fileData + "\n")
			names.write(nameData + "\n")
		
	def getFileInfo(self, fileUrl, fileName):
		#Open the info page and create a file info object
		infoUrl = "http://www.cemetech.net/programs/index.php?mode=file&path=" + fileUrl
		fileInfo = info.FileInfo(fileUrl, fileName, infoUrl, self.output)
		infoPage = urllib.urlopen(infoUrl)
		infoText = infoPage.read()
		infoPage.close()
		
		#Fill in all the data provided by Cemetech
		fileInfo.repository = self.name
		fileInfo.fileName = fileName #self.getSimpleFileData(infoText, "Download")
		fileInfo.author = self.getSimpleFileData(infoText, "Author")
		fileInfo.category = self.getSimpleFileData(infoText, "Folder")
		fileInfo.description = self.getFileDescription(infoText)
		fileInfo.downloads = self.getComplexFileData(infoText, "Statistics")
		
		fileInfo.printData(self.output)
		return fileInfo

	def getSimpleFileData(self, fileInfo, data):
		"""Function to initialize the simple data for file info"""
		result = fileInfo[fileInfo.find(data + "</td>"):]
		result = result[:result.find("</A></td>")]
		result = result[result.rfind(">") + 1:]
		return result
		
	def getComplexFileData(self, fileInfo, data):
		"""Function to initialize the slightly more complicated data for file info"""
		result = fileInfo[fileInfo.find(data + "</td>") + len(data + "</td>"):]
		result = result[:result.find("</td>")]
		result = result[result.rfind(">") + 1:]
		return result
		
	def getFileDescription(self, fileInfo):
		"""Function to get the description of a file."""
		data = 'Description'
		result = fileInfo[fileInfo.find(data + "</td>") + len(data + "</td>"):]
		result.lstrip()
		result = result[:result.find("</td>")]
		result = result[result.rfind("<"):]
		if "<td" in result:
			result = result[result.find(">") + 1:]
		return result
		
def getRepository():
	"""Returns the relevant CalcRepository object for this repo file"""
	global name, url
	return CemetechRepository(name, url)
