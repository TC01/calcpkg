# So I'm just going to leave this here for now, because:
# Unlike Cemetech and ticalc.org, Omni uses file IDs for downloads
# This could be handled by making files.index just be a list of IDs
# But this sort of breaks searches

# On the other hand, it may be easier to enumerate all files, in that case

# THIS CODE IS CURRENTLY USELESS, DON'T ENABLE THIS REPO

import urllib

from calcrepo import info
from calcrepo import repo

name = "omnimaga"
url = "http://www.omnimaga.org/"
enabled = False

class OmnimagaRepository(repo.CalcRepository):
	
	def formatDownloadUrl(self, url):
		fileid = "???" # See comments above
		return "http://www.omnimaga.org/index.php?action=downloads;sa=downfile&id=" + fileid

	def updateRepoIndexes(self, verbose=False):
		return NotImplementedError
		
	def getFileInfo(self, fileUrl, fileName):
		return NotImplementedError

def getRepository():
	"""Returns the relevant CalcRepository object for this repo file"""
	global name, url
	return OmnimagaRepository(name, url)
