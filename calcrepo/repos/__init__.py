import os
import pkgutil
import sys

from distutils import sysconfig

def getPackageFolder():
	"""Returns the folder the package is located in."""
	libdir = sysconfig.get_python_lib()
	repodir = os.path.join(libdir, "calcrepo", "repos")
	return repodir

def createRepoObjects():
	"""Imports each 'plugin' in this package and creates a repo file from it"""
	repositories = {}
	repodir = getPackageFolder()
	for importer, name, ispkg in pkgutil.iter_modules([repodir]):
		module = importer.find_module(name).load_module(name)
		repo_name = module.name
		if module.enabled:
			repositories[repo_name] = module.getRepository()
	
	return repositories
