import os

from distutils import sysconfig

garbageRoots = "/pub", "/files"

def getReposPackageFolder():
	"""Returns the folder the package is located in."""
	libdir = sysconfig.get_python_lib()
	repodir = os.path.join(libdir, "calcrepo", "repos")
	return repodir

def replaceNewlines(string, newlineChar):
	"""There's probably a way to do this with string functions but I was lazy.
		Replace all instances of \r or \n in a string with something else."""
	if newlineChar in string:
		segments = string.split(newlineChar)
		string = ""
		for segment in segments:
			string += segment
	return string

def removeRootFromName(string):
	"""Helper function to remove /pub, /files from string."""
	global garbageRoots
	for root in garbageRoots:
		if root in string:
			string = string[string.find(root) + len(root):]
	return string

def getScriptLocation():
	"""Helper function to get the location of a Python file."""
	location = os.path.abspath("./")
	if __file__.rfind("/") != -1:
		location = __file__[:__file__.rfind("/")]
	return location
