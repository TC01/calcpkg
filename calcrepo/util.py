import os

from distutils import sysconfig

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