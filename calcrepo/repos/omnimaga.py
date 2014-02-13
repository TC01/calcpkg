# Shush, the '2' in the module looks ugly.
import urllib2 as urllib

from calcrepo import info
from calcrepo import repo

name = "omnimaga"
url = "http://www.omnimaga.org/"
enabled = True

class OmnimagaRepository(repo.CalcRepository):
	
	def formatDownloadUrl(self, url):
		return "http://www.omnimaga.org" + url

	def updateRepoIndexes(self, verbose=False):
		self.printd("Reading omnimaga master index (this will take some time).")
		
		# First read in the text (the only network process involved)
		headers = { 'User-Agent' : 'Mozilla/5.0' }
		request = urllib.Request('http://www.omnimaga.org/files/master.index', None, headers)
		masterIndex = urllib.urlopen(request).read()
		self.printd("  Read in omnimaga master index.")

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
		self.printd("Finished updating omnimaga repo.\n")
		
	def getFileInfo(self, fileUrl, fileName):
		return NotImplementedError

def getRepository():
	"""Returns the relevant CalcRepository object for this repo file"""
	global name, url
	return OmnimagaRepository(name, url)
