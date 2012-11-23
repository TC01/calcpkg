import os
import pkgutil
import sys

from calcrepo import util

def createRepoObjects():
	"""Imports each 'plugin' in this package and creates a repo file from it"""
	repositories = {}
	repodir = util.getReposPackageFolder()
	for importer, name, ispkg in pkgutil.iter_modules([repodir]):
		module = importer.find_module(name).load_module(name)
		repo_name = module.name
		if module.enabled:
			repositories[repo_name] = module.getRepository()
	
	return repositories
