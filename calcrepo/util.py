import os

from distutils import sysconfig

def getReposPackageFolder():
	"""Returns the folder the package is located in."""
	libdir = sysconfig.get_python_lib()
	repodir = os.path.join(libdir, "calcrepo", "repos")
	return repodir