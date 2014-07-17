#!/usr/bin/env python

#Dependencies
import argparse
import os
import sys

#Import the necessary function from repos subpackage
from repos import createRepoObjects

#Main function of script... yeah.
def main():
	"""Core function for the script"""
	commands = ['update', 'list', 'get', 'info', 'count', 'search', 'download']
	parser = argparse.ArgumentParser(description="Command line access to software repositories for TI calculators, primarily ticalc.org and Cemetech")
	parser.add_argument("action", metavar="ACTION", type=str, help="The calcpkg command to execute (count, get, info, list, update)")
	parser.add_argument("string", metavar="STRING", type=str, help="The string to search for when using count, get, info, or list commands", nargs="?", default="")
	
	parser.add_argument("-c", "--category", dest="category", help="Limit searching to a specified category", default="")
	parser.add_argument("-e", "--extension", dest="extension", help="Limit searching to a specified file extension", default="")
	parser.add_argument("-f", "--filename", dest="searchFiles", action="store_true", help="Search by archive filenames rather than descriptive package name")
	parser.add_argument("-g", "--game", dest="game", action="store_true", help="Limit searching to games only")
	parser.add_argument("-m", "--math", dest="math", action="store_true", help="Limit searching to math and science programs only")
	parser.add_argument("-r", "--repository", dest="repo", help="Limit searching by one repository- default is to use all", default="")
	parser.add_argument("-v", "--verbose", dest="verbose", action="store_true", help="Always provide verbose output")
	parser.add_argument("-x", "--extract", dest="extract", action="store_true", help="After downloading, autoextract archive files when possible")
	parser.add_argument("-y", "--assume-yes", dest="prompt", action="store_false", help="Never prompt for verification of command")
	args = parser.parse_args()

	#Verify that a valid command was specified
	if not args.action in commands:
		print "Error: Invalid action specified, action must be one of " + str(commands)
		return
	
	#args.category is special
	if args.category != "":
		category = "/" + args.category + "/"
	else:
		category = ""
	
	#Initialize repositories; all behind-the-scene processing is done by plugins in calcrepo.repos
	repositories = createRepoObjects()
	if args.repo != "":
		for repoName, repository in repositories.iteritems():
			if repoName != args.repo:
				repositories[repoName] = None
	
	#Now, run commands for each repo		
	for name, repository in repositories.iteritems():
		if repository != None:
			repository.setRepoData(args.string, category, args.extension, args.math, args.game, args.searchFiles)
			if args.action == "update":
				repository.updateRepoIndexes(args.verbose)
			elif (args.action == "list" or args.action == "search"):
				repository.searchIndex()
			elif (args.action == "get" or args.action == "download"):
				repository.searchIndex()
				repository.downloadFiles(args.prompt, args.extract)
			elif args.action == "info":
				repository.getFileInfos()
			elif args.action == "count":
				repository.countIndex()
				
if __name__ == '__main__':
	main()
