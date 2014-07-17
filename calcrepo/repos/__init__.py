import os
import pkgutil
import sys

from calcrepo import util

def createRepoObjects():
	"""Imports each 'plugin' in this package and creates a repo file from it"""
	repositories = {}
	repodir = os.path.join(getScriptLocation())
	for importer, name, ispkg in pkgutil.iter_modules([repodir]):
		module = importer.find_module(name).load_module(name)
		repo_name = module.name
		if module.enabled:
			repositories[repo_name] = module.getRepository()
	
	return repositories

def getScriptLocation():
	"""Helper function to get the location of a Python file."""
	location = os.path.abspath("./")
	if __file__.rfind("/") != -1:
		location = __file__[:__file__.rfind("/")]
	return location
