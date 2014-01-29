import urllib

from calcrepo import info
from calcrepo import repo

name = "cemetech"
url = "http://www.cemetech.net/"
enabled = True

class CemetechRepository(repo.CalcRepository):
	
	def formatDownloadUrl(self, url):
		return "http://www.cemetech.net/programs/index.php?mode=file&path=" + url + "&location=archive"

	def updateRepoIndexes(self, verbose=False):
		archiveRoot = "http://www.cemetech.net/programs/index.php?mode=folder&path="
		
		# Recursively list all files
		
		
		return NotImplementedError
		
	def updateFromArchivePage(self, archiveRoot, names, files, parent = "/", verbose=False):
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
		
		
	def getFileInfo(self, fileUrl, fileName):
		#Open the info page and create a file info object
		infoUrl = "http://www.cemetech.net/programs/index.php?mode=file&path=" + fileUrl
		fileInfo = info.FileInfo(fileUrl, fileName, infoUrl, self.output)
		infoPage = urllib.urlopen(infoUrl)
		infoText = infoPage.read()
		infoPage.close()
		
		#Fill in all the data provided by Cemetech
		fileInfo.repository = self.name
		fileInfo.fileName = self.getSimpleFileData(infoText, "Download")
		fileInfo.author = self.getSimpleFileData(infoText, "Author")
		fileInfo.category = self.getSimpleFileData(infoText, "Folder")
		fileInfo.description = self.getComplexFileData(infoText, "Description")
		fileInfo.downloads = self.getComplexFileData(infoText, "Statistics")
	
		print fileInfo.printData(self.output)
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
		
def getRepository():
	"""Returns the relevant CalcRepository object for this repo file"""
	global name, url
	return CemetechRepository(name, url)
