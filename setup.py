#/usr/bin/env python

from distutils.core import setup

import os
import shutil
import sys

#This is really bad, but hey... it works!
scriptname = "calcpkg"
if sys.platform == "win32":
	try:
		print "Creating script as calcpkg.py because we are running Windows\n"
		shutil.copy("calcpkg", "calcpkg.py")
	except:
		pass	#We are not making a distribution, we are installing one or doing some other operation
	scriptname = "calcpkg.py"

setup(	name = "calcpkg",
		version = "2.0",
		description = "ticalc.org package manager",
		long_description = "CLI software to access TI calculator software sites such as ticalc.org.",
		author = "Ben Rosser",
		license = "MIT",
		author_email = "rosser.bjr@gmail.com",
		url = "http://www.ticalc.org/archives/files/fileinfo/433/43348.html",
		packages = ["calcrepo", "calcrepo.repos"],
		scripts = [scriptname],
		package_data={'calcrepo': ['ticalc.files.index', 'ticalc.names.index']} )

#Clean up the mess we made
try:
	if sys.platform == "win32":
		os.remove("calcpkg.py")
except:
	pass
	
